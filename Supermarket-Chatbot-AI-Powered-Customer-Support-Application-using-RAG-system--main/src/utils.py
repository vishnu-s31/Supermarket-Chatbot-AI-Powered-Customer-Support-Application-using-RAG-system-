import logging
from dotenv import load_dotenv
import os

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('supermarket_chatbot.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def load_config():
    load_dotenv()
    config = {
        'MYSQL_HOST': os.getenv('MYSQL_HOST'),
        'MYSQL_USER': os.getenv('MYSQL_USER'),
        'MYSQL_PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'MYSQL_DB': os.getenv('MYSQL_DB'),
        'DEEPSEEK_API_KEY': os.getenv('DEEPSEEK_API_KEY')
    }
    missing = [key for key, value in config.items() if value is None]
    if missing:
        setup_logging().error(f"Missing environment variables: {missing}")
        raise ValueError(f"Missing environment variables: {missing}")
    return config

def format_product_response(product):
    if not product:
        return "No product found."
    return (f"{product['name']} ({product['brand']})\n"
            f"Category: {product['category']}\n"
            f"Price: ₹{product['price']}\n"
            f"In Stock: {'Yes' if product['in_stock'] else 'No'}\n"
            f"Stock Quantity: {product['stock_quantity']}\n"
            f"Description: {product['description']}")

logger = setup_logging()
