import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample DataFrame
data = {
    'x': np.random.rand(100),
    'y': np.random.rand(100)
}
df = pd.DataFrame(data)

# Streamlit app
st.title('Data Visualization with Pandas, NumPy, Matplotlib, and Seaborn')

# Display the DataFrame
st.write('Sample DataFrame:')
st.write(df)

# Scatter plot using Matplotlib
st.write('### Scatter Plot using Matplotlib')
plt.scatter(df['x'], df['y'])
st.pyplot()

# Histogram using Matplotlib
st.write('### Histogram using Matplotlib')
plt.hist(df['x'], bins=20)
st.pyplot()

# Heatmap using Seaborn
st.write('### Heatmap using Seaborn')
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True)
st.pyplot()
