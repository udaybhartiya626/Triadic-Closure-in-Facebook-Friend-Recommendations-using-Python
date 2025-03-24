import streamlit as st
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

# Function to find mutual friends
def mutual_friends(user):
    """Find mutual friends for a given user."""
    if user not in G.nodes:
        return []
    friends = set(G.neighbors(user))
    recommendations = {}

    for friend in friends:
        for potential_friend in G.neighbors(friend):
            if potential_friend != user and potential_friend not in friends:
                recommendations[potential_friend] = recommendations.get(potential_friend, 0) + 1

    return sorted(recommendations.items(), key=lambda x: x[1], reverse=True)

# Streamlit UI
st.set_page_config(page_title="Friend Recommendation System", layout="wide")

# Sidebar
st.sidebar.title("🔍 Friend Recommendation System")
st.sidebar.markdown("Select a user to get friend recommendations based on mutual friends.")

# Select a user
user = st.sidebar.selectbox("Choose a User", users)

# Main Title
st.title("🤝 Friend Recommendation System")
st.write("This system recommends friends using **Triadic Closure** (Mutual Friends) and Social Network Analysis.")

# Show recommendations
if st.sidebar.button("Get Recommendations"):
    recommendations = mutual_friends(user)

    # Display results
    st.subheader(f"🔹 Friend Recommendations for {user}")
    
    if recommendations:
        for friend, count in recommendations:
            st.write(f"👉 **{friend}** ({count} mutual connections)")
    else:
        st.write("❌ No new recommendations found.")

# Visualizing the Social Network Graph
st.subheader("🌍 Social Network Graph")

# Function to draw the graph
def draw_graph():
    plt.figure(figsize=(8,6))
    pos = nx.spring_layout(G)  # Layout for positioning nodes
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2500, font_size=12, edge_color="gray")
    plt.title("Social Network Visualization")
    st.pyplot(plt)

# Display the graph
draw_graph()
