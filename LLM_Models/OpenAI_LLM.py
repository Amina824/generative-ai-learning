from langchain_openai import OpenAI

#to load private key from .env file
from dotenv import load_dotenv
load_dotenv()

#Selecting a LLm model of OpenAI from langchain
llm1 = OpenAI(model="gpt-3.5-turbo-instruct")
result=llm1.invoke(" Tell me about 5 business ideas")
print(result)