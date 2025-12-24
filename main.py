from langchain_core.messages import HumanMessage
# langchain is a high level framework that allows us to build AI applications

from langchain_openai import ChatOpenAI
# langchain_openai allows us to use open AI within langchain and langgraph
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
# langgraph is a complex framework that allows us three to build AI Agents
from dotenv import load_dotenv
#dotenv allows to load environment variable files from out python script