import streamlit as st
import pandas as pd

def main():
    st.title('Hello World')
    
    # Load the data
    data = pd.read_csv('Data/Jadarat_cleaned_data.csv') 

    # Display the raw data
    st.subheader('Raw Data')
    st.write(data)
    
    
    
      

 
if __name__ == '__main__':
    main()
