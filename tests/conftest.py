import os

import pytest
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

from src.variables import environment_vars

os.environ["OPENAI_API_KEY"] = environment_vars.openai_api_key
os.environ["PINECONE_API_KEY"] = environment_vars.pinecone_api_key


@pytest.fixture()
def vector_db():
    return PineconeVectorStore(embedding=OpenAIEmbeddings(), index_name=environment_vars.pinecone_index_name)
