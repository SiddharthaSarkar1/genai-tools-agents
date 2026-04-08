from dotenv import load_dotenv
load_dotenv()


from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# 1. Prompt Template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)

# 2. Model
model = ChatMistralAI(model="mistral-small-2506")

# 3. Output Parser
parser = StrOutputParser()


##Step by step manual flow withour parser---------------------------

# # Format the prompt
# formatted_prompt = prompt.format_prompt(topic="Machine Learning")

# # Call the model manually
# response = model.invoke(formatted_prompt)

# # Parse the output manually
# final_output = parser.parse(response.content)

# print(final_output)

#-----------------------------------------------------

# Implemented with Chains
# This is not an authentic chain, just a way to show how we are connecting runnables

chain = prompt | model | parser

result = chain.invoke("Generative AI") # invoking runnables with invoke method

print(result)

