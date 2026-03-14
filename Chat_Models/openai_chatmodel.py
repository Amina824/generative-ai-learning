from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="gpt-3.5-turbo", temperature=1.5, max_completion_tokens=10)
result=model.invoke("Give the information about granular energy certificates")
print(result.content)
