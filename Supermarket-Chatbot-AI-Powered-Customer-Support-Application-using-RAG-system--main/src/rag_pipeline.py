import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import requests
import pickle
from fuzzywuzzy import fuzz
from src.db_connect import fetch_product_by_id, fetch_all_products
from src.utils import logger, load_config, format_product_response
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
class RAGPipeline:
    def __init__(self):
        self.config = load_config()
        if not self.config.get('DEEPSEEK_API_KEY'):
            logger.error("DEEPSEEK_API_KEY not found in config")
            raise ValueError("DEEPSEEK_API_KEY not found in config")
        self.model_name = self.config.get('LLM_MODEL', 'deepseek/deepseek-chat-v3-0324:free')  # Load model from .env
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        try:
            faiss_index_path = os.path.join(PROJECT_ROOT, 'data', 'faiss_index', 'product_index.faiss')
            mappings_path = os.path.join(PROJECT_ROOT, 'data', 'mappings', 'product_mapping.pkl')
            self.index = faiss.read_index(faiss_index_path)
            with open(mappings_path, 'rb') as f:
                mappings = pickle.load(f)
                self.product_ids = mappings['ids']
                self.products = mappings['products']
            logger.info(f"Loaded FAISS index from {faiss_index_path}")
            logger.info(f"Loaded product mappings from {mappings_path}")
        except Exception as e:
            logger.error(f"Failed to load FAISS index or mappings: {e}")
            raise
    def preprocess_query(self, query):
        query = query.lower()
        corrections = {
            'coco cola': 'coca cola',
            'coka cola': 'coca cola',
            'cocacola': 'coca cola',
        }
        for wrong, correct in corrections.items():
            if wrong in query:
                logger.info(f"Correcting query from '{query}' to '{query.replace(wrong, correct)}'")
                query = query.replace(wrong, correct)
        return query
    def retrieve(self, query, top_k=5):
        try:
            query = self.preprocess_query(query)
            query_embedding = self.model.encode([query], show_progress_bar=False)
            distances, indices = self.index.search(query_embedding, top_k)
            retrieved_product_ids = [self.product_ids[idx] for idx in indices[0]]
            retrieved_products = [fetch_product_by_id(product_id) for product_id in retrieved_product_ids]
            retrieved_products = [p for p in retrieved_products if p is not None]
            if not any('orange' in p['name'].lower() for p in retrieved_products if p):
                logger.info("No exact matches with embedding search, trying fuzzy matching...")
                all_products = fetch_all_products()
                for product in all_products:
                    if fuzz.partial_ratio(query, product['name'].lower()) > 80:
                        if product not in retrieved_products:
                            retrieved_products.append(product)
            logger.info(f"Retrieved {len(retrieved_products)} products for query: {query}")
            logger.info(f"Products: {[p['name'] for p in retrieved_products if p]}")
            return retrieved_products
        except Exception as e:
            logger.error(f"Error during retrieval: {e}")
            return []
    def generate_response(self, query, products):
        query = self.preprocess_query(query)
        if not products and "list" in query.lower() and "product" in query.lower():
            logger.info("Broad product list query detected, fetching all products")
            products = fetch_all_products()
            if not products:
                logger.warning("No products available in database")
                return "Sorry, no products are available at the moment."
        if not products:
            logger.warning(f"No products found for query: {query}")
            return "Sorry, I couldn't find any products matching your query."
        product_texts = [format_product_response(p) for p in products]
        product_context = "\n\n".join(product_texts)
        prompt = (
            f"You are a helpful supermarket customer support assistant. "
            f"Answer the customer's query based on the following product information:\n\n"
            f"{product_context}\n\n"
            f"Customer Query: {query}\n"
            f"Provide a concise, friendly, and accurate response."
        )
        try:
            headers = {
                'Authorization': f"Bearer {self.config['DEEPSEEK_API_KEY']}",
                'Content-Type': 'application/json',
                'HTTP-Referer': 'http://localhost:5000',  # Optional for OpenRouter
                'X-Title': 'Supermarket Chatbot',  # Optional for OpenRouter
            }
            payload = {
                'model': self.model_name,  # Use model from .env
                'messages': [{'role': 'user', 'content': prompt}],
                'max_tokens': 150
            }
            logger.info("Sending request to OpenRouter API...")
            response = requests.post(
                'https://openrouter.ai/api/v1/chat/completions',  # OpenRouter endpoint
                json=payload,
                headers=headers
            )
            response.raise_for_status()
            if 'choices' not in response.json() or not response.json()['choices']:
                logger.error("OpenRouter API response missing 'choices'")
                return "Sorry, there was an issue processing your request. Please try again."
            answer = response.json()['choices'][0]['message']['content']
            logger.info(f"Generated response for query: {query}")
            return answer.strip()
        except Exception as e:
            logger.error(f"Error generating response with OpenRouter: {e}")
            return "Sorry, there was an issue processing your request. Please try again."
    def process_query(self, query):
        logger.info(f"Processing query: {query}")
        products = self.retrieve(query)
        response = self.generate_response(query, products)
        return response
if __name__ == "__main__":
    rag = RAGPipeline()
    test_query = "Do you have potato chips?"
    response = rag.process_query(test_query)
    print(f"Query: {test_query}\nResponse: {response}")