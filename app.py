import streamlit as st
import pandas as pd
import plotly.express as px

# Load your dataset
df = pd.read_csv('Data/Jadarat_data.csv')

st.title('Job Postings Analysis in Saudi Arabia')
st.markdown("In the heart of Saudi Arabia lies Riyadh, a bustling hub of economic activity where job opportunities abound. Let's delve into the data to uncover insights and offer recommendations for both genders thriving in Riyadh's workforce.")

# Regional Distribution of Job Postings
st.subheader('Regional Distribution of Job Postings')
region_counts = df['region'].value_counts().reset_index()
region_counts.columns = ['Region', 'Job Postings']

fig1 = px.bar(region_counts, x='Region', y='Job Postings',
              title='Number of Job Postings by Region',
              labels={'Job Postings':'Number of Job Postings', 'Region':'Region'},
              template='plotly_white')
st.plotly_chart(fig1)

st.markdown("""
### Insight:
Riyadh leads in job postings, indicating a strong job market in the capital. This could be due to its status as an economic and administrative hub, attracting businesses and job seekers alike. Other regions with high job postings include Jeddah and Dammam, reflecting their importance as commercial and industrial centers.
""")

# Gender Preference in Job Postings
st.subheader('Gender Preference in Job Postings')
gender_counts = df['gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Job Postings']

fig2 = px.pie(gender_counts, values='Job Postings', names='Gender',
              title='Gender Preference in Job Postings',
              template='plotly_white',
              hole=0.3)
st.plotly_chart(fig2)

st.markdown("""
### Insight:
The majority of job postings do not specify a gender preference, indicating a trend towards gender-neutral job opportunities. However, some postings still indicate a preference for male or female candidates, reflecting traditional gender roles in certain industries or job functions.
""")
