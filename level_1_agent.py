from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.ollama import Ollama

def SayHello() -> str:
    """
    Whenever User asks to "Say Hello" use this function

    Args:
        No arguments
    Returns:
        str: String message as response
    """
    print("I said Hello")
    return "I Said Hello"

agent = Agent(
    model=Ollama(id="llama3.2:latest"),
    tools=[DuckDuckGoTools(), SayHello],
    instructions="Use tables to display data. Don't include any other text.",
    markdown=True,
    show_tool_calls=True
)
agent.print_response("Say Hello", stream=True)
# agent.print_response("What is the stock price of Apple?", stream=True)


