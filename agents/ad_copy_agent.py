from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

# _llm = ChatBedrock(model="global.anthropic.claude-haiku")
_llm =ChatBedrock(model="anthropic.claude-3-haiku-20240307-v1:0")

@tool
def create_ad_copy(business_name: str):
    """Generate ad copy for a given business."""
    
    prompt = f"""
Create ad copy for {business_name}.
Return only ad content. No explanation.
"""
    response = _llm.invoke([HumanMessage(content=prompt)])
    return response.content