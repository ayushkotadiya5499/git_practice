import streamlit as st
import requests

st.header('welcome to conflict world ')

url='http://127.0.0.1:8000/get_answer'
url1='http://127.0.0.1:8000/get_answer_with_translate'

st.header('langchain with streamlit')
st.success('this is only mine what')
question=st.text_input('Enter your question here ok under 50 words')

if st.button('Get Answer'):
    response=requests.get(url, params={'question': question})
    st.success(response.text)
    st.balloons()

if st.button('Get Answer with Translate'):
    response=requests.get(url1, params={'question': question})
    st.success(response.text)
    st.balloons()