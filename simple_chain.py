from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model=ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-3.5-turbo", temperature=0.9)
response=model.invoke("What is the capital of India? and famous food").content
print(response)