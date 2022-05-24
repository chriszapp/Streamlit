# !pip install pandas
# !pip install streamlit
!pip install yfinance

import streamlit as st
import pandas as pd
import numpy as np

import yfinance as yf

st.title("Welcome to the financial App!")

selected_stock = st.text_input("Please select the stock:")

if selected_stock: 
    data = yf.download(selected_stock,'2021-01-01','2022-01-01')
    # st.write('This is the Data')
    st.write(data)

    selected_price = st.text_input("Please select the column:")
    if selected_price:
        st.line_chart(data=data[selected_price], use_container_width=True)


if selected_stock:
    multiple_choice = st.multiselect('Select countries:', options=data.columns, default=['Open', 'Close'])
    if len(multiple_choice) > 0 :
        st.line_chart(data[multiple_choice])






# with st.sidebar: 
#     selection = st.radio(
#         "Select the KPI",
#         nav_list)

# if selection == nav_list[0]:
#     st.title("Total Earnings")
#     # st.write(pivot)#[pivot['Branch'] == 'A'])
#     st.line_chart(data=pivot, use_container_width=True)


# if selection == nav_list[1]:
#     st.title('We Are Here!')
#     name_branch = st.text_input("Please select the branch (A, B, or C):")
#     if name_branch:
#         st.write("The branch ", name_branch, " is in ", supermarket[supermarket['Branch'] == name_branch]['City'].unique()[0])


# if selection == nav_list[2]:
#     # How to display data
#     st.write(supermarket)

#     # import yfinance as yf

#     # data = yf.download('AAPL','2016-01-01','2019-08-01')

#     # # get stock info
#     # st.write(data)




