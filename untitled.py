import streamlit as st
import pandas as pd

st.title('Our dataset:')

df = pd.read_csv("Data/Jadarat_data.csv")

st.dataframe(df)