import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Jadarat_df = pd.read_csv("Data/Jadarat_data.csv")

# Title and description
st.title("Job Market Analysis Dashboard")
st.write("""
This dashboard presents an analysis of the job market based on the provided dataset. 
Explore various aspects such as job distributions, company information, regional analysis, and more.
""")
# Add a logo at the top
logo_path = "Images/11.jpeg"  # Replace with the correct path to your logo image
st.image(logo_path, width=400)

# Sidebar for user inputs
st.sidebar.header("Filters")
region_filter = st.sidebar.multiselect("Select Region", options=Jadarat_df["region"].unique(), default=Jadarat_df["region"].unique())
gender_filter = st.sidebar.multiselect("Select Gender", options=Jadarat_df["gender"].unique(), default=Jadarat_df["gender"].unique())

# Filter data based on user inputs
filtered_data = Jadarat_df[(Jadarat_df["region"].isin(region_filter)) & (Jadarat_df["gender"].isin(gender_filter))]

# Job title distribution
st.subheader("Job Title Distribution")
job_title_counts = filtered_data["job_title"].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(x=job_title_counts.values, y=job_title_counts.index, ax=ax)
ax.set_xlabel("Count")
ax.set_ylabel("Job Title")
st.pyplot(fig)

# Company type distribution
st.subheader("Company Type Distribution")
company_type_counts = filtered_data["comp_type"].value_counts()
fig, ax = plt.subplots()
sns.barplot(x=company_type_counts.values, y=company_type_counts.index, ax=ax)
ax.set_xlabel("Count")
ax.set_ylabel("Company Type")
st.pyplot(fig)

# Regional distribution
st.subheader("Regional Distribution")
region_counts = filtered_data["region"].value_counts()
fig, ax = plt.subplots()
sns.barplot(x=region_counts.values, y=region_counts.index, ax=ax)
ax.set_xlabel("Count")
ax.set_ylabel("Region")
st.pyplot(fig)

# Experience requirement distribution
st.subheader("Experience Requirement Distribution")
exper_counts = filtered_data["exper"].value_counts()
fig, ax = plt.subplots()
sns.barplot(x=exper_counts.values, y=exper_counts.index, ax=ax)
ax.set_xlabel("Count")
ax.set_ylabel("Experience Requirement")
st.pyplot(fig)

# Conclusion
st.write("""
### Conclusion
The data analysis provides insights into the job market. Further analysis can include more detailed visualizations 
and interactive components to dive deeper into the trends and patterns.
""")

# Run the Streamlit app with the command: streamlit run dashboard.py