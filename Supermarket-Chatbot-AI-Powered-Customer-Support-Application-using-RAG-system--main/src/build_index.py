import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from src.db_connect import fetch_all_products
from src.utils import logger
import pickle
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
def build_faiss_index():
    logger.info("Fetching products from database...")
    products = fetch_all_products()
    if not products:
        logger.error("No products found in database.")
        return False
    logger.info(f"Retrieved {len(products)} products.")
    try:
        model = SentenceTransformer('all-MiniLM-L6-v2')
        logger.info("Loaded SentenceTransformer model.")
    except Exception as e:
        logger.error(f"Failed to load embedding model: {e}")
        return False
    texts = [f"{p['name']} {p['category']} {p['description'] or ''}" for p in products]
    product_ids = [p['product_id'] for p in products]
    try:
        embeddings = model.encode(texts, show_progress_bar=True)
        logger.info("Generated embeddings for products.")
    except Exception as e:
        logger.error(f"Failed to generate embeddings: {e}")
        return False
    try:
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(embeddings)
        logger.info("Built FAISS index.")
    except Exception as e:
        logger.error(f"Failed to build FAISS index: {e}")
        return False
    try:
        faiss_index_dir = os.path.join(PROJECT_ROOT, 'data', 'faiss_index')
        mappings_dir = os.path.join(PROJECT_ROOT, 'data', 'mappings')
        faiss_index_path = os.path.join(faiss_index_dir, 'product_index.faiss')
        mappings_path = os.path.join(mappings_dir, 'product_mapping.pkl')
        os.makedirs(faiss_index_dir, exist_ok=True)
        os.makedirs(mappings_dir, exist_ok=True)
        faiss.write_index(index, faiss_index_path)
        with open(mappings_path, 'wb') as f:
            pickle.dump({'ids': product_ids, 'products': products}, f)
        logger.info(f"Saved FAISS index to {faiss_index_path}")
        logger.info(f"Saved product mappings to {mappings_path}")
        return True
    except Exception as e:
        logger.error(f"Failed to save FAISS index or mappings: {e}")
        return False
if __name__ == "__main__":
    success = build_faiss_index()
    if success:
        logger.info("FAISS index building completed successfully.")
    else:
        logger.error("FAISS index building failed.")