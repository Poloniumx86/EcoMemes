import streamlit as st
import openai
from backend_to_be_added import selected_key

openai.api_key = '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'

messages=[
    {"role": "system", "content": "We will provide you an image name, we want you to provide us meme text about sustainability that is related to the image name we provide. Keep the meme text short and be very funny"},
  ]

def get_assistant_response(messages):
    r = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": m["role"], "content": m["content"]} for m in messages],
    )
    response = r.choices[0].message.content
    return response

messages.append({"role": "user", "content": selected_key})

# Get assistant response

if st.button("Generate Meme :sunglasses:"):
    response = get_assistant_response(messages)
    st.write(response)
    st.image(f'./images/{selected_key}', use_column_width=True)