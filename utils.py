import os
import sys

import openai
# required accelerate and transformers
from llama_index import VectorStoreIndex, SimpleDirectoryReader

openai.api_key = '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'
os.environ["OPENAI_API_KEY"] = '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'


def read_pdf(datafile_folder=os.path.dirname(os.path.abspath(sys.argv[0]))+"\\yourPdf"):
    global documents
    documents = SimpleDirectoryReader(datafile_folder).load_data()


def load_data():
    global query_engine
    try:
        index = VectorStoreIndex.from_documents(documents, show_progress=True)
        query_engine = index.as_query_engine()
    except Exception as e:
        print(e)
        print("Please re-start again")


def ask_question(question: str):
    return query_engine.query(question)
