import streamlit as st
import pandas as pd


import streamlit as st

# Using object notation
nav_list = ["Total Earnings", "Locations", "Check the Data"]
link = "https://raw.githubusercontent.com/chriszapp/datasets/main/supermarket_sales%20-%20Sheet1.csv"
supermarket = pd.read_csv(link, header = 0)

with st.sidebar: 
    selection = st.radio(
        "Select the KPI",
        nav_list)

if selection == nav_list[0]:
    st.title("Total Earnings")


if selection == nav_list[1]:
    st.title('We Are Here!')
    name = st.text_input("Please give me your name:")
    name_length = len(name)
    st.write("Your name has ",name_length, "characters")


if selection == nav_list[2]:
    # How to display data
    st.write(supermarket)




