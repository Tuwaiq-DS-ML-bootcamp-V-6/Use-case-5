import streamlit as st


st.text("Welcome to My Streamlit website. Hope you like it!")

# Markdown text
st.markdown("""
    ## Topic: Jadarat

    <span style='color:black; font-weight:bold;'>
    Jadarat.sa is a platform dedicated to fostering growth, development, 
    and empowerment. their mission is to equip individuals, organizations, 
    and communities with the skills, knowledge, and resources needed to thrive in today's dynamic world.
    </span>


""", unsafe_allow_html=True)

st.markdown("\n \n")
st.markdown("\n \n")


st.markdown("""
            <span style='color:black; font-weight:bold;'>
            Understanding regional job posting proportions in Saudi Arabia helps job seekers target their search efforts more effectively, 
            increasing their chances of finding relevant opportunities in areas with higher demand for their skills, 
            thus saving time and effort.</span>
            """, unsafe_allow_html=True )

st.markdown("""
    <span style='color:black; font-weight:bold;'> Q1)  What proportion of job postings is attributed to each region within the kingdom?</span>
""", unsafe_allow_html=True)

st.markdown("\n \n")

# Display an image from a local file
st.image('image-1.png', caption='image-1.png', use_column_width=True)

