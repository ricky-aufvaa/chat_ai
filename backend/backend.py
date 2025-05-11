# from langchain_community.llms import huggingface_hub
# from langchain_huggingface import HuggingFaceEndpoint

# import os
# from getpass import getpass
# from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace


# from langchain_core.prompts import (ChatPromptTemplate,
# HumanMessagePromptTemplate,
# SystemMessagePromptTemplate)



from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# os.environ['HUGGINGFACEHUB_API_TOKEN'] = "key"

def initiate_llm():
    llm = HuggingFaceEndpoint(
        repo_id="microsoft/Phi-3-mini-4k-instruct",
        task="text-generation",
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
    )

    chat = ChatHuggingFace(llm=llm, verbose=True)
    return chat





app = FastAPI()
# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

# def llm_chain(query):
#     chat = initiate_llm()
#     system_prompt = SystemMessagePromptTemplate.from_template("You are an intellegent rapper")
#     human_prompt = HumanMessagePromptTemplate.from_template("{query}", input_variables=["query"])
#     prompt = ChatPromptTemplate.from_messages([system_prompt,human_prompt])
#     final_prompt = prompt.format_messages(query = query)
#     response = chat.invoke(final_prompt)
#     return response.content

#endpoint
@app.post("/query")
def queryendpoint(request:QueryRequest):
    query = request.query
    # response = llm_chain(query)
    response = f"Your query was {query} and how are you?"

    if response:
        return {"answer":response}
    else:
        return {"answer": "no response from the backend"}