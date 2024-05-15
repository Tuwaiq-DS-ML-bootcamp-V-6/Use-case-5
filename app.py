import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title('Employment Insights in Saudi Arabia')
    
    # Load the data
    df = pd.read_csv('Data/Jadarat_cleaned_data.csv') 

    # Display the raw data
    st.subheader('Data Sample')
    st.write(df)
    
    
    bar_chart = px.bar(df, x='job_title', title='Job Titles Distribution')
    bar_chart.show()

    
    
    

    
    
      

 
if __name__ == '__main__':
    main()
