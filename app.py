import streamlit as st
from PIL import Image

# Title of the appjobs in saudi arabia
st.title('Jobs in Saudi Arabia')

# Path to your image
image_path = 'header.png'

# Load the image using PIL
image = Image.open(image_path)

# Method 1: Using HTML/CSS to resize
# st.markdown(
#     f"""
#     <style>
#     .image {{
#         width: 300px; /* Adjust the width as needed */
#     }}
#     </style>
#     <img src="{image_path}" class="image">
#     """,
#     unsafe_allow_html=True
# )

st.write("---")  # Separator

# Method 2: Using Python to resize
# Resize the image
new_width = 300  # Adjust the width as needed
new_height = int(new_width * image.height / image.width)  # Maintain aspect ratio
resized_image = image.resize((new_width, new_height))

# Display the resized image
st.image(resized_image, use_column_width=False)
st.markdown("Finding a job is pretty challenging, especially if you’re a fresh graduate. So, I started my journey to find a job and wanted to see which city has more job opportunities in Saudi Arabia. I want to communicate with my colleagues about the results of my search.")
st.image("regions.png")
st.write("---")
st.markdown("After I found the best city in terms of job opportunities which is Riyadh, I wanted to see the best city in terms of salary.")
st.image("salary.png")
st.markdown("I found out that Riyadh wasn’t the best in terms of average salary it was Al-Baha .")
st.write("---")
st.write("concluson ")
st.write("  •	The city with the most job opportunities is Riyadh.")
st.write("	•	Al-Baha is also the best city in terms of average salary.")
