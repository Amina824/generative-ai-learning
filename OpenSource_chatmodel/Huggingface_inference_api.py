from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
load_dotenv()

llm1= HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text_generation"
)

model= ChatHuggingFace(llm=llm1)


result= model.invoke("tell me capital of pak")
print(result)