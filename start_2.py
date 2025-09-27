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

