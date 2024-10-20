# Text-to-SQL Query System with Multi-Source Data
### Project Demo Video: [Youtube video link](https://youtu.be/NpuQf5pdtqY)
## Project Overview

This project implements a Text-to-SQL Query System that can convert natural language queries into SQL queries to retrieve data from multiple sources, including a MySQL database and CSV files. The system uses Langchain, Flask, and Python to create an intelligent agent that can understand and process queries for different data sources.

## Project Design
![Text-to-SQL Project Design](app_images/text-to-sql.jpg)

## Features

- Convert natural language queries to SQL queries
- Query data from MySQL database
- Query data from CSV files
- RESTful API for submitting queries
- Simple web interface for interacting with the system

## APP Images
![Text-to-SQL DB Query](app_images/db_query_img.png)
![Text-to-SQL CSV File Query](app_images/csv_query_img.png)

## Prerequisites

- Python 3.7+
- pip (Python package manager)
- MySQL database (for SQL queries)
- OpenAI API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/text-to-sql-system.git
   cd text-to-sql-system
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   Create a `.env` file in the root directory and add the following:
   ```
   OPENAI_API_KEY=your_openai_api_key
   SQL_DATABASE_URI=mysql://username:password@host:port/database
   ```

## Project Structure
```
text_to_sql_system/
├── app.py
├── agents/
│   ├── __init__.py
│   ├── sql_agent.py
│   ├── csv_agent.py
│   └── orchestrator.py
├── data/
│   └── sample.csv
├── templates/
│   └── index.html
├── .env
└── README.md
```


## Usage

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000` to use the web interface.

3. To use the API directly, send a POST request to `http://localhost:5000/query` with a JSON payload:
   ```
   curl -X POST http://localhost:5000/query \
        -H "Content-Type: application/json" \
        -d '{"query": "Show me all customers in the USA"}'
   ```

## API Endpoints

- `POST /query`: Submit a natural language query
  - Request body: `{"query": "Your natural language query here"}`
  - Response: JSON object with the query result or error message
