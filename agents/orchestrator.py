from .sql_agent import SQLAgent
from .csv_agent import CSVAgent
import os

class Orchestrator:
    def __init__(self):
        self.sql_agent = SQLAgent()
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample.csv')
        self.csv_agent = CSVAgent(csv_path)

    def process_query(self, query):
        # Check for CSV-related keywords in the query
        csv_keywords = ['csv', 'file', 'excel', 'spreadsheet']
        if any(keyword in query.lower() for keyword in csv_keywords):
            return self.csv_agent.run(query)
        else:
            return self.sql_agent.run(query)