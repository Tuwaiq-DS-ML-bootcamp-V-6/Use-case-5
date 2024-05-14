import pandas as pd
import streamlit as st

job_data = pd.read_csv("https://raw.githubusercontent.com/GoldenHamad/Use-case-5/main/Data/Jadarat_data.csv")


st.title("Always Be Prepared")
st.image('https://raw.githubusercontent.com/GoldenHamad/Use-case-5/main/Images/Hire%20me.webp')
st.write("almost 90 percent of fresh graduates have an idea of which path they want to take, but not many know of the salary they should expect when they first come to the business environment")
st.write("with this statistic i hope to give fresh graduates an idea of the salary they should expect, and that they should probably try to bargain if they get a lower offer (if possible).")
st.image("blob:https://github.com/c9bcedc3-866d-47e8-b189-d3ae2ecb118c")
st.write("")
st.title("Conclusion")
st.write("In Conclusion, people should expect to get salaries in the range of 4k as fresh graduates, so should'nt be too greedy and expect a lot more and they should know what to answer when they're asked "'How much do salary do you expect to get from us".')
st.write('They should always be prepared!.')