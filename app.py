import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title('Employment Insights in Saudi Arabia')
    
    # Load the data
    df = pd.read_csv('Data/Jadarat_cleaned_data.csv') 

    # Calculate the top 10 job titles
    top_10_job_titles = df['job_title'].value_counts().nlargest(10).index.tolist()

    # Filter the DataFrame to include only the top 10 job titles
    df_top_10 = df[df['job_title'].isin(top_10_job_titles)]

    # Display the raw data
    st.subheader('Data Sample')
    st.write(df_top_10)
    
    # Create a bar chart
    bar_chart = px.bar(df_top_10, x='job_title', title='Top 10 Job Titles Distribution')

    # Display the bar chart using st.plotly_chart
    st.plotly_chart(bar_chart)

if __name__ == '__main__':
    main()
