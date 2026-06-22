import streamlit as st
import pandas as pd

st.title("Hello World!")
st.write("My first deployed Streamlit app.")

name = st.text_input("What is your name?")

if name:
    st.write(f"Welcome, {name}!")