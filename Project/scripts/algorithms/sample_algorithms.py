# import networkx as nx
# from SPARQLWrapper import SPARQLWrapper, JSON

# # SPARQL endpoint and query to fetch data
# SPARQL_ENDPOINT = 'http://localhost:7200/repositories/federation'
# sparql_query = """
# PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
# SELECT ?s ?p ?o
# WHERE {
#   ?s ?p ?o .
# }
# """

# # Function to fetch data from SPARQL endpoint
# def fetch_graph_data(query):
#     sparql = SPARQLWrapper(SPARQL_ENDPOINT)
#     sparql.setQuery(query)
#     sparql.setReturnFormat(JSON)
#     results = sparql.query().convert()
#     return results

# # Fetch data and build NetworkX graph
# results = fetch_graph_data(sparql_query)
# G = nx.Graph()

# for result in results["results"]["bindings"]:
#     s = result["s"]["value"]
#     p = result["p"]["value"]
#     o = result["o"]["value"]
#     G.add_edge(s, o, predicate=p)

# # Example: Compute centrality measures
# pagerank = nx.pagerank(G)
# betweenness = nx.betweenness_centrality(G)

# print("PageRank:", pagerank)
# print("Betweenness Centrality:", betweenness)


# import networkx as nx
# from SPARQLWrapper import SPARQLWrapper, JSON

# # SPARQL endpoint and query to fetch data
# SPARQL_ENDPOINT = 'http://localhost:7200/repositories/federation'
# sparql_query = """
# PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
# SELECT ?s ?p ?o
# WHERE {
#   ?s ?p ?o .
# }
# """

# # Function to fetch data from SPARQL endpoint
# def fetch_graph_data(query):
#     sparql = SPARQLWrapper(SPARQL_ENDPOINT)
#     sparql.setQuery(query)
#     sparql.setReturnFormat(JSON)
#     results = sparql.query().convert()
#     return results

# # Fetch data and build NetworkX graph
# results = fetch_graph_data(sparql_query)
# G = nx.Graph()

# for result in results["results"]["bindings"]:
#     s = result["s"]["value"]
#     p = result["p"]["value"]
#     o = result["o"]["value"]
#     G.add_edge(s, o, predicate=p)

# # Print first few nodes to identify source and target nodes
# print("First few nodes in the graph:")
# nodes = list(G.nodes)
# for i, node in enumerate(nodes[:10]):  # Print first 10 nodes
#     print(f"{i + 1}: {node}")

# # Example nodes for pathfinding (update these based on printed nodes)
# source_node = nodes[0]
# target_node = nodes[1]

# # Pathfinding Algorithms

# def find_shortest_path(graph, source, target):
#     return nx.dijkstra_path(graph, source, target)

# # Centrality Algorithms

# def calculate_pagerank(graph):
#     return nx.pagerank(graph)

# def calculate_betweenness_centrality(graph):
#     return nx.betweenness_centrality(graph)

# def calculate_closeness_centrality(graph):
#     return nx.closeness_centrality(graph)

# # Community Detection Algorithms

# def detect_communities_louvain(graph):
#     from community import community_louvain
#     return community_louvain.best_partition(graph)

# def detect_communities_label_propagation(graph):
#     return nx.algorithms.community.label_propagation.label_propagation_communities(graph)

# # Similarity Algorithms

# def calculate_cosine_similarity(graph, node1, node2):
#     from sklearn.metrics.pairwise import cosine_similarity
#     vec1 = nx.adjacency_matrix(graph, nodelist=[node1])
#     vec2 = nx.adjacency_matrix(graph, nodelist=[node2])
#     return cosine_similarity(vec1, vec2)

# def calculate_jaccard_similarity(graph, node1, node2):
#     return nx.jaccard_coefficient(graph, [(node1, node2)])

# # Subgraph Matching Algorithms

# def find_subgraph_isomorphism(graph, subgraph):
#     from networkx.algorithms import isomorphism
#     return isomorphism.GraphMatcher(graph, subgraph).subgraph_is_isomorphic()

# # Traversal Algorithms

# def depth_first_search(graph, source):
#     return list(nx.dfs_edges(graph, source))

# def breadth_first_search(graph, source):
#     return list(nx.bfs_edges(graph, source))

# # Link Prediction Algorithms

# def predict_links_adamic_adar(graph):
#     return list(nx.adamic_adar_index(graph))

# def predict_links_common_neighbors(graph):
#     return list(nx.common_neighbors(graph))

# # Example usage

# # Shortest path
# print("Shortest Path (Dijkstra):", find_shortest_path(G, source_node, target_node))

# # Centrality measures
# print("PageRank:", calculate_pagerank(G))
# print("Betweenness Centrality:", calculate_betweenness_centrality(G))
# print("Closeness Centrality:", calculate_closeness_centrality(G))

# # Community detection
# print("Communities (Louvain):", detect_communities_louvain(G))
# print("Communities (Label Propagation):", list(detect_communities_label_propagation(G)))

# # Similarity measures
# print("Cosine Similarity:", calculate_cosine_similarity(G, source_node, target_node))
# print("Jaccard Similarity:", list(calculate_jaccard_similarity(G, source_node, target_node)))

# # Traversal
# print("Depth First Search:", depth_first_search(G, source_node))
# print("Breadth First Search:", breadth_first_search(G, source_node))

# # Link prediction
# print("Adamic/Adar Index:", predict_links_adamic_adar(G))
# print("Common Neighbors:", predict_links_common_neighbors(G))


# import networkx as nx
# from SPARQLWrapper import SPARQLWrapper, JSON
# import pandas as pd

# # SPARQL endpoint and query to fetch data
# SPARQL_ENDPOINT = 'http://localhost:7200/repositories/federation'
# sparql_query = """
# PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
# SELECT ?s ?p ?o
# WHERE {
#   ?s ?p ?o .
# }
# """

# # Function to fetch data from SPARQL endpoint
# def fetch_graph_data(query):
#     sparql = SPARQLWrapper(SPARQL_ENDPOINT)
#     sparql.setQuery(query)
#     sparql.setReturnFormat(JSON)
#     results = sparql.query().convert()
#     return results

# # Fetch data and build NetworkX graph
# results = fetch_graph_data(sparql_query)
# G = nx.Graph()

# for result in results["results"]["bindings"]:
#     s = result["s"]["value"]
#     p = result["p"]["value"]
#     o = result["o"]["value"]
#     G.add_edge(s, o, predicate=p)

# # Print first few nodes to identify source and target nodes
# print("First few nodes in the graph:")
# nodes = list(G.nodes)
# for i, node in enumerate(nodes[:10]):  # Print first 10 nodes
#     print(f"{i + 1}: {node}")

# # Example nodes for pathfinding (update these based on printed nodes)
# source_node = nodes[0]
# target_node = nodes[1]

# # print(source_node)
# # print(target_node)

# # Pathfinding Algorithms

# def find_shortest_path(graph, source, target):
#     return nx.dijkstra_path(graph, source, target)

# # Centrality Algorithms

# def calculate_pagerank(graph):
#     return nx.pagerank(graph)

# def calculate_betweenness_centrality(graph):
#     return nx.betweenness_centrality(graph)

# def calculate_closeness_centrality(graph):
#     return nx.closeness_centrality(graph)

# # Community Detection Algorithms

# def detect_communities_louvain(graph):
#     from community import community_louvain
#     return community_louvain.best_partition(graph)

# def detect_communities_label_propagation(graph):
#     return nx.algorithms.community.label_propagation.label_propagation_communities(graph)

# # Similarity Algorithms

# def calculate_cosine_similarity(graph, node1, node2):
#     from sklearn.metrics.pairwise import cosine_similarity
#     vec1 = nx.adjacency_matrix(graph, nodelist=[node1])
#     vec2 = nx.adjacency_matrix(graph, nodelist=[node2])
#     return cosine_similarity(vec1, vec2)

# def calculate_jaccard_similarity(graph, node1, node2):
#     return nx.jaccard_coefficient(graph, [(node1, node2)])

# # Subgraph Matching Algorithms

# def find_subgraph_isomorphism(graph, subgraph):
#     from networkx.algorithms import isomorphism
#     return isomorphism.GraphMatcher(graph, subgraph).subgraph_is_isomorphic()

# # Traversal Algorithms

# def depth_first_search(graph, source):
#     return list(nx.dfs_edges(graph, source))

# def breadth_first_search(graph, source):
#     return list(nx.bfs_edges(graph, source))

# # Link Prediction Algorithms

# def predict_links_adamic_adar(graph):
#     return list(nx.adamic_adar_index(graph))

# def predict_links_common_neighbors(graph):
#     return list(nx.common_neighbors(graph))

# # Example usage and saving results

# def save_results_to_files(results, algorithm_name):
#     df = pd.DataFrame(results)
#     df.to_csv(f'{algorithm_name}_results.csv', index=False)
#     df.to_json(f'{algorithm_name}_results.json', orient='records', lines=True)
#     print(f"Results for {algorithm_name} saved to {algorithm_name}_results.csv and {algorithm_name}_results.json")
#     return df

# # Shortest path
# shortest_path = find_shortest_path(G, source_node, target_node)
# print("Shortest Path (Dijkstra):", shortest_path)
# save_results_to_files({'Shortest Path': [shortest_path]}, 'shortest_path')

# # Centrality measures
# pagerank = calculate_pagerank(G)
# betweenness_centrality = calculate_betweenness_centrality(G)
# closeness_centrality = calculate_closeness_centrality(G)

# print("PageRank:", pagerank)
# save_results_to_files(pagerank, 'pagerank')

# print("Betweenness Centrality:", betweenness_centrality)
# save_results_to_files(betweenness_centrality, 'betweenness_centrality')

# print("Closeness Centrality:", closeness_centrality)
# save_results_to_files(closeness_centrality, 'closeness_centrality')

# # Community detection
# louvain_communities = detect_communities_louvain(G)
# label_propagation_communities = list(detect_communities_label_propagation(G))

# print("Communities (Louvain):", louvain_communities)
# save_results_to_files(louvain_communities, 'louvain_communities')

# print("Communities (Label Propagation):", label_propagation_communities)
# save_results_to_files(label_propagation_communities, 'label_propagation_communities')

# # Similarity measures
# cosine_similarity = calculate_cosine_similarity(G, source_node, target_node)
# jaccard_similarity = list(calculate_jaccard_similarity(G, source_node, target_node))

# print("Cosine Similarity:", cosine_similarity)
# save_results_to_files(cosine_similarity, 'cosine_similarity')

# print("Jaccard Similarity:", jaccard_similarity)
# save_results_to_files(jaccard_similarity, 'jaccard_similarity')

# # Traversal
# dfs_edges = depth_first_search(G, source_node)
# bfs_edges = breadth_first_search(G, source_node)

# print("Depth First Search:", dfs_edges)
# save_results_to_files(dfs_edges, 'dfs_edges')

# print("Breadth First Search:", bfs_edges)
# save_results_to_files(bfs_edges, 'bfs_edges')

# # Link prediction
# adamic_adar_index = predict_links_adamic_adar(G)
# common_neighbors = predict_links_common_neighbors(G)

# print("Adamic/Adar Index:", adamic_adar_index)
# save_results_to_files(adamic_adar_index, 'adamic_adar_index')

# print("Common Neighbors:", common_neighbors)
# save_results_to_files(common_neighbors, 'common_neighbors')

# print("Results saved to respective CSV and JSON files")



import networkx as nx
from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# SPARQL endpoint and query to fetch data
SPARQL_ENDPOINT = 'http://localhost:7200/repositories/federation'
sparql_query = """
PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
SELECT ?s ?unitPrice ?quantityRemaining ?dateExpiry ?date
WHERE {
  ?s a global:SupermarketInventory ;
     global:unitPrice ?unitPrice ;
     global:quantityRemaining ?quantityRemaining ;
     global:dateExpiry ?dateExpiry ;
     global:date ?date .
}
"""

# Function to fetch data from SPARQL endpoint
def fetch_graph_data(query):
    sparql = SPARQLWrapper(SPARQL_ENDPOINT)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

# Fetch data and build NetworkX graph
results = fetch_graph_data(sparql_query)
G = nx.Graph()

for result in results["results"]["bindings"]:
    s = result["s"]["value"]
    unitPrice = result["unitPrice"]["value"]
    quantityRemaining = result["quantityRemaining"]["value"]
    dateExpiry = result["dateExpiry"]["value"]
    date = result["date"]["value"]

    # Add edges to the graph with attributes
    G.add_node(s, unitPrice=float(unitPrice), quantityRemaining=int(quantityRemaining), dateExpiry=dateExpiry, date=date)

# Print first few nodes to identify source and target nodes
print("First few nodes in the graph:")
nodes = list(G.nodes)
for i, node in enumerate(nodes[:10]):  # Print first 10 nodes
    print(f"{i + 1}: {node}, attributes: {G.nodes[node]}")

# Example nodes for pathfinding (update these based on printed nodes)
source_node = nodes[0]
target_node = nodes[1]

# Function to get node attributes as vectors
def get_node_attributes_as_vectors(graph, attribute):
    node_list = list(graph.nodes)
    attr_matrix = []

    for node in node_list:
        attr_values = [0] * len(node_list)
        if attribute in graph.nodes[node]:
            attr_values[node_list.index(node)] = graph.nodes[node][attribute]
        attr_matrix.append(attr_values)
    
    return np.array(attr_matrix), node_list

# Calculate cosine similarity
def calculate_cosine_similarity(graph, attribute):
    attr_matrix, node_list = get_node_attributes_as_vectors(graph, attribute)
    cosine_sim = cosine_similarity(attr_matrix)
    return cosine_sim, node_list

# Save results to files
def save_results_to_files(results, algorithm_name, node_list=None):
    if node_list:
        df = pd.DataFrame(results, index=node_list, columns=node_list)
    else:
        df = pd.DataFrame(results)
    df.to_csv(f'{algorithm_name}_results.csv', index=False)
    df.to_json(f'{algorithm_name}_results.json', orient='records', lines=True)
    print(f"Results for {algorithm_name} saved to {algorithm_name}_results.csv and {algorithm_name}_results.json")
    return df

# Pathfinding Algorithms

def find_shortest_path(graph, source, target):
    return nx.dijkstra_path(graph, source, target)

# Centrality Algorithms

def calculate_pagerank(graph):
    return nx.pagerank(graph)

def calculate_betweenness_centrality(graph):
    return nx.betweenness_centrality(graph)

def calculate_closeness_centrality(graph):
    return nx.closeness_centrality(graph)

# Community Detection Algorithms

def detect_communities_louvain(graph):
    from community import community_louvain
    return community_louvain.best_partition(graph)

def detect_communities_label_propagation(graph):
    return nx.algorithms.community.label_propagation.label_propagation_communities(graph)

# Similarity Algorithms

def calculate_jaccard_similarity(graph, node1, node2):
    return nx.jaccard_coefficient(graph, [(node1, node2)])

# Subgraph Matching Algorithms

def find_subgraph_isomorphism(graph, subgraph):
    from networkx.algorithms import isomorphism
    return isomorphism.GraphMatcher(graph, subgraph).subgraph_is_isomorphic()

# Traversal Algorithms

def depth_first_search(graph, source):
    return list(nx.dfs_edges(graph, source))

def breadth_first_search(graph, source):
    return list(nx.bfs_edges(graph, source))

# Link Prediction Algorithms

def predict_links_adamic_adar(graph):
    return list(nx.adamic_adar_index(graph))

def predict_links_common_neighbors(graph):
    return list(nx.common_neighbors(graph))

# Example usage and saving results

# Shortest path
# shortest_path = find_shortest_path(G, source_node, target_node)
# print("Shortest Path (Dijkstra):", shortest_path)
# save_results_to_files({'Shortest Path': [shortest_path]}, 'shortest_path')

# Centrality measures
pagerank = calculate_pagerank(G)
betweenness_centrality = calculate_betweenness_centrality(G)
closeness_centrality = calculate_closeness_centrality(G)

print("PageRank:", pagerank)
save_results_to_files(pagerank, 'pagerank')

print("Betweenness Centrality:", betweenness_centrality)
save_results_to_files(betweenness_centrality, 'betweenness_centrality')

print("Closeness Centrality:", closeness_centrality)
save_results_to_files(closeness_centrality, 'closeness_centrality')

# Community detection
louvain_communities = detect_communities_louvain(G)
label_propagation_communities = list(detect_communities_label_propagation(G))

print("Communities (Louvain):", louvain_communities)
save_results_to_files(louvain_communities, 'louvain_communities')

print("Communities (Label Propagation):", label_propagation_communities)
save_results_to_files(label_propagation_communities, 'label_propagation_communities')

# Similarity measures
cosine_sim, node_list = calculate_cosine_similarity(G, 'unitPrice')
print("Cosine Similarity:", cosine_sim)
save_results_to_files(cosine_sim, 'cosine_similarity', node_list)

jaccard_similarity = list(calculate_jaccard_similarity(G, source_node, target_node))
print("Jaccard Similarity:", jaccard_similarity)
save_results_to_files(jaccard_similarity, 'jaccard_similarity')

# Traversal
dfs_edges = depth_first_search(G, source_node)
bfs_edges = breadth_first_search(G, source_node)

print("Depth First Search:", dfs_edges)
save_results_to_files(dfs_edges, 'dfs_edges')

print("Breadth First Search:", bfs_edges)
save_results_to_files(bfs_edges, 'bfs_edges')

# Link prediction
adamic_adar_index = predict_links_adamic_adar(G)
common_neighbors = predict_links_common_neighbors(G)

print("Adamic/Adar Index:", adamic_adar_index)
save_results_to_files(adamic_adar_index, 'adamic_adar_index')

print("Common Neighbors:", common_neighbors)
save_results_to_files(common_neighbors, 'common_neighbors')

print("Results saved to respective CSV and JSON files")
