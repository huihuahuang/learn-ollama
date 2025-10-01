import ollama
import os

model = "llama3.2"
# Paths to input and output files
input_files = "./data/grocery_list.txt"
output_files = "./data/categorized_grocery_list.txt"

# Check if the input file exists
if not os.path.exists(input_files):
    print(f"Input file '{input_files}' not found.")
    exit(1)

# Read grocery items from input file
with open(input_files, "r") as f:
    items = f.read().strip()

# Prepare the prompt
prompt = f"""

You are an assistant that categorized and sorts grocery items.

Here is a list of grocery items:

{items}

Please:

1. Categorize these items into appropriate categories such as Produce, Dairy, 
Meat, Bakery, Beverage, etc.
2. Sort the items alphabetically within each category.
3. Present the categorized list in a clear and organized manner,using bullet points 
or numbering.
"""

# Send prompt and get the response
try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_text = response.get("response", "")

    with open(output_files, "w") as f:
        f.write(generated_text.strip())
    print(f"Categorized grocery list has been saved to '{output_files}'")
except Exception as e:
    print("An error occurred: ", str(e))