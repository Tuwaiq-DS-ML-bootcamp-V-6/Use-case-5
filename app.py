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
    
    # Create a scatter plot for Experience vs. Salary
    scatter_chart = px.scatter(df, x='exper', y='salary', title='Experience vs. Salary',
                               labels={'exper': 'Years of Experience', 'salary': 'Salary'})
    
    # Display the scatter plot
    st.plotly_chart(scatter_chart)
    
    st.write('The scatter plot above shows the relationship between years of experience and salary levels in Saudi Arabia. It can provide insights into how salary levels vary with experience across different job roles.')
    
    # Calculate average salary by region
    df_mean_salary_region = df.groupby('region')['salary'].mean().reset_index()

    # Create a bar chart for Average Salary by Region
    bar_chart = px.bar(df_mean_salary_region, x='region', y='salary', title='Average Salary by Region',
                       labels={'region': 'Region', 'salary': 'Average Salary'})

    # Display the bar chart
    st.plotly_chart(bar_chart)

    st.write('The bar chart above shows the average salary levels across different regions in Saudi Arabia, providing insights into regional disparities in salary levels.')
    
    # Add a sidebar section for filtering
    st.markdown("## Filter Job Opportunities:")
    
    # Job title filter
    selected_job_title = st.multiselect('Select Job Title', df['job_title'].unique())

    # Region filter
    selected_region = st.multiselect('Select Region', df['region'].unique())

    # Gender filter
    selected_gender = st.multiselect('Select Gender', df['gender'].unique())

    # Experience filter
    selected_experience = st.multiselect('Select Years of Experience', df['exper'].unique())

    # Filter the data based on user selections
    filtered_df = df[(df['region'].isin(selected_region)) & (df['job_title'].isin(selected_job_title)) & (df['gender'].isin(selected_gender)) & (df['exper'].isin(selected_experience))]

    # Display the filtered data
    st.subheader('Available Opportunities')
    st.write(filtered_df)


if __name__ == '__main__':
    main()
