# GenAI Tools and Agent Basics

This project demonstrates fundamental concepts in Generative AI, including the use of Tools, AI Agents, and Tool Calling within the LangChain framework.

## Key Concepts Demonstrated

### Tools
Tools are functions that an AI agent can use to interact with the outside world. They allow the agent to go beyond its training data and access real-time information or perform specific actions.

### AI Agents
An AI Agent is a system that uses a Large Language Model (LLM) to reason about a problem, create a plan, and execute that plan using a set of available tools. The agent determines which tools to use and in what order to best answer the user's request.

### Tool Calling
Tool calling is the process by which the LLM, acting as the agent's reasoning engine, determines which tool to use and with what arguments to respond to a user's query. The agent then executes that tool call and uses the result to inform its final response.

### LangChain (`langchain.agents`)
This project uses the LangChain library, specifically its `agents` module, to build the agent. LangChain provides a powerful and flexible framework for developing applications powered by language models, including abstracting away much of the complexity of agent creation.

### Integrating External APIs
To empower the tools, this project integrates with external APIs:
-   **OpenWeatherMap API**: Used by the weather tool to fetch real-time weather data.
-   **Tavily API**: Used by the news tool to search for the latest news articles.
-   **Mistral AI API**: Used for the LLM that powers the agent's reasoning.

## Example Implementation: City Intelligence Tool

This repository contains a practical example of these concepts in the form of a **City Intelligence Tool**.

You can find the implementation in the `Agent/` directory.

### Features
- **Weather Information:** Get real-time weather data for any city.
- **Latest News:** Fetches the latest news articles for a specified city.
- **Interactive Agent:** An interactive command-line interface to chat with the agent.
- **Human-in-the-loop:** Includes a mechanism for human approval before executing tool calls, ensuring user control.

