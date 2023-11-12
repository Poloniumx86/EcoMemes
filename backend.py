import openai

openai.api_key = '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'

# Initialize the chat messages history
messages = [{"role": "assistant", "content": "How can I help?"}]

# Function to display the chat history
def display_chat_history(messages):
    for message in messages:
        print(f"{message['role'].capitalize()}: {message['content']}")

# Function to get the assistant's response
def get_assistant_response(messages):
    r = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": m["role"], "content": m["content"]} for m in messages],
    )
    response = r.choices[0].message.content
    return response

# Main chat loop
while True:
    # Display chat history
    display_chat_history(messages)

    # Get user input
    prompt = input("User: ")
    messages.append({"role": "user", "content": prompt})

    # Get assistant response
    response = get_assistant_response(messages)
    messages.append({"role": "assistant", "content": response})