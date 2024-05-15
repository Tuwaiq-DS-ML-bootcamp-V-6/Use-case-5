import streamlit as st
import pandas as pd 

st.write('Hello world!')

df = pd.read_csv("Data\Jadarat_data.csv")

st.dataframe(df)