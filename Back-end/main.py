from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from api.api_router import generate_answer_router
import asyncio
import uvicorn


app = FastAPI(
    title="Doctor's Appointment Agentic Flow",
    version="1.0.0",
    description="Allow users to find and book availbility",
    openapi_url="/openapi.json",
    docs_url="/",
)