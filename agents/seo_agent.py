from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

# _llm = ChatBedrock(model="global.anthropic.claude-haiku")
_llm = ChatBedrock(model="anthropic.claude-3-haiku-20240307-v1:0")

@tool
def generate_seo_keywords(business_name: str):
    """Generate SEO keywords."""
    
    prompt = f"""
Generate SEO keywords for {business_name}.
Return only keywords list.
"""
    response = _llm.invoke([HumanMessage(content=prompt)])
    return response.content