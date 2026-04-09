from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain.tools import tool 
from langchain_core.messages import HumanMessage, ToolMessage
from rich import print
import operator

# 1. Define your custom tools

@tool
def get_text_length(text: str) -> int:
    """Returns the number of characters in a given text."""
    return len(text)

@tool
def calculator(a: float, b: float, operation: str) -> float:
    """
    Performs a mathematical calculation.
    
    Args:
        a: The first number.
        b: The second number.
        operation: The operation to perform, either 'add', 'subtract', 'multiply', or 'divide'.
    """
    op_map = {
        'add': operator.add,
        'subtract': operator.sub,
        'multiply': operator.mul,
        'divide': operator.truediv,
    }
    if operation not in op_map:
        raise ValueError("Invalid operation. Must be one of 'add', 'subtract', 'multiply', 'divide'.")
    return op_map[operation](a, b)


# A list of all available tools
available_tools = [get_text_length, calculator]

# A dictionary to map tool names to their functions for execution
tool_map = {
    "get_text_length": get_text_length,
    "calculator": calculator,
}

llm = ChatMistralAI(model = "mistral-small-2506")

# 2. Bind the tools to the LLM
llm_with_tools = llm.bind_tools(available_tools)

# 3. Create the chat loop
messages = []
prompt = input("You: ")
messages.append(HumanMessage(prompt))

# First invocation to get the tool calls
ai_response = llm_with_tools.invoke(messages)
messages.append(ai_response)

print("Initial AI Response:", ai_response)

# 4. Execute tool calls if any
if ai_response.tool_calls:
    for tool_call in ai_response.tool_calls:
        print(f"Executing tool: {tool_call['name']} with args: {tool_call['args']}")
        tool_function = tool_map[tool_call["name"]]
        # Safely call the tool with its arguments
        tool_output = tool_function.invoke(tool_call["args"])
        
        # Append the tool's output to the message history
        messages.append(ToolMessage(content=str(tool_output), tool_call_id=tool_call['id']))

    # Second invocation with the tool output
    final_response = llm_with_tools.invoke(messages)
    print("\nFinal Response:")
    print(final_response.content)
else:
    # If no tool was called, the first response is the final one
    print("\nFinal Response:")
    print(ai_response.content)
