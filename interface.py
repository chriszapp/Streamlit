import streamlit as st
import pandas as pd
import streamlit_player as sp

st.title("Hello Cristina, I'm so proud of you!")

name = st.text_input("Please give me your name:")
name_length = len(name)
st.write("Your name has ",name_length, "characters")

# How to display data
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)
st.write(df_weather)

# How to display graphics
st.line_chart(df_weather['MAX_TEMPERATURE_C'])

# Embed a youtube video
sp.st_player("https://www.youtube.com/watch?v=9sg-A-eS6Ig")

