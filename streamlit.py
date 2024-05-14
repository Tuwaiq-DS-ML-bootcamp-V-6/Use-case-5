
import pandas as pd
import streamlit as st
import plotly.express as px



# -- LOADING DATA
jdata = pd.read_csv('https://raw.githubusercontent.com/MohammedAlaklabi/Use-case-5/main/data/Jadarat_data.csv')


# -- LOGO
st.image('images/RIYADH.png') 

# -- TITLE
st.title(':blue[Riyadh] ( The City of Dreamers 🤩 )')
st.subheader("Riyadh holds promising opportunities for job seekers, making it an ideal destination to explore. Enjoy your visit to Riyadh, and we look forward to welcoming you to our community.")
# -- CHARTS

# Top 10 Cities
st.subheader('Here we highlighted the biggest regions for jobs')
city_counts = jdata['region'].value_counts().head(10)
fig_bar = px.bar(city_counts, x=city_counts.index, y=city_counts.values)
fig_bar.update_xaxes(title="Regions")
fig_bar.update_yaxes(title="Avg Jobs")
fig_bar.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig_bar)
st.markdown("Riyadh stands as the largest market to target, offering a plethora of opportunities worth exploring. Be sure to thoroughly explore all the possibilities that Riyadh has in store for you.")

st.divider()
# - Riyadh offers a diverse array of choices.
if "df" not in st.session_state:
    st.session_state.df = jdata

st.header("Riyadh offers a diverse array of choices.")
color = st.color_picker("Color", "#FF0000")
st.session_state.df["region"] = st.session_state.df["region"].astype(str)
st.scatter_chart(st.session_state.df, x="region", y="contract", color=color)
st.markdown("If you prefer the flexibility of working from home, Riyadh provides ample opportunities for you to make that adjustment. There are numerous options available to cater to your preferences.")

st.divider()
# Top 10 comp_size
st.subheader('Bigger Companies')
city_counts = jdata['comp_size'].value_counts().head(10)
fig_bar = px.bar(city_counts, x=city_counts.index, y=city_counts.values)
fig_bar.update_xaxes(title="Companies size")
fig_bar.update_yaxes(title="Avg Companies")
fig_bar.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig_bar)
st.markdown("Discover a multitude of company sizes and types that offer excellent opportunities, particularly in Riyadh since its the top 1 city in Saudi Arabia for Jobs opportunities, shaping a thriving job market.")

st.divider()
# Select top 25 data points
st.header('Experience vs. Number of Positions')
st.subheader("Even inexperienced youth can find opportunities in Riyadh.")
fig_scatter = px.scatter(jdata, x='exper', y='positions', color='region')
st.plotly_chart(fig_scatter)
st.markdown(" Uncover the perfect opportunity in Riyadh to initiate your career journey ! ")

st.divider()
st.title("Conclusion")
st.markdown("In my view, Riyadh presents a plethora of remarkable opportunities for individuals from diverse demographics, regardless of age, gender, or background, to embark on their career journeys. Whether you're a young professional seeking your first job or an experienced individual looking for new prospects, Riyadh's dynamic job market caters to all. The city's vibrant economy and progressive outlook ensure that there are ample avenues for growth and advancement. By considering Riyadh as a potential destination, you open yourself up to a world of possibilities, where talent and ambition are recognized and rewarded. I trust that this perspective aids you in making a well-informed decision about pursuing your career goals in Riyadh.")
