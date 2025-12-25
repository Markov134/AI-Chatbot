from langchain_core.messages import HumanMessage
# langchain is a high level framework that allows us to build AI applications

from langchain_openai import ChatOpenAI
# langchain_openai allows us to use open AI within langchain and langgraph
from langchain.tools import tool
#from langgraph.prebuilt import create_react_agent
from langchain.agents import create_agent
# langgraph is a complex framework that allows us three to build AI Agents
from dotenv import load_dotenv
#dotenv allows to load environment variable files from out python script

load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithmeric calculations with numbers"""
    print("tool has been called.")
    return f"The sum of {a} and {b} is {a+b}"

@tool
def say_hello(name: str) -> str:
    """Useful for greeting a user"""
    print("tool has been called.")
    return f"Hello {name}, I hope you are well today."

def main():
    model = ChatOpenAI(model="gpt-4o-mini", temperature = 0) # the higher the temperature the more random model is going to be
                                      # temp 0 means no randomness

    tools = [calculator, say_hello]
    agent_executor = create_agent(model, tools)

    print("Welcome! I am your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break

        print("\nAssistant: ", end="", flush=True)
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]},
            stream_mode="updates"
        ):
            for node_name, node_data in chunk.items():
                if "messages" in node_data:
                    new_msg = node_data["messages"][-1]

                if new_msg.type == "ai" and new_msg.content:
                    print(new_msg.content, end="", flush=True)
        print()

if __name__ == "__main__":
    main()