from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

model = ChatMistralAI(model="mistral-small-2506")
op_parser = StrOutputParser()

code_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a code generator. You must answer only in code snippets, no text"),
    ("human", "{topic}")
])

explain_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that explains things in simple terms"),
    ("human", "Explain the following code in simple words:\n{code}")
])

seq1 = code_prompt | model | op_parser

seq2 = RunnableParallel({
    "code": RunnablePassthrough(),
    "explanation": explain_prompt | model | op_parser
})

chain = seq1 | seq2

result = chain.invoke({"topic": "Write code for a Armstrong number in python"})

print(result["code"])
print(result["explanation"])