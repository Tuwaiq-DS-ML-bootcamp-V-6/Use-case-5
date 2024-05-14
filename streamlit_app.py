import streamlit as st


st.text("Hello, this is a simple text.")

# Markdown text
st.markdown("""
    ## Welcome to my Streamlit app!

    This is a **bold** text.

    - Here's a bullet point.
    - And another one.

    [Link to Streamlit](https://streamlit.io/)
""")

import streamlit as st



# Display an image from a local file
st.image('image-1.png', caption='image-1.png', use_column_width=True)

