import streamlit as st
import pandas as pd 
# import matplotlib.pyplot as plt
import plotly.graph_objects as go


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

    #plotting
    fig.update_layout(
        xaxis_title='Years of Experience',
        yaxis_title='Salary Range',
        legend_title='Percentiles',

    )

    st.plotly_chart(fig)

##################################




#writing the actual streamlit app
st.write('Hello world!')

jadarat_df = pd.read_csv("Data\Jadarat_clean.csv")

sal_rang(jadarat_df)