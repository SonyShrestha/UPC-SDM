import networkx as nx
from SPARQLWrapper import SPARQLWrapper, JSON
import matplotlib.pyplot as plt
import community as community_louvain  # Ensure this is installed

# Function to fetch data from the SPARQL endpoint
def fetch_graph_data(query, endpoint):
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

# SPARQL endpoint and query
SPARQL_ENDPOINT = 'http://localhost:7200/repositories/federation'
sparql_query = """
PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?buyer ?product
WHERE {
  ?cust_purch a global:CustomerPurchase .
  ?cust_purch global:productPurchased ?product .
  ?cust_purch global:buyer ?buyer .
  # FILTER(?product = 'amul%20plain%20processed%20cheese%20slices%20%20%28100%20g%29' || ?product='epigamia%20belgian%20chocolate%20milkshake'|| ?buyer='107.0' )
}
"""

# Fetch data from the SPARQL endpoint
results = fetch_graph_data(sparql_query, SPARQL_ENDPOINT)

# Initialize a NetworkX graph
G = nx.Graph()

# Track unique products to differentiate them in the graph
unique_products = set()

# Add nodes and edges to the graph
for result in results["results"]["bindings"]:
    buyer = int(float(result["buyer"]["value"]))
    product = result["product"]["value"]
    unique_products.add(product)

    G.add_node(buyer, type='buyer', label=buyer)
    G.add_node(product, type='product', label=product)
    G.add_edge(buyer, product)

# Project bipartite graph to buyer nodes
buyers = {n for n, d in G.nodes(data=True) if d['type'] == 'buyer'}
G_projected = nx.bipartite.weighted_projected_graph(G, buyers)

# Apply community detection
partition = community_louvain.best_partition(G_projected)

# Assign community information to nodes
for node, comm_id in partition.items():
    G_projected.nodes[node]['community'] = comm_id

# Visualization
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G_projected)  # Node positions

# Color nodes based on their community
community_colors = [partition[node] for node in G_projected.nodes]
nx.draw_networkx_nodes(G_projected, pos, node_color=community_colors, node_size=500, cmap=plt.cm.jet)

nx.draw_networkx_edges(G_projected, pos, alpha=0.5)
nx.draw_networkx_labels(G_projected, pos, labels={node: node for node in G_projected.nodes}, font_size=12)

plt.legend()
plt.axis('off')
plt.show()
