import streamlit as st
import pandas as pd

st.title("Hello Cristina, I'm so proud of you!")

name = st.text_input("Please give me your name:")
name_length = len(name)
st.write("Your name has ",name_length, "characters")

# How to display data
link = "https://raw.githubusercontent.com/chriszapp/datasets/main/supermarket_sales%20-%20Sheet1.csv"
supermarket = pd.read_csv(link, header = 0)
st.write(supermarket)

# How to display graphics
st.line_chart(supermarket['Quantity'])

