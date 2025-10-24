import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("🥧 Interactive Pie Chart")

st.markdown(
    """
    **Goal:** Create an interactive pie chart from CSV data with customizable options.
    """
)

# Load data
@st.cache_data
def load_pie_data():
    """Load pie chart data from CSV file"""
    try:
        df = pd.read_csv("data/Pie_demo.csv")
        return df
    except FileNotFoundError:
        st.error("Could not find data/Pie_demo.csv file!")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

# Load the data
df = load_pie_data()

if not df.empty:
    st.write("**Data Preview:**")
    st.dataframe(df, use_container_width=True)
    
    # Interactive controls
    st.markdown("### Chart Customization")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Chart title input
        chart_title = st.text_input("Chart Title", value="Market Share Distribution")
        
        # Color scheme selection
        color_scheme = st.selectbox(
            "Color Scheme",
            options=["Set3", "Pastel1", "Dark2", "Set1", "Tab10"],
            index=0
        )
    
    with col2:
        # Show values toggle
        show_values = st.checkbox("Show Values on Chart", value=True)
        
        # Show percentages toggle
        show_percentages = st.checkbox("Show Percentages", value=True)
        
        # Chart size
        chart_height = st.slider("Chart Height", min_value=400, max_value=800, value=500)
    
    # Filter data based on minimum value
    min_value = st.slider("Minimum Value to Display", 
                         min_value=0, 
                         max_value=int(df['Value'].max()), 
                         value=0)
    
    # Filter the data
    filtered_df = df[df['Value'] >= min_value]
    
    if not filtered_df.empty:
        # Create the pie chart
        st.markdown(f"### {chart_title}")
        
        # Prepare text information for the pie chart
        textinfo = []
        if show_values:
            textinfo.append("value")
        if show_percentages:
            textinfo.append("percent")
        
        textinfo_str = "+".join(textinfo) if textinfo else "none"
        
        # Create pie chart using plotly express
        fig = px.pie(
            filtered_df, 
            values='Value', 
            names='Category',
            title=chart_title,
            color_discrete_sequence=px.colors.qualitative.__dict__[color_scheme],
            height=chart_height
        )
        
        # Update traces for better appearance
        fig.update_traces(
            textposition='inside', 
            textinfo=textinfo_str,
            hovertemplate="<b>%{label}</b><br>" +
                         "Value: %{value}<br>" +
                         "Percentage: %{percent}<br>" +
                         "<extra></extra>",
            textfont_size=12
        )
        
        # Update layout
        fig.update_layout(
            showlegend=True,
            legend=dict(
                orientation="v",
                yanchor="middle",
                y=0.5,
                xanchor="left",
                x=1.01
            ),
            margin=dict(l=20, r=100, t=70, b=20)
        )
        
        # Display the chart
        st.plotly_chart(fig, use_container_width=True)
        
        # Data summary
        with st.expander("📊 Data Summary"):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Total Categories", len(filtered_df))
            
            with col2:
                st.metric("Total Value", f"{filtered_df['Value'].sum():,}")
            
            with col3:
                st.metric("Largest Category", filtered_df.loc[filtered_df['Value'].idxmax(), 'Category'])
            
            # Detailed breakdown
            st.markdown("**Category Breakdown:**")
            summary_df = filtered_df.copy()
            summary_df['Percentage'] = (summary_df['Value'] / summary_df['Value'].sum() * 100).round(1)
            summary_df = summary_df.sort_values('Value', ascending=False)
            st.dataframe(summary_df, use_container_width=True, hide_index=True)
    
    else:
        st.warning("No data matches the current filter criteria. Try lowering the minimum value.")

else:
    st.info("Please ensure the data/Pie_demo.csv file exists and contains data.")

# Instructions for the user
st.divider()
st.markdown("### 📝 Instructions")
st.markdown(
    """
    **To test the dynamic updates:**
    1. **Modify the chart title** above and see it update instantly
    2. **Edit the CSV file** (`data/Pie_demo.csv`) by:
       - Changing values in the 'Value' column
       - Adding new categories
       - Removing existing rows
    3. **Refresh the page** (F5 or Ctrl+R) to see your CSV changes reflected
    4. **Use the interactive controls** to customize the visualization
    
    **Observations:** *[Write your 1-2 sentence observations here after testing]*
    
    """
)

st.caption("Edit `pages/3_Pie.py` and `data/Pie_demo.csv` to experiment with the visualization.")
