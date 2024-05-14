#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install plotly


# In[ ]:


import streamlit as st
import pandas as pd
import plotly.graph_objs as go

# Load your dataset
df = pd.read_csv('Data/Jadarat_data.csv')

st.title('Job Postings Analysis in Saudi Arabia')
st.markdown("In the heart of Saudi Arabia lies Riyadh, a bustling hub of economic activity where job opportunities abound. Let's delve into the data to uncover insights and offer recommendations for both genders thriving in Riyadh's workforce.")

# Regional Distribution of Job Postings
st.subheader('Regional Distribution of Job Postings')
st.write("In Riyadh, job postings flourish, painting a vivid picture of the city's economic vitality. With Riyadh leading the charge, it's evident that the capital serves as a beacon, attracting businesses and job seekers alike. This concentration of opportunities underscores Riyadh's pivotal role as an economic and administrative powerhouse in the region.")
# st.image(
#             "https://imgur.com/WjnMnEW.jpg",
#             width=400, # Manually Adjust the width of the image as per requirement
#         )
s = df[~pd.isnull(df['region'])]['region']
chart = pd.value_counts(s).to_frame(name='data')
chart['percent'] = (chart['data'] / chart['data'].sum()) * 100
chart.index.name = 'labels'
chart = chart.reset_index().sort_values(['data', 'labels'], ascending=[False, True])
chart = chart[:100]
charts = [go.Bar(x=chart['labels'].values, y=chart['data'].values, name='Frequency')]
figure = go.Figure(data=charts, layout=go.Layout({
    'barmode': 'group',
    'legend': {'orientation': 'h'},
    'title': {'text': 'region Value Counts'},
    'xaxis': {'title': {'text': 'region'}},
    'yaxis': {'title': {'text': 'Frequency'}}
}))

# Display the graph using Plotly in Streamlit
st.plotly_chart(figure)

st.markdown("""
### Insight:
Riyadh leads in job postings, indicating a strong job market in the capital. This could be due to its status as an economic and administrative hub, attracting businesses and job seekers alike. Other regions with high job postings include Dammam, reflecting their importance as commercial and industrial centers.
""")

# Gender Preference in Job Postings
st.subheader('Gender Preference in Job Postings')
st.write("In the realm of job postings, gender preferences occasionally surface, reflecting societal norms and industry traditions. While the majority of postings remain neutral in their gender specifications, there's a subtle undercurrent that warrants attention. Despite strides towards inclusivity, gender biases persist in certain sectors, influencing hiring practices and candidate preferences.")
# st.image(
#             "https://imgur.com/HYkJ4sM.jpg",
#             width=400, # Manually Adjust the width of the image as per requirement
#         )
s = df[~pd.isnull(df['gender'])]['gender']
chart = pd.value_counts(s).to_frame(name='data')
chart['percent'] = (chart['data'] / chart['data'].sum()) * 100
chart.index.name = 'labels'
chart = chart.reset_index().sort_values(['data', 'labels'], ascending=[False, True])
chart = chart[:100]
charts = [go.Bar(x=chart['labels'].values, y=chart['data'].values, name='Frequency')]
figure = go.Figure(data=charts, layout=go.Layout({
    'barmode': 'group',
    'legend': {'orientation': 'h'},
    'title': {'text': 'gender Value Counts'},
    'xaxis': {'title': {'text': 'gender'}},
    'yaxis': {'title': {'text': 'Frequency'}}
}))

# Display the graph using Plotly in Streamlit
st.plotly_chart(figure)

st.markdown("""
### Insight:
The majority of job postings do not specify a gender preference, indicating a trend towards gender-neutral job opportunities. However, some postings still indicate a preference for male or female candidates, reflecting traditional gender roles in certain industries or job functions.
""")

st.markdown("""
### Recommendation:
1- Employers and policymakers should capitalize on Riyadh's thriving job market by investing in infrastructure, education, and talent development initiatives to further bolster economic prosperity.

2- Employers should adopt gender-neutral language in job postings and cultivate a culture of diversity and inclusion within their organizations to ensure equal opportunities for all individuals.""")

