from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from api.api_router import generate_answer_router
import asyncio
import uvicorn