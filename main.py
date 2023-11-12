import streamlit as st
import openai
from backend import *
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("API_KEY")

messages=[
    {"role": "system", "content": "We will provide you an image name, we want you to provide us meme text about sustainability that is related to the image name we provide. Keep the meme text short and be very funny. Don't mention the exact name of the image."},
  ]

def get_assistant_response(messages):
    r = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": m["role"], "content": m["content"]} for m in messages],
    )
    response = r.choices[0].message.content
    return response

# Get assistant response


if st.button("Generate Meme :sunglasses:"):
    currentImage = File_Name()
    messages.append({"role": "user", "content": currentImage})
    response = get_assistant_response(messages)
    st.write(response)
    st.image(f'./images/{currentImage}', use_column_width=True)