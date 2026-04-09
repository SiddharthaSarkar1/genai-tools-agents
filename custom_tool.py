from langchain.tools import tool

@tool # decorator to create a tool 
def get_greeting(name: str) -> str :
    """ Generate a greeting message for a user """ # This is a doc string describes what the tool does

    return f"Hello {name}, welcome to AI world."

result = get_greeting.invoke({"name": "Siddhartha"})

print(result)

print(get_greeting.name)
print(get_greeting.description)
print(get_greeting.args)