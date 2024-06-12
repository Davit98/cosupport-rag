import os

from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

from src.variables import environment_vars

__all__ = ['rag_chain']


os.environ["OPENAI_API_KEY"] = environment_vars.openai_api_key
os.environ["PINECONE_API_KEY"] = environment_vars.pinecone_api_key

vectorstore = PineconeVectorStore(embedding=OpenAIEmbeddings(), index_name=environment_vars.pinecone_index_name)
retriever = vectorstore.as_retriever()

llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

prompt = hub.pull("rlm/rag-prompt")


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
)
