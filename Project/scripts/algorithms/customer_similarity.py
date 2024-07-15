import pandas as pd
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from SPARQLWrapper import SPARQLWrapper, JSON

# Define the SPARQL endpoint and query
SPARQL_ENDPOINT = 'http://localhost:7200/repositories/federation'
sparql_query = """
PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?buyer ?product
WHERE {
  ?cust_purch a global:CustomerPurchase .
  ?cust_purch global:productPurchased ?product .
  ?cust_purch global:buyer ?buyer .
  BIND(xsd:decimal(?buyer) AS ?customer)
  # FILTER(?customer=200 || ?customer=201 || ?customer=271 || ?customer=274 || ?customer=44)
}
"""

# Query the SPARQL endpoint
sparql = SPARQLWrapper(SPARQL_ENDPOINT)
sparql.setQuery(sparql_query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

# Convert the results to a DataFrame
data = []
for result in results["results"]["bindings"]:
    buyer_value = result['buyer']['value']
    if '.' in buyer_value:
        buyer_value = int(float(buyer_value))
    else:
        buyer_value = int(buyer_value)
    data.append({
        'customer_id': buyer_value,
        'product_id': result['product']['value']
    })

df = pd.DataFrame(data)

# Create a bipartite graph
B = nx.Graph()

# Add nodes with the bipartite attribute
customers = df['customer_id'].unique()
products = df['product_id'].unique()

B.add_nodes_from(customers, bipartite=0)
B.add_nodes_from(products, bipartite=1)

# Add edges between customers and products
edges = list(df.itertuples(index=False, name=None))
B.add_edges_from(edges)

# Project onto customers
G = nx.bipartite.weighted_projected_graph(B, customers)

# Calculate Jaccard similarity
jaccard_sim = nx.jaccard_coefficient(G)
jaccard_similarity = {(u, v): p for u, v, p in jaccard_sim}

# Create a matrix for cosine similarity calculation
adj_matrix = nx.adjacency_matrix(G)
cosine_sim_matrix = cosine_similarity(adj_matrix)

# Create a dictionary of cosine similarity
cosine_similarity_dict = {}
nodes = list(G.nodes())
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        cosine_similarity_dict[(nodes[i], nodes[j])] = round(cosine_sim_matrix[i, j], 2)

# Convert the similarity dictionaries to DataFrames for better visualization
cosine_df = pd.DataFrame(list(cosine_similarity_dict.items()), columns=['Pair', 'Cosine Similarity'])

# Plot the graph with cosine similarity as weights
G_weighted = nx.Graph()

# Add nodes
G_weighted.add_nodes_from(customers)

# Add edges with weights (cosine similarity)
for (u, v), weight in cosine_similarity_dict.items():
    G_weighted.add_edge(u, v, weight=weight)

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G_weighted)
edges = G_weighted.edges(data=True)
weights = [d['weight'] for (u, v, d) in edges]

nx.draw(G_weighted, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, font_color="black", font_weight="bold", edge_color=weights, edge_cmap=plt.cm.Blues, width=2)
edge_labels = nx.get_edge_attributes(G_weighted, 'weight')
edge_labels = {k: f'{v:.2f}' for k, v in edge_labels.items()}  # Round to two decimal places
nx.draw_networkx_edge_labels(G_weighted, pos, edge_labels=edge_labels)
plt.title("Customer Purchase Similarity Graph (Cosine Similarity)")
plt.show()
