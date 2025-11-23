import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import time
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import community

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


betweenness_centrality = nx.betweenness_centrality(G)
most_popular = max(betweenness_centrality, key=betweenness_centrality.get)


communities = list(community.greedy_modularity_communities(G))

community_colors = ["red", "yellow", "green"]

node_color_map = {}

for i, com in enumerate(communities):
    for node in com:
        node_color_map[node] = community_colors[i % len(community_colors)]

node_color_map[most_popular] = "orange"

fig, ax = plt.subplots(figsize=(10, 8))

# Try with G = nx.karate_club_graph() for a big graph
pos = nx.spring_layout(G)  # Force-directed layout
node_colors = [node_color_map[node] for node in G.nodes()]
nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='gray', ax=ax)
# Display in Streamlit
st.pyplot(fig)
