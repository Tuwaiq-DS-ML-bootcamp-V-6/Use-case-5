import streamlit as st
import pandas as pd

# Load your dataset
df = pd.read_csv('Data/Jadarat_data.csv')

st.title('Job Postings Analysis in Saudi Arabia')
st.markdown("In the heart of Saudi Arabia lies Riyadh, a bustling hub of economic activity where job opportunities abound. Let's delve into the data to uncover insights and offer recommendations for both genders thriving in Riyadh's workforce.")

# Regional Distribution of Job Postings
st.subheader('Regional Distribution of Job Postings')
st.write("In Riyadh, job postings flourish, painting a vivid picture of the city's economic vitality. With Riyadh leading the charge, it's evident that the capital serves as a beacon, attracting businesses and job seekers alike. This concentration of opportunities underscores Riyadh's pivotal role as an economic and administrative powerhouse in the region.")
st.image(
            "https://imgur.com/WjnMnEW.jpg",
            width=400, # Manually Adjust the width of the image as per requirement
        )
st.markdown("""
### Insight:
Riyadh leads in job postings, indicating a strong job market in the capital. This could be due to its status as an economic and administrative hub, attracting businesses and job seekers alike. Other regions with high job postings include Dammam, reflecting their importance as commercial and industrial centers.
""")

# Gender Preference in Job Postings
st.subheader('Gender Preference in Job Postings')
st.write("In the realm of job postings, gender preferences occasionally surface, reflecting societal norms and industry traditions. While the majority of postings remain neutral in their gender specifications, there's a subtle undercurrent that warrants attention. Despite strides towards inclusivity, gender biases persist in certain sectors, influencing hiring practices and candidate preferences.")
st.image(
            "https://imgur.com/HYkJ4sM.jpg",
            width=400, # Manually Adjust the width of the image as per requirement
        )

st.markdown("""
### Insight:
The majority of job postings do not specify a gender preference, indicating a trend towards gender-neutral job opportunities. However, some postings still indicate a preference for male or female candidates, reflecting traditional gender roles in certain industries or job functions.
""")

st.markdown("""
### Recommendation:
1- Employers and policymakers should capitalize on Riyadh's thriving job market by investing in infrastructure, education, and talent development initiatives to further bolster economic prosperity.

2- Employers should adopt gender-neutral language in job postings and cultivate a culture of diversity and inclusion within their organizations to ensure equal opportunities for all individuals.""")
