import requests
from rdflib import Graph, Namespace, Literal, RDF, XSD
from datetime import datetime

GRAPHDB_BASE_URL = 'http://localhost:7200'

# Define namespaces
ex = Namespace("http://www.example.edu/spicy_bytes/")
meta = Namespace("http://www.example.edu/spicy_bytes/metadata#")

# Configuration template for the repository
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

# Function to delete a repository in GraphDB
def delete_repository(repo_id):
    url = f'{GRAPHDB_BASE_URL}/rest/repositories/{repo_id}'
    response = requests.delete(url)
    if response.status_code == 200:
        print(f"Repository '{repo_id}' deleted successfully.")
        return True
    else:
        print(f"Failed to delete repository '{repo_id}': {response.text}")
        return False

# Function to check if a repository already exists
def check_repository_exists(repo_id):
    url = f'{GRAPHDB_BASE_URL}/rest/repositories/{repo_id}'
    response = requests.get(url)
    return response.status_code == 200

# Function to create a repository in GraphDB
def create_repository(repo_id):
    if check_repository_exists(repo_id):
        print(f"Repository '{repo_id}' already exists. Deleting existing repository...")
        if not delete_repository(repo_id):
            return  # Stop if the deletion fails
        
    # Save the configuration to a file
    config_ttl = config_ttl_template.format(repo_id, repo_id)
    config_file_path = f'{repo_id}_config.ttl'
    with open(config_file_path, 'w') as file:
        file.write(config_ttl)

    # Upload the configuration file to GraphDB
    url = f'{GRAPHDB_BASE_URL}/rest/repositories'
    files = {'config': open(config_file_path, 'rb')}
    response = requests.post(url, files=files)

    if response.status_code == 201:
        print(f"Repository '{repo_id}' created successfully.")
    else:
        print(f"Failed to create repository '{repo_id}': {response.text}")

# Function to upload TBox to a repository
def upload_tbox_to_repository(repo_id, tbox_data, graph_uri):
    response = requests.post(
        f'{GRAPHDB_BASE_URL}/repositories/{repo_id}/statements',
        params={'context': f'<{graph_uri}>'},
        data=tbox_data.encode('utf-8'),
        headers={'Content-Type': 'application/x-turtle'}
    )

    if response.status_code == 204:
        print(f"TBox uploaded to repository '{repo_id}' successfully.")
    else:
        print(f"Failed to upload TBox to repository '{repo_id}': {response.text}")

# Main script execution
repo_id = 'schema_global'
tbox_file_path = './output/tbox/tbox_global.ttl'  # Path to your TBox file
tbox_data = open(tbox_file_path, 'r').read()
graph_uri = 'http://www.example.edu/spicy_bytes/schema#'

create_repository(repo_id)
upload_tbox_to_repository(repo_id, tbox_data, graph_uri)
