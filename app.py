from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun
from langchain.output_parsers import StructuredOutputParser

import streamlit as st

arxiv_wrapper = ArxivAPIWrapper()
arxiv_query_run = ArxivQueryRun(api_wrapper=arxiv_wrapper)

st.title("Arxiv Search")

query = st.text_input("Enter a query:")

if st.button("Search"):
    if query:
        result = arxiv_query_run.invoke(query)
        st.write(result)