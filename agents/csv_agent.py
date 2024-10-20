from langchain_experimental.agents import create_csv_agent
from langchain_openai import ChatOpenAI
import pandas as pd
import chardet
import os

class CSVAgent:
    def __init__(self, csv_file):
        df = self.read_csv_with_encoding(csv_file)
        self.agent = create_csv_agent(
            ChatOpenAI(temperature=0, model="gpt-3.5-turbo"),
            csv_file,
            verbose=True,
            allow_dangerous_code=True  
        )

    def read_csv_with_encoding(self, file_path):
        encodings = ['utf-8', 'iso-8859-1', 'windows-1252']
        
        for encoding in encodings:
            try:
                return pd.read_csv(file_path, encoding=encoding)
            except UnicodeDecodeError:
                continue
        
        with open(file_path, 'rb') as file:
            raw_data = file.read()
        detected_encoding = chardet.detect(raw_data)['encoding']
        
        try:
            return pd.read_csv(file_path, encoding=detected_encoding)
        except:
            raise ValueError(f"Unable to read the CSV file. Detected encoding: {detected_encoding}")

    def run(self, query):
        return self.agent.run(query)