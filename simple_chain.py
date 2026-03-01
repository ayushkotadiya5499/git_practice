from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
from fastapi import FastAPI


load_dotenv()


template=PromptTemplate(template="""

        give me answer of this question  : {question} in less than 50 words
                        """,
                        input_variables=['question'],
                        validate_template=True)


model=ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-5.2-2025-12-11", temperature=0.9)


app = FastAPI()

@app.get('/get_answer')
def get_answer(question):
    x=template.invoke(question)
    response=model.invoke(x).content
    return response

@app.get('/get_answer_with_translate')
def get_answer2(question):
    x=template.invoke(question)
    response=model.invoke(x).content
    response2=model2.invoke(f"translate this answer in gujarati : {response}")
    return response2.content