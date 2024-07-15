from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import networkx as nx
from urllib.parse import unquote

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
}
"""

# Execute the SPARQL query
sparql = SPARQLWrapper(SPARQL_ENDPOINT)
sparql.setQuery(sparql_query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

# Extract the results into a DataFrame
data = []
for result in results['results']['bindings']:
    data.append({
        'customer_id': result['buyer']['value'],
        'product_id': unquote(result['product']['value'])  # Decode the product name
    })

df = pd.DataFrame(data)

# Remove duplicate entries if any
df.drop_duplicates(inplace=True)

# Create a bipartite graph
B = nx.Graph()

# Add nodes with the bipartite attribute
customers = set(df['customer_id'])
products = set(df['product_id'])

B.add_nodes_from(customers, bipartite=0)  # Add the customer nodes
B.add_nodes_from(products, bipartite=1)  # Add the product nodes

# Add edges between customers and products
for _, row in df.iterrows():
    B.add_edge(row['customer_id'], row['product_id'])

# Project the bipartite graph onto the product nodes
G = nx.bipartite.weighted_projected_graph(B, products)

# Compute PageRank
pagerank = nx.pagerank(G, weight='weight')

# Convert to DataFrame for better readability
pagerank_df = pd.DataFrame(pagerank.items(), columns=['Product', 'PageRank']).sort_values(by='PageRank', ascending=False)

# Format PageRank to 4 decimal places
pagerank_df['Product'] = pagerank_df['Product'].map(lambda x: x.title())

pagerank_df['PageRank'] = pagerank_df['PageRank'].map(lambda x: f'{x:.4f}')

# Print the DataFrame
print(pagerank_df)
