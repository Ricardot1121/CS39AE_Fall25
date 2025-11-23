import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import time
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([
    ("Alice", "Bob"),
    ("Alice", "Charlie"),
    ("Bob", "Charlie"),
    ("Charlie", "Diana"),
    ("Diana", "Eve"),
    ("Bob", "Diana"),
    ("Frank", "Eve"),
    ("Eve", "Ian"),
    ("Diana", "Ian"),
    ("Ian", "Grace"),
    ("Grace", "Hannah"),
    ("Hannah", "Jack"),
    ("Grace", "Jack"),
    ("Charlie", "Frank"),
    ("Alice", "Eve"),
    ("Bob", "Jack")
])

st.header("Network Graph")

# Advanced Network Metrics for Analysis
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G, max_iter=1000)

 #Try with G = nx.karate_club_graph() for a big graph
# Create a figure
fig, ax = plt.subplots(figsize=(10, 8))

# Try with G = nx.karate_club_graph() for a big graph
pos = nx.spring_layout(G)  # Force-directed layout
nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='gray', ax=ax)

# Display in Streamlit
st.pyplot(fig)
