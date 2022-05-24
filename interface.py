import streamlit as st
import pandas as pd
import numpy as np


import streamlit as st

# Using object notation
nav_list = ["Total Earnings", "Locations", "Check the Data"]
link = "https://raw.githubusercontent.com/chriszapp/datasets/main/supermarket_sales%20-%20Sheet1.csv"
supermarket = pd.read_csv(link, header = 0)
pivot = pd.pivot_table(supermarket, index = 'Date', values = 'Total', aggfunc = np.sum)#.sort_values('Date', inplace = True)

with st.sidebar: 
    selection = st.radio(
        "Select the KPI",
        nav_list)

if selection == nav_list[0]:
    st.title("Total Earnings")
    # st.write(pivot)#[pivot['Branch'] == 'A'])
    st.line_chart(data=pivot, use_container_width=True)


if selection == nav_list[1]:
    st.title('We Are Here!')
    name_branch = st.text_input("Please select the branch (A, B, or C):")
    if name_branch:
        st.write("The branch ", name_branch, " is in ", supermarket[supermarket['Branch'] == name_branch]['City'].unique()[0])


if selection == nav_list[2]:
    # How to display data
    st.write(supermarket)

    # import yfinance as yf

    # data = yf.download('AAPL','2016-01-01','2019-08-01')

    # # get stock info
    # st.write(data)




