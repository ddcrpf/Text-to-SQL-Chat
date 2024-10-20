from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_openai import OpenAI
import os

class SQLAgent:
    def __init__(self):
        db = SQLDatabase.from_uri(os.getenv("SQL_DATABASE_URI"))
        llm = OpenAI(temperature=0)
        toolkit = SQLDatabaseToolkit(db=db, llm=llm)

        self.agent_executor = create_sql_agent(
            llm=llm,
            toolkit=toolkit,
            verbose=True
        )

    def run(self, query):
        return self.agent_executor.run(query)