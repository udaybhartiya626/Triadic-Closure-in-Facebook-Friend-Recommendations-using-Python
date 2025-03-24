import networkx as nx

# Function to find mutual friends
def mutual_friends(user, graph):
    """Finds mutual friends for a given user."""
    friends = set(graph.neighbors(user))
    recommendations = {}

    for friend in friends:
        for potential_friend in graph.neighbors(friend):
            if potential_friend != user and potential_friend not in friends:
                recommendations[potential_friend] = recommendations.get(potential_friend, 0) + 1

    # Sort recommendations by number of mutual friends
    return sorted(recommendations.items(), key=lambda x: x[1], reverse=True)

# Load social network graph
G = nx.Graph()
G.add_edges_from([
    ("Amit", "Rahul"), ("Amit", "Priya"), ("Rahul", "Sneha"),
    ("Sneha", "Vikram"), ("Vikram", "Meera"), ("Raj", "Pooja"),
    ("Arjun", "Neha"), ("Rahul", "Vikram"), ("Meera", "Amit"),
    ("Pooja", "Arjun"), ("Neha", "Priya"), ("Rahul", "Raj")
])

# Example usage
print("Friend Recommendations for Rahul:", mutual_friends("Rahul", G))
