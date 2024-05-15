import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title('Employment Opportunities in Saudi Arabia')
    
    st.markdown("# Introduction :")
    st.write("Welcome to the Employment opportunities data story, where we explore the landscape of job opportunities in Saudi Arabia. This analysis delves into a dataset containing information about various job titles, companies, qualifications, salaries, and more. By examining this data, we aim to uncover valuable insights into the employment market in Saudi Arabia.")
    
    # Load the data
    df = pd.read_csv('Data/Jadarat_cleaned_data.csv')

    # Calculate the top 10 job titles
    top_10_job_titles = df['job_title'].value_counts().nlargest(10).index.tolist()

    # Filter the DataFrame to include only the top 10 job titles
    df_top_10 = df[df['job_title'].isin(top_10_job_titles)]

    # Aggregate the data to get the sum of counts for each job title
    df_agg = df_top_10.groupby('job_title').size().reset_index(name='count')

    # Sort the aggregated data by count
    df_agg_sorted = df_agg.sort_values('count', ascending=False)

    # Display the raw data
    st.subheader('Data Sample')
    st.write(df)
    
    # Create a bar chart
    bar_chart = px.bar(df_agg_sorted, x='job_title', y='count', title='Top 10 Job Titles Distribution',
                       category_orders={'job_title': df_agg_sorted['job_title']})

    # Display the bar chart using st.plotly_chart
    st.plotly_chart(bar_chart)
    
    st.write('The bar chart above shows the distribution of the top 10 job titles in Saudi Arabia. It is evident that some job titles are more common than others such as "بائع" and "محاسب", providing insights into the most sought-after roles in the job market.')
    
    
    # Aggregate the data to get the mean salary for each years of experience
    df_mean_salary = df_top_10.groupby('exper')['salary'].mean().reset_index()

    # Sort the data by years of experience
    df_mean_salary_sorted = df_mean_salary.sort_values('exper')

    # Create a line plot for Experience vs. Salary
    line_chart = px.line(df_mean_salary_sorted, x='exper', y='salary', title='Experience vs. Average Salary',
                         labels={'exper': 'Years of Experience', 'salary': 'Average Salary'})
    
    # Display the line plot
    st.plotly_chart(line_chart)
    
    st.write('The line plot above shows the relationship between years of experience and average salary levels in Saudi Arabia. It provides insights into how average salary levels change with increasing experience across different job roles.')

if __name__ == '__main__':
    main()
