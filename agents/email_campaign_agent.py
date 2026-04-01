from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

# _llm = ChatBedrock(model="global.anthropic.claude-haiku")
_llm = ChatBedrock(model="anthropic.claude-3-haiku-20240307-v1:0")

@tool
def create_email_campaign(business_name: str):
    """Generate email marketing campaign."""
    
    prompt = f"""
Create a 3-step email marketing campaign for {business_name}.
Return only email content.
"""
    response = _llm.invoke([HumanMessage(content=prompt)])
    return response.content