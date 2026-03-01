from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()


template=PromptTemplate(template="""

        give me answer of this question  : {question} in less than 50 words
                        """,
                        input_variables=['question'],
                        validate_template=True)


model=ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-5.2-2025-12-11", temperature=0.9)


x=template.invoke('what is capital of india')

response=model.invoke(x).content

print(response)