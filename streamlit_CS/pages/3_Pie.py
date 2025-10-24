import os
import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Interactive Pie Chart - Business Sectors")

# Build a safe, absolute path
csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "pie_demo.csv")

# Load CSV data
df = pd.read_csv(csv_path)

# Display the data
st.dataframe(df)

# Create interactive pie chart
fig = px.pie(df, names='Category', values='Value',
             title='Distribution of Business Sectors',
             color_discrete_sequence=px.colors.qualitative.Pastel)

# Show chart
st.plotly_chart(fig, use_container_width=True)

st.write("""
You can modify the **data/pie_demo.csv** file or change the chart title above.
When you **refresh the Streamlit page**, the chart will automatically update to reflect the new data or title.
""")
