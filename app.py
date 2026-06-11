from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

def my_output(query) : 
    response = model.generate_content(query)
    return response.text

# To check inside vs code

# input = str(input("Enter your query: "))
# response = my_output(input)
# print(response)

# UI development using streamlit

st.set_page_config(page_title="I/O MVP")
st.header("I/O MVP")
input = st.text_input("Input ", key='input')
submit = st.button("Ask your Query: ")

if submit: 
    response = my_output(input)
    # st.subheader("Check the output below: ")
    st.write(response)