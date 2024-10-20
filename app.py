from flask import Flask, request, jsonify, render_template
from agents.orchestrator import Orchestrator
from dotenv import load_dotenv
import logging

load_dotenv()

app = Flask(__name__)
orchestrator = Orchestrator()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    user_query = data.get('query')
    
    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        logger.info(f"Received query: {user_query}")
        result = orchestrator.process_query(user_query)
        logger.info(f"Query result: {result}")
        return jsonify({"result": result})
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)