"""
FastAPI-based UI backend for LLMChain visual tools.
"""
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ui_dir = os.path.join(os.path.dirname(__file__), "frontend")
app.mount("/static", StaticFiles(directory=ui_dir), name="static")

@app.get("/", response_class=HTMLResponse)
def index():
    with open(os.path.join(ui_dir, "index.html")) as f:
        return f.read()
