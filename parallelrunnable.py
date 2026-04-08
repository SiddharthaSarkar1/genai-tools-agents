from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableLambda

model = ChatMistralAI(model="mistral-small-2506")
op_parser = StrOutputParser()

#Drafting 2 different prompts
short_prompt = ChatPromptTemplate.from_template("Explain {topic} in 1-2 lines")
long_prompt = ChatPromptTemplate.from_template("Explain {topic} in detail")

topic = "Generative AI"

# Convert Dictionary to a runnable, using RunnableParallel
chain = RunnableParallel({
    "short": RunnableLambda(lambda x :x['short']) | short_prompt | model | op_parser,
    "detailed": RunnableLambda(lambda x :x['detailed']) | long_prompt | model | op_parser,
})

result = chain.invoke({
    "short" : {"topic": "Deep Learning"},
    "detailed" : {"topic": "Generative AI"}
})

print(result["short"])
print(result["detailed"])