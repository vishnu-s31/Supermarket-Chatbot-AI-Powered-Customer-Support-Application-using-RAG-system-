import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, request, render_template, session, jsonify
from src.rag_pipeline import RAGPipeline
from src.utils import logger
app = Flask(__name__, template_folder=os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'templates'))
app.secret_key = 'your_secret_key_here'  # Required for session management
logger.info(f"Template folder set to: {app.template_folder}")
rag_pipeline = None
def initialize_rag():
    global rag_pipeline
    try:
        logger.info("Starting RAG pipeline initialization...")
        rag_pipeline = RAGPipeline()
        logger.info("RAG pipeline initialized successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize RAG pipeline: {e}")
        raise
@app.route('/', methods=['GET', 'POST'])
def chatbot():
    if 'chat_history' not in session:
        session['chat_history'] = []
    if request.method == 'POST':
        try:
            query = request.form.get('query')
            if not query or not query.strip():
                logger.warning("Invalid request: Empty query")
                session['chat_history'].append({'query': query, 'response': 'Error: Query cannot be empty'})
            else:
                logger.info(f"Processing query: {query}")
                response = rag_pipeline.process_query(query)
                logger.info(f"Query processed successfully: {query}")
                session['chat_history'].append({'query': query, 'response': response})
            session.modified = True
        except Exception as e:
            logger.error(f"Error processing query: {e}")
            session['chat_history'].append({'query': query, 'response': 'Error: Internal server error'})
            session.modified = True
    return render_template('chatbot.html', chat_history=session['chat_history'])
@app.route('/query', methods=['POST'])
def handle_query():
    try:
        data = request.get_json()
        if not data or 'query' not in data:
            logger.warning("Invalid request: Missing query field")
            return jsonify({'error': 'Missing query field'}), 400
        query = data['query']
        if not query.strip():
            logger.warning("Invalid request: Empty query")
            return jsonify({'error': 'Query cannot be empty'}), 400
        logger.info(f"Processing query: {query}")
        response = rag_pipeline.process_query(query)
        logger.info(f"Query processed successfully: {query}")
        return jsonify({'response': response}), 200
    except Exception as e:
        logger.error(f"Error processing query: {e}")
        return jsonify({'error': 'Internal server error'}), 500
if __name__ == "__main__":
    logger.info("Starting Flask server...")
    initialize_rag()
    app.run(host='0.0.0.0', port=5000, debug=True)