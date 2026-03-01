import streamlit as st
import requests

url='http://127.0.0.1:8000/get_answer'

st.header('langchain with streamlit')

question=st.text_input('Enter your question here')

if st.button('Get Answer'):
    response=requests.get(url, params={'question': question})
    st.write(response.text)