import streamlit as st
import openai
from backend import *
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("API_KEY")

#style
st.markdown(
        f"""
        <style>
            body {{
                background-image: url('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Fpremium-photo%2Fpurple-grid-background_37222602.htm&psig=AOvVaw28xGz5OYq3jDIk_3gwMxeA&ust=1699879412304000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCNjKgLa-voIDFQAAAAAdAAAAABAE');
                background-size: cover;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

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