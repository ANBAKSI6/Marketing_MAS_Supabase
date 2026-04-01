import asyncio
from graph.graph import graph
from langchain_core.messages import HumanMessage

async def main():
    msgs = []
    while True:
        q = input("You: ")
        msgs.append(HumanMessage(content=q))
        res = await graph.ainvoke({"messages": msgs})
        msgs = res["messages"]
        print("AI:", msgs[-1].content)

asyncio.run(main())