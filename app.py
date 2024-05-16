import streamlit as st
import pandas as pd
#data = pd.read_csv('C:\\Users\\ryyao\\Desktop\\Use-case-5\\Data\\Jadarat_data.csv')
#data = data.loc[:, ~data.columns.duplicated()]
st.title('Opportunities for Young Saudis')
st.write("""
In the dynamic job market of Saudi Arabia, young people are finding increasing opportunities to start their careers without prior experience. The "Distribution of Experience Requirements" chart reveals that over half of the job postings are for positions requiring zero years of experience. This indicates that companies are actively seeking fresh graduates and young job seekers, offering them a platform to begin their professional journeys.
""")
st.title('Distribution of Experience Requirements')
st.image("Screenshot 2024-05-16 063929.png")
st.write("""
This trend highlights the supportive work environment in Saudi Arabia, where employers are willing to invest in young talent. Many companies provide training programs and mentorship opportunities to help new employees develop their skills and gain confidence. Such initiatives are crucial in helping young professionals feel valued and empowered as they transition into the workforce.
""")
st.write("""
The Kingdom's Vision 2030 initiative also plays a significant role in creating these opportunities. By focusing on diversifying the economy and generating jobs across various sectors, the initiative aims to include young Saudis in the workforce and reduce unemployment rates. This concerted effort is paving the way for a new generation of professionals to contribute to Saudi Arabia's growth and development.
""")
