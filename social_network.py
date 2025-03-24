import networkx as nx
import matplotlib.pyplot as plt

# Create a social network graph
G = nx.Graph()

# List of Indian names for users
users = ["Amit", "Priya", "Rahul", "Sneha", "Vikram", "Meera", "Raj", "Pooja", "Arjun", "Neha"]

# Define friendships (edges between nodes)
friendships = [
    ("Amit", "Rahul"), ("Amit", "Priya"), ("Rahul", "Sneha"),
    ("Sneha", "Vikram"), ("Vikram", "Meera"), ("Raj", "Pooja"),
    ("Arjun", "Neha"), ("Rahul", "Vikram"), ("Meera", "Amit"),
    ("Pooja", "Arjun"), ("Neha", "Priya"), ("Rahul", "Raj")
]

# Add users and friendships to the graph
G.add_nodes_from(users)
G.add_edges_from(friendships)

# Visualize the social network graph
plt.figure(figsize=(8,6))
nx.draw(G, with_labels=True, node_color="skyblue", node_size=2500, font_size=12, edge_color="gray")
plt.title("Social Network Graph")
plt.show()
