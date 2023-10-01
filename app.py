import streamlit as st
import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)

# Streamlit app
st.title('Pandas DataFrame Example')
st.write('Here is a sample DataFrame:')
st.write(df)
