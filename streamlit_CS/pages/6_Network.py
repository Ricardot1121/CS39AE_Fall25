import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import time
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([("Alice", "Bob"), ("Alice", "Eve"), ("Bob", "Eve")])
 #Try with G = nx.karate_club_graph() for a big graph
pos = nx.spring_layout(G)  # Force-directed layout
nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='gray')
plt.show()
