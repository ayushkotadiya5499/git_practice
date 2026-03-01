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


model=ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4.1-mini", temperature=0.9)

app = FastAPI()

@app.get('/get_answer')
def get_answer(question):
    x=template.invoke(question)
    response=model.invoke(x).content
    return response