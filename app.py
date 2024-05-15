import streamlit as st
import pandas as pd
import plotly.graph_objects as go




st.image("mqdefault.jpg", width=250)

df = pd.read_csv('Data/Jadarat_data.csv')

st.title('Trend Postings in Saudi Arabia')

st.title('Introduction')
st.markdown('Welcome to our recommendation board! Today, we’ll showcase top related jobs in the region.')


st.title('Use case scenario')
st.markdown('The top image illustrates the differences in opportunities across various regions and the diversity of opportunities. It appears that Riyadh has the highest demand for a variety of jobs.')

st.title('Streamlit Storytelling')
st.markdown('We’ve created a user-friendly interface using Streamlit. Users can input their preferences: make, maximum price, maximum mileage, and minimum year. Our system then searches through the data store to find matching cars')

selected_region = st.selectbox('Select a region:', df['Region'].unique())


s = ""

if selected_region == 'Riyadh':
    s = "Riyadh, the capital city, is known for its bustling urban environment and long commutes. The top 10 used cars in Riyadh tend to be fuel-efficient and comfortable for city driving. based on the graph above these car dominate the list due to their reliability and low maintenance costs. Given Riyadh’s vast urban landscape and heavy traffic, fuel efficiency and durability are crucial factors for car owners."
elif selected_region == 'Jeddah':
    s = "Jeddah, a major commercial hub, has a more diverse car market. The city’s coastal environment means that cars with good air conditioning and resistance to humidity are preferred. The economic activity in Jeddah also influences the popularity of models that offer a blend of comfort and practicality for both personal and business use."
elif selected_region == 'Dammam':
    s = "Dammam, known for its oil industry, sees a preference for robust and sturdy vehicles. These models on the graph above are popular due to their powerful performance and ability to handle rougher terrains, which are common in the region’s industrial areas."
elif selected_region == 'Hail':
    s = "Hail’s terrain is more mountainous and rugged, which is reflected in the popularity of SUVs and off-road vehicles. The top cars here are favored for their off-road capabilities, durability, and spaciousness, making them ideal for navigating the challenging landscape."
elif selected_region == 'Abha':
    s = 'Abha, known for its cooler climate and picturesque scenery, sees a mix of fuel-efficient and versatile vehicles. These models are appreciated for their ability to handle both city driving and occasional trips to the surrounding hilly areas.'
else:
    s= "Esraa is the best"

# Filter dataframe based on the selected region
region_df = df[df['Region'] == selected_region]


# Group by car name and count occurrences
top_cars = region_df.groupby('Type').size().reset_index(name='count')

top_cars = top_cars.sort_values(by='count', ascending=False)


st.title('Popular cars in your region')
st.bar_chart(
   top_cars.head(10), x="Type", y='count', color="#FF0000" # Optional
)
st.markdown('Take a look at the graph above showing the top 10 cars in your region. You might be wondering why this matters when choosing a used car. Opting for one of the most popular cars in your area ensures that local mechanics are well-versed in handling it, which can save you time and trouble with repairs. Additionally, selecting a popular model in the used market makes it easier to find spare parts, reducing maintenance costs and hassle.')

st.markdown(f"**FUN FACT:**  {s}")


chart_data = pd.concat([
    clean['Year'],
    clean['Price'],
], axis=1)
chart_data = chart_data.sort_values(['Year'])

chart_data_mean = chart_data.groupby(['Year'], dropna=True)[['Price']].mean()
chart_data_mean.columns = ['Pricemean']
chart_data = chart_data_mean.reset_index()
chart_data = chart_data.dropna()

chart_data = chart_data.sort_values(by='Pricemean', ascending=False)

st.title('Most expensive car models')
st.bar_chart(
   chart_data.head(10), x="Year", y='Pricemean', color="#FF0000" # Optional
)
st.markdown("Take a look at the graph above highlighting the significance of choosing the right model year for your budget. It's not about picking the newest model; it's about finding the best price based on the average cost per year. Here's how the years break down:")
text = """
- **Like New (up to 3 years old):** Practically new with modern features and reliability.
- **Okay Condition (up to 5 years old):**  Good condition with slightly lower prices.
- **Considered Old (5+ years):** May vary in condition but can be a great budget-friendly option.
"""

st.markdown(text)

def main(df):
    st.title('Mean Mileage by Gear Type')
    

    # Sample data (replace this with your actual data loading)


    # Data preprocessing
    df = df.reset_index().drop('index', axis=1, errors='ignore')
    df.columns = [str(c) for c in df.columns]  # Update columns to strings in case they are numbers

    chart_data = pd.concat([df['Gear_Type'], df['Mileage']], axis=1)
    chart_data = chart_data.sort_values(['Gear_Type'])
    chart_data_mean = chart_data.groupby(['Gear_Type'], dropna=True)[['Mileage']].mean()
    chart_data_mean.columns = ['Mileage Mean']
    chart_data = chart_data_mean.reset_index()
    chart_data = chart_data.dropna()

    # Create Plotly bar chart
    fig = go.Figure(data=[go.Bar(
        x=chart_data['Gear_Type'],
        y=chart_data['Mileage Mean'],
        marker=dict(color="#FF0000")
    )])

    fig.update_layout(
        barmode='group',
        legend={'orientation': 'h', 'y': -0.3},

        xaxis={'title': {'text': 'Gear Type'}},
        yaxis={'title': {'text': 'Mean of Mileage'}, 'type': 'linear'}
        
    )

    # Display the Plotly figure in Streamlit
    st.plotly_chart(fig)
    st.markdown("Take a look at the graph above showing the differences in mileage between manual and automatic gears. Manual gears offer better mileage and lower repair costs, making them smart purchases in the used car market. Ideal for enthusiasts and rugged terrains like Hail, they provide more value and efficiency. Automatic gears, while pricier to maintain, offer unmatched comfort and convenience, perfect for navigating the busy streets of Riyadh and Jeddah. Choose wisely and enjoy a better driving experience with the right gear type!")


main(df)

st.title("Conclusion")
st.markdown("In our analysis, we've identified key factors to help you choose the perfect used car in Saudi Arabia. These factors include popularity, usage needs, and budget considerations.")

st.markdown("""
- **Popularity:** Opting for one of the top 10 cars in your region ensures local mechanics can handle it, saving you time and trouble with repairs. Plus, it’s easier to find spare parts, reducing maintenance costs.
- **Usage:** Manual gears offer better mileage and lower repair costs, ideal for rugged terrains like Hail. Automatic gears, though pricier to maintain, provide unmatched comfort for busy cities like Riyadh and Jeddah. Choose the right gear type for your needs.
- **Budget:**
    - Like New (up to 3 years): Modern features and reliability.
    - Okay Condition (up to 5 years): Slightly lower prices.
    - Considered Old (5+ years): Budget-friendly with varying conditions.
""")

st.markdown("Choose wisely to get the most value for your money!")





