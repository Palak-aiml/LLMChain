"""
llmchain/deployment/server.py

Basic FastAPI server for LLMChain deployment.
"""
from fastapi import FastAPI, Request
from llmchain.llms.dummy_llm import DummyLLM

app = FastAPI()
llm = DummyLLM()

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    response = llm.generate(prompt)
    return {"response": response}
