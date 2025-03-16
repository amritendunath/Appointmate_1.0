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
    
    def route_update_info(self, state: State):
        route = tools_condition(state)
        if route == END:
            return END
        tool_calls = state["messages"][-1].tool_calls
        did_cancel = any(tc["name"] == CompleteOrEscalate.__name__ for tc in tool_calls)
        if did_cancel:
            return "leave_skill"
        safe_toolnames = [t.name for t in self.tools]
        if all(tc["name"] in safe_toolnames for tc in tool_calls):
            return self.update_tool