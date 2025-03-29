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