import requests
from rdflib import Graph, Namespace, Literal, RDF, XSD
from datetime import datetime
import sys

# Temporarily increase the recursion limit 
sys.setrecursionlimit(2000)

GRAPHDB_BASE_URL = 'http://localhost:7200'

# Define namespaces
ex = Namespace("http://www.example.edu/spicy_bytes/")
meta = Namespace("http://www.example.edu/spicy_bytes/metadata#")

# Configuration template
config_ttl_template = """
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rep: <http://www.openrdf.org/config/repository#> .
@prefix sail: <http://www.openrdf.org/config/sail#> .
@prefix graphdb: <http://www.ontotext.com/config/graphdb#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<#{}> a rep:Repository;
  rep:repositoryID "{}";
  rep:repositoryImpl [
      rep:repositoryType "graphdb:SailRepository";
      <http://www.openrdf.org/config/repository/sail#sailImpl> [
          <http://www.ontotext.com/config/graphdb#base-URL> "http://www.example.edu/spicy_bytes/";
          <http://www.ontotext.com/config/graphdb#check-for-inconsistencies> "false";
          <http://www.ontotext.com/config/graphdb#defaultNS> "";
          <http://www.ontotext.com/config/graphdb#disable-sameAs> "true";
          <http://www.ontotext.com/config/graphdb#enable-context-index> "false";
          <http://www.ontotext.com/config/graphdb#enable-fts-index> "false";
          <http://www.ontotext.com/config/graphdb#enable-literal-index> "true";
          <http://www.ontotext.com/config/graphdb#enablePredicateList> "true";
          <http://www.ontotext.com/config/graphdb#entity-id-size> "32";
          <http://www.ontotext.com/config/graphdb#entity-index-size> "10000000";
          <http://www.ontotext.com/config/graphdb#fts-indexes> ("default" "iri");
          <http://www.ontotext.com/config/graphdb#fts-iris-index> "none";
          <http://www.ontotext.com/config/graphdb#fts-string-literals-index> "default";
          <http://www.ontotext.com/config/graphdb#imports> "";
          <http://www.ontotext.com/config/graphdb#in-memory-literal-properties> "true";
          <http://www.ontotext.com/config/graphdb#query-limit-results> "0";
          <http://www.ontotext.com/config/graphdb#query-timeout> "0";
          <http://www.ontotext.com/config/graphdb#read-only> "false";
          <http://www.ontotext.com/config/graphdb#repository-type> "file-repository";
          <http://www.ontotext.com/config/graphdb#ruleset> "rdfsplus-optimized";
          <http://www.ontotext.com/config/graphdb#storage-folder> "storage";
          <http://www.ontotext.com/config/graphdb#throw-QueryEvaluationException-on-timeout> "false";
          sail:sailType "graphdb:Sail"
      ]
    ];
  rdfs:label "" .
"""

# Function to delete an existing repository in GraphDB
def delete_repository(repo_id):
    url = f'{GRAPHDB_BASE_URL}/rest/repositories/{repo_id}'
    response = requests.delete(url)
    print(f"Delete repository response status: {response.status_code}")
    if response.status_code == 200:
        print(f"Repository '{repo_id}' deleted successfully.")
    else:
        print(f"Failed to delete repository '{repo_id}': {response.text}")

# Function to create a repository in GraphDB
def create_repository(repo_id):
    # Check if repository exists and delete if it does
    delete_repository(repo_id)
    
    # Save the configuration to a file
    config_ttl = config_ttl_template.format(repo_id, repo_id)
    config_file_path = f'{repo_id}_config.ttl'
    with open(config_file_path, 'w') as file:
        file.write(config_ttl)

    # Upload the configuration file to GraphDB
    url = f'{GRAPHDB_BASE_URL}/rest/repositories'
    files = {'config': open(config_file_path, 'rb')}
    response = requests.post(url, files=files)

    print(f"Create repository response status: {response.status_code}")
    print(f"Create repository response text: {response.text}")

    if response.status_code == 201:
        print(f"Repository '{repo_id}' created successfully.")
        create_metadata(repo_id, "Repository Creation", graph_uri=f'http://www.example.edu/spicy_bytes/{repo_id}')
    else:
        print(f"Failed to create repository '{repo_id}': {response.text}")

# Function to upload RDF data to a repository
def upload_data_to_repository(repo_id, data, graph_uri, create_metadata_entry=True):
    encoded_data = data.encode('utf-8')
    response = requests.post(
        f'{GRAPHDB_BASE_URL}/repositories/{repo_id}/statements',
        params={'context': f'<{graph_uri}>'},
        data=encoded_data,
        headers={'Content-Type': 'application/x-turtle'}
    )
    
    print(f"Upload data response status: {response.status_code}")
    print(f"Upload data response text: {response.text}")

    if response.status_code == 204:
        print(f"Data uploaded to repository '{repo_id}' successfully.")
        if create_metadata_entry:
            create_metadata(repo_id, "Repository Created and Data Uploaded", graph_uri)
    else:
        print(f"Failed to upload data to repository '{repo_id}': {response.text}")

# Function to create metadata instances for source tracking and audit trails
def create_metadata(repo_id, action, graph_uri):
    metadata_graph = Graph()
    metadata_graph.bind("meta", meta)
    timestamp = datetime.now().isoformat()
    source_instance = meta[repo_id]
    audit_instance = meta[f'audit_{repo_id}_{timestamp}']

    metadata_graph.add((source_instance, RDF.type, meta.Source))
    metadata_graph.add((source_instance, meta.sourceId, Literal(repo_id, datatype=XSD.string)))
    metadata_graph.add((source_instance, meta.sourceName, Literal(repo_id, datatype=XSD.string)))

    metadata_graph.add((audit_instance, RDF.type, meta.AuditTrail))
    metadata_graph.add((audit_instance, meta.timestamp, Literal(timestamp, datatype=XSD.dateTime)))
    metadata_graph.add((audit_instance, meta.action, Literal(action, datatype=XSD.string)))
    metadata_graph.add((audit_instance, meta.performedBy, Literal("Automated System", datatype=XSD.string)))

    metadata_graph.add((audit_instance, meta.relatedSource, source_instance))

    # Upload the metadata
    upload_data_to_repository('metadata', metadata_graph.serialize(format='turtle'), graph_uri, create_metadata_entry=False)

# Function to create and load TBox for local datasets
def create_and_load_local_datasets(repo_id, tbox_data, abox_data, graph_uri):
    # Create repository
    create_repository(repo_id)

    # Create TBox
    tbox_graph = Graph()
    tbox_graph.parse(data=tbox_data, format="ttl")

    # Create TBox
    abox_graph = Graph()
    abox_graph.parse(data=abox_data, format="ttl")

    # Upload TBox to repository
    upload_data_to_repository(repo_id, tbox_graph.serialize(format='turtle'), graph_uri)
    upload_data_to_repository(repo_id, abox_graph.serialize(format='turtle'), graph_uri)

# Create metadata repository first
create_repository('metadata')

# File paths for TBox data
tbox_files = {
    'business_inventory': './output/tbox/tbox_business_inventory.ttl',
    'customer': './output/tbox/tbox_customer.ttl',
    'customer_inventory': './output/tbox/tbox_customer_inventory.ttl',
    'customer_location': './output/tbox/tbox_customer_location.ttl',
    'location': './output/tbox/tbox_location.ttl',
    'supermarkets': './output/tbox/tbox_supermarket.ttl',
    'spicybytes_b2c': './output/tbox/tbox_spicybytes_b2c.ttl',
    'spicybytes_c2c': './output/tbox/tbox_spicybytes_c2c.ttl'
}

# File paths for Abox data
abox_files = {
    'business_inventory': './output/abox/abox_business_inventory.ttl',
    'customer': './output/abox/abox_customer.ttl',
    'customer_inventory': './output/abox/abox_customer_inventory.ttl',
    'customer_location': './output/abox/abox_customer_location.ttl',
    'location': './output/abox/abox_location.ttl',
    'supermarkets': './output/abox/abox_supermarket.ttl',
    'spicybytes_b2c': './output/abox/abox_spicybytes_b2c.ttl',
    'spicybytes_c2c': './output/abox/abox_spicybytes_c2c.ttl'
}


# Function to load data from files
def load_data_from_file(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as file:
        return file.read()
    

# Load local datasets
for repo_id in tbox_files:
    tbox_data = load_data_from_file(tbox_files[repo_id])
    abox_data = load_data_from_file(abox_files[repo_id])
    graph_uri = f'http://www.example.edu/spicy_bytes/'
    create_and_load_local_datasets(repo_id, tbox_data, abox_data, graph_uri)


