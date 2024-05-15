import streamlit as st
import pandas as pd 
# import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import os


##################################################
#Drawing functions go here
def sal_rang(df):
    experiences = df['exper']
    salaries = df['salary']

    data = pd.DataFrame({'Experience': experiences, 'Salary': salaries})
    grouped_data = data.groupby('Experience')['Salary'].describe().reset_index()

    fig = go.Figure()

    #25% line
    fig.add_trace(go.Scatter(
        x=grouped_data['Experience'], y=grouped_data['25%'], 
        mode='lines+markers', 
        name='25%',
        line=dict(color='skyblue')
    ))
    #50% line
    fig.add_trace(go.Scatter(
        x=grouped_data['Experience'], y=grouped_data['50%'], 
        mode='lines+markers', 
        name='50%',
        line=dict(color='blue')
    ))
    #75% line
    fig.add_trace(go.Scatter(
        x=grouped_data['Experience'], y=grouped_data['75%'], 
        mode='lines+markers', 
        name='75%',
        line=dict(color='skyblue')
    ))

    #fill between 25% and 75%
    fig.add_trace(go.Scatter(
        x=grouped_data['Experience'], y=grouped_data['75%'],
        fill=None,
        mode='lines',
        line=dict(color='skyblue'),
        showlegend=False
    ))
    fig.add_trace(go.Scatter(
        x=grouped_data['Experience'], y=grouped_data['25%'],
        fill='tonexty', 
        mode='lines',
        line=dict(color='skyblue'),
        showlegend=False
    ))

    fig.update_layout(
        xaxis_title='Years of Experience',
        yaxis_title='Salary Range',
        legend_title='Percentiles',

    )

    st.plotly_chart(fig)

def job_gender(df):
    job_gender_counts = df.groupby(['job_title', 'gender']).size().reset_index(name='counts')


    job_gender_counts = job_gender_counts.sort_values(by='counts', ascending=False)


    fig = px.bar(job_gender_counts.head(80), x='job_title', y='counts', color='gender', barmode='group',
                labels={'counts': 'Number of People', 'job_title': 'Job Title'})
    
    st.plotly_chart(fig)



def best_region(df):
    region_counts = df['region'].value_counts().reset_index(name='counts')
    region_counts.columns = ['region', 'counts']

    fig = px.bar(region_counts, x='region', y='counts',
                labels={'counts': 'Number of Job Requests', 'region': 'Region'})
    
    st.plotly_chart(fig)
##################################




#writing the actual streamlit app
jadarat_df = pd.read_csv("https://raw.githubusercontent.com/Sulaiman-F-Alharbi/Use-case-5/main/Data/Jadarat_clean.csv")

st.title("Finding the best job opportunities in Saudi Arabia")

image_path = "Imgs/logo.jpg"
if os.path.exists(image_path):
    st.image(image_path)
else:
    st.error(f"Image file not found: {image_path}")

st.markdown("Many people find it difficult to find a job, especially if you new to the job business like newly graduated senior students where many of them face anxiety  and don't know what the current market need.")
st.markdown("Since it is a big issue I decided to gather some publicly available datasets that focus on Saudi Arabia's job market and see what is the shape of the current market, and learn together the trends and the needs of the market, to make it easier for people to decide what they choose, based on region, salary and gender.")



st.title("Where to work?")
st.markdown("Saudi Arabia is considered a big country especially if you compare it by it's neighbors, which means that you could find job opportunities all over the kingdom but that doesn't mean you will have the same chance in 2 different cities, and we can see that from the below graph:")
best_region(jadarat_df)
st.markdown("As we can see each Region has different number of job opportunities so lets talk about the main reasons why:")

st.subheader("Economical")
st.markdown("""
Regions that serve as economic and administrative hubs typically host the headquarters of major national and international companies,
financial institutions, and government bodies. This centralization of economic activities creates a plethora of job opportunities across various industries.
For example, Riyadh, the capital city, is an economic powerhouse with numerous corporate and government offices.
""")

st.subheader("Governmental and Vision 2030")
st.markdown("""
Government initiatives and development plans, such as Vision 2030 in Saudi Arabia, often focus on major regions to drive growth and diversification.
Investments in infrastructure, technology, and various sectors are concentrated in these areas to transform them into global cities.
For instance, initiatives like Green Riyadh, Riyadh Metro, and Qiddiyah in Riyadh, as well as similar projects in Makkah and the Eastern Province, significantly boost job creation.
""")

st.subheader("Tourism and Hospitality")
st.markdown("""
Regions with significant cultural, religious, or natural attractions often have a high demand for jobs in tourism and hospitality.
Makkah, as the holiest city in Islam, attracts millions of pilgrims annually, creating jobs in hospitality, transportation, and retail.
Similarly, the Eastern Province, with its coastline and industrial cities, also sees significant job growth in tourism and related sectors.
""")
st.markdown("")




st.title("What kind of salary can you anticipate?")
st.markdown("""One of the top reasons why would someone would search for a job is money,
             so knowing what would you expect for your salary depending on your experience would help you especially during job interviews.""")
sal_rang(jadarat_df)
st.markdown("As we can see from the above graph we have a salary range depending on the years of experience and the reason why the salary differ depending on your experience is as follows:")

st.markdown("**Early Career (0-2 Years)**")
st.markdown("""
- **Learning Curve:** New employees typically spend the initial years developing their skills and gaining practical experience.
- **Lower Starting Salaries:** Entry-level positions often come with lower salaries, reflecting the need for training and mentorship.
""")

st.markdown("**Mid Career (3-6 Years)**")
st.markdown("""
- **Skill Development:** Employees with 3-6 years of experience have developed significant skills and knowledge, making them more valuable to employers.
- **Increased Responsibilities:** Professionals in this range often take on more complex tasks and responsibilities, justifying higher salaries.
- **Market Demand:** This period often sees rapid salary growth as demand for skilled and experienced workers increases.
""")

st.markdown("**Senior Career (10+ Years)**")
st.markdown("""
- **Stabilization:** After around 10 years, salary growth tends to stabilize. Employees may have reached the upper limits of their career ladder.
- **Top Percentiles:** Those in the top percentiles often hold high-level executive or specialist positions, which are less common and have less variation in salary increases.
- **Demand vs. Supply:** There may be fewer new opportunities for significant raises unless employees change roles or companies.
""")




st.title("What are the top job opportunities for men and women?")
st.markdown("""Gender preferences in job opportunities can stem from a variety of factors.
             Historical roles and societal norms often shape perceptions about which jobs are suitable for men or women.
             Physical demands and risk factors may lead some jobs, especially those involving heavy labor or high risk, to prefer male candidates.
             Conversely, fields like nursing or education, traditionally seen as nurturing, might prefer female candidates.
             Additionally, educational backgrounds and personal interests, influenced by early socialization, play a role in these preferences.
             Understanding these factors helps explain why certain jobs may lean towards one gender over the other.""")
st.write("And we can see that from the following graph.")
job_gender(jadarat_df)




st.title("Conclusion")
st.markdown("""Navigating the job market in Saudi Arabia can be challenging, especially for new graduates. 
            By analyzing publicly available datasets, we can identify key trends and needs within the market to aid in making informed decisions about where to work.
             Regions like Riyadh, Makkah, and the Eastern Province offer diverse opportunities due to their economic significance, government initiatives, and cultural importance.""")
st.markdown("""Understanding salary expectations based on experience can also provide valuable insights for job seekers.
             Early career stages involve lower salaries due to training needs, 
            while mid and senior career stages see significant growth due to skill development and increased responsibilities.""")

st.markdown("""Additionally, recognizing gender preferences in job opportunities helps in understanding the distribution of roles across different sectors.
             Historical and societal factors play a role, with certain jobs favoring men or women based on physical demands, cultural norms, and educational backgrounds.""")

st.markdown("By considering these factors, job seekers can better navigate the job market in Saudi Arabia, aligning their career goals with the opportunities available in different regions and sectors.")