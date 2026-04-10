# City Intelligence Tool

### Tools
### AI Agents
### Tool Calling
### LangChain agent (langchain.agents)
### Integrating external API to empower tools

This is a city intelligence tool

To create this we have used

1. Weather Tool
    API: OpenWeatherMap

2. News Search Tool
    API: Tavily

3. LLM
    API: MISTRAL

4. Prompt Template
    API: LangChain

Flow :

User Query 

-> 

LLM Decision
    -> weather? -> to call weather tool
    -> News? -> to call news tool

->

Tool result

->

LLM formats the final answer

