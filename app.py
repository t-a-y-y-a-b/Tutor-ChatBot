import streamlit as st
import os
from groq import Groq

# Set up the Groq API client
client = Groq(api_key=(" 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"))

# Title of the app
st.title("Groq + LLaMA 3.2-90B Vision Preview")

# Text input for the user to type a message
user_input = st.text_area("Enter your text here:")

# Displaying the response from the model after button click
if st.button("Generate Response"):
    if user_input.strip():
        try:
            # Request a response from the model
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "user", "content": user_input}
                ],
                model="llama-3.2-90b-vision-preview",
            )
            
            # Display the response
            st.write("Generated Response:")
            st.write(chat_completion.choices[0].message.content)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text.")
