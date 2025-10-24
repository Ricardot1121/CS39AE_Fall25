import os
import pandas as pd
import streamlit as st
import plotly.express as px

# Page title
st.title("Interactive Pie Chart - Business Sectors")

# Build an absolute path to the CSV file
csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "test.csv"))

# Show the path being used (for debugging)
st.caption(f"Reading CSV from: {csv_path}")

# Check if file exists before loading
if not os.path.exists(csv_path):
    st.error("CSV file not found! Please ensure 'test.csv' is inside the 'data' folder.")
    st.stop()

# Try reading the CSV file
try:
    df = pd.read_csv(csv_path)
except Exception as e:
    st.error(f"Error reading CSV: {e}")
    st.stop()

# Display the data
st.subheader("📊 Data Preview")
st.dataframe(df)

# Validate required columns
if "Category" not in df.columns or "Value" not in df.columns:
    st.error("CSV must contain 'Category' and 'Value' columns.")
    st.stop()

# Create interactive pie chart
fig = px.pie(
    df,
    names='Category',
    values='Value',
    title='Distribution of Business Sectors',
    color_discrete_sequence=px.colors.qualitative.Pastel
)

# Show chart
st.subheader("🧁 Interactive Pie Chart")
st.plotly_chart(fig, use_container_width=True)

# Instructions
st.write("""
💡 **Tip:**  
Modify the `data/test.csv` file or change the chart title above.  
Then **refresh the Streamlit page** — your updates will automatically appear!
""")

# Observation input
st.subheader("📝 Your Observations")
observation = st.text_area("I see that technology is very popular in the demo data. And that Entertainment is the least popular in my demo data, which is about business sectors. I used AI for 3_Pie Microsoft Copilot. (2025, October 24). Response to prompt: “Can you give me a work cited of Copilot?” Generated using https://copilot.microsoft.com/..")

if observation:
    st.success("Thanks for your input!")
    st.write("You wrote:")
    st.write(observation)
