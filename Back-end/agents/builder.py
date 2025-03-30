import os
from langgraph.graph import StateGraph
from agents.agentstate import State
from agents.base import Assistant
from langgraph.graph import START, END
from utils.helper import create_entry_node
from langchain_openai import AzureChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv
from agents.agents import get_runnable
from models.agents import CompleteOrEscalate
from utils.prompts import info_agent_prompt,booking_agent_prompt,primary_agent_prompt
from tools.tools import (
    set_appointment,
    reschedule_appointment,
    cancel_appointment,
    check_availability_by_specialization,
    check_availability_by_doctor
)
from models.agents import ToAppointmentBookingAssistant, ToGetInfo, ToPrimaryBookingAssistant
from utils.helper import (
    create_tool_node_with_fallback,
    pop_dialog_state,
    RouteUpdater,
    route_to_workflow,
    route_primary_assistant
)

from utils.config import get_settings
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

conn = sqlite3.connect('checkpoints.db',check_same_thread=False)

memory = SqliteSaver(conn)

Azure_Creds = get_settings()

os.environ["LANGCHAIN_TRACING_V2"] = 'true'
os.environ["LANGCHAIN_ENDPOINT"] = Azure_Creds.LANGCHAIN_ENDPOINT
os.environ["LANGCHAIN_API_KEY"] = Azure_Creds.LANGCHAIN_API_KEY
os.environ["LANGCHAIN_PROJECT"] = Azure_Creds.LANGCHAIN_PROJECT


llm = AzureChatOpenAI(temperature=0,
                           api_key=Azure_Creds.AZURE_OPENAI_API_KEY,
                           azure_endpoint=Azure_Creds.AZURE_OPENAI_ENDPOINT,
                           openai_api_version=Azure_Creds.AZURE_OPENAI_VERSION,
                           azure_deployment=Azure_Creds.AZURE_GPT4O_MODEL
                           )