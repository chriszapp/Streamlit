import streamlit as st
import pandas as pd

st.title("Hello Cristina, I'm so proud of you!")

name = st.text_input("Please give me your name:")
name_length = len(name)
st.write("Your name has ",name_length, "characters")

# How to display data
link = "https://raw.githubusercontent.com/chriszapp/datasets/main/books.csv"
books = pd.read_csv(link)
st.write(books)

# How to display graphics
st.line_chart(books['ratings_count'])

