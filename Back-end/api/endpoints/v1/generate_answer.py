from fastapi import APIRouter, Depends, HTTPException, status
from models.generate_answer import GenerationResponse,GenerationRequest,ErrorResponse
from fastapi.responses import JSONResponse, StreamingResponse
from langchain_core.messages import HumanMessage
from fastapi import FastAPI, HTTPException, Header, Query
from agents.builder import build_graph
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
