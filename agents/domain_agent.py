from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

_llm = ChatBedrock(model="global.anthropic.claude-haiku")

@tool
def get_domain_suggestions(business_name: str):
    """Generate domain name suggestions."""
    
    prompt = f"""
Generate 10 domain names for {business_name}.
Return only domain names list.
"""
    response = _llm.invoke([HumanMessage(content=prompt)])
    return response.content