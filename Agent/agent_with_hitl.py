from dotenv import load_dotenv

load_dotenv()

import os
import requests

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from tavily import TavilyClient
from rich import print

# Create Tools

# 1 - Weather Tool using OpenWeather API

@tool
def get_weather(city: str) -> str:
    """ Get current weather of the given city """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()
    
    if str(data.get("cod")) != "200":
        return f"Error: {data.get('message', 'Could not fetch the weather data')}"

    temp = data['main']['temp']
    desc = data['weather'][0]['description']

    return f"Weather in {city}: {desc}, {temp}°C"

# print(get_weather.invoke("Kolkata"))

# 2 - News Search Tool using Tavily API

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def get_news(city: str) -> str:
    """ Get latest news about the given city """

    response = tavily_client.search(
        query=f"Latest news about {city}",
        search_depth="basic",
        max_results=3
    )

    results = response.get("results", [])

    if not results:
        return f"No news found for {city}"

    news_list = []

    for r in results:
        title = r.get("title", "No Title")
        url = r.get("url", "")
        snippet = r.get("content", "")
        
        news_list.append(
            f"- {title}\n  🔗 {url}\n  📝 {snippet[:100]}..."
        )

    return f"Latest news in {city}:\n\n" + "\n\n".join(news_list)

# print(get_news.invoke("Kolkata"))

# Step - : Setup LLM and Bind Tools

llm = ChatMistralAI(model="mistral-small-2506")

available_tools = [get_weather, get_news]

tools = {
    "get_weather": get_weather,
    "get_news": get_news
}

llm_with_tool = llm.bind_tools(available_tools)

# Agent Loop

messages = []

print("City Intelligent System")
print("Type exit to quit")

while True:
    prompt = input("You: ")
    if prompt.lower() == "exit":
        break
    messages.append(HumanMessage(prompt))

    while True:
        result = llm_with_tool.invoke(messages)
        

        # if tool is required
        if result.tool_calls:
            messages.append(result)
            tool_call_denied_by_user = False
            for tool_call in result.tool_calls:
                tool_name = tool_call["name"]
                #HUMAN IN THE LOOP
                confirm = input(f"Agent wants to call {tool_name} (y/n):")

                if confirm.lower() == "n":
                    print("Tool call denied and I cannot get the latest info.")
                    tool_call_denied_by_user = True
                    break

                tool_message = tools[tool_name].invoke(tool_call["args"])
                messages.append(ToolMessage(
                    content = tool_message,
                    tool_call_id = tool_call["id"]
                ))

            if tool_call_denied_by_user:
                messages.pop() # remove the AIMessage
                break 

            continue
        else:
            print(result.content)
            break
