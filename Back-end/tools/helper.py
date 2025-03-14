from agents.AgentState import State
from models.agents import CompleteOrEscalate,ToAppointmentBookingAssistant
from langgraph.prebuilt import tools_condition, ToolNode
from langgraph.graph import END
from langchain_core.messages import ToolMessage
from langchain_core.runnables import RunnableLambda
from typing import Callable, Literal

class RouteUpdater:
    def __init__(self, tools,update_tool):
        self.tools = tools
        self.update_tool = update_tool