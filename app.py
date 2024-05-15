import streamlit as st
from PIL import Image 

st.title('Jobs in Saudi Arabia')

image = Image.open('header.png')

st.image(image, caption='')

st.write("In the vibrant and ever-growing economy of Saudi Arabia, job postings serve as a gateway to exciting employment opportunities. With its rich cultural heritage, rapid modernization, and diverse sectors, Saudi Arabia offers a wide range of job prospects for both local residents and expatriates alike.")

st.write("From bustling metropolises like Riyadh, Jeddah, and Dammam to emerging business hubs, Job seekers can explore positions at various levels, from entry-level roles to executive positions, catering to different skill sets and qualifications.")

image = Image.open('regions.jpg')

st.image(image, caption='')

st.write("When considering job opportunities in Saudi Arabia, salary is a key factor that job seekers are interested in. Salaries in Saudi Arabia vary based on several factors, including level of experience, qualifications, job type, and the sector the company belongs to.")

image = Image.open('Salary.jpg')

st.image(image, caption='')


