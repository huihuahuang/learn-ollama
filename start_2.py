import ollama

# Check what will be returned from ollama
response = ollama.list()

#  Chat Example
# https://github.com/ollama/ollama-python
res1 = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "Why is the sky blue?"}
    ]
)

print(res1["message"]["content"])

# Chat Example with streaming
res2 = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "Why is the ocean so salty?"}
    ],
    stream=True,
)

# Use for loop to iterate the response
for line in res2:
    print(line["message"]["content"], end="", flush=True)

# Create a new model with modelfile
# file = """
# FROM llama3.2

# SYSTEM "You are a very smart assistant who knows everything about the ocean. Be succinct and informative."

# PARAMETER temperature 0.1
# """


# ollama.create(model="knowitall", modelfile=file)

# res3 = ollama.generate(model="knowitall", prompt="why is the ocean salty?")

# Delete model
# ollama.delete("knowitall")