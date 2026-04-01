from graph.state import AgentState
from graph.prompt import SYSTEM_PROMPT
from agents.tools import tools

from langchain_aws import ChatBedrock
from langchain_core.messages import SystemMessage
from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition

_llm = ChatBedrock(model="global.anthropic.claude-sonnet-4-6")
_llm_with_tools = _llm.bind_tools(tools)

async def agent_node(state: AgentState):
    messages = [SystemMessage(content=SYSTEM_PROMPT)] + state["messages"]
    response = await _llm_with_tools.ainvoke(messages)
    return {"messages": [response]}

def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("agent", agent_node)
    builder.add_node("tools", ToolNode(tools))

    builder.add_edge(START, "agent")
    builder.add_conditional_edges("agent", tools_condition)
    builder.add_edge("tools", "agent")

    return builder.compile()

graph = build_graph()