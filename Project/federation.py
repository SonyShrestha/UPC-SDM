import requests

GRAPHDB_BASE_URL = 'http://localhost:7200'

# Adjusted configuration template according to RDF4J guidelines
fedx_config_ttl_template = """
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rep: <http://www.openrdf.org/config/repository#> .
@prefix fedx: <http://www.fluidops.com/config/fedx#> .

<#Repository> a rep:Repository ;
    rep:repositoryID "{}" ;
    rep:repositoryImpl [
        rep:repositoryType "fedx:FedXRepository" ;
        fedx:member [
            fedx:store "SPARQL" ;
            fedx:location "{}"
        ] ;
        fedx:member [
            fedx:store "SPARQL" ;
            fedx:location "{}"
        ]
    ];
    rdfs:label "{}" .
"""

def check_repository_exists(repo_id):
    url = f'{GRAPHDB_BASE_URL}/rest/repositories/{repo_id}'
    response = requests.get(url)
    print(f"Check repo exists response: {response.status_code}")
    return response.status_code == 200

def delete_repository(repo_id):
    if not check_repository_exists(repo_id):
        print("No repository found to delete.")
        return True  # No need to delete if it doesn't exist

    url = f'{GRAPHDB_BASE_URL}/rest/repositories/{repo_id}'
    response = requests.delete(url)
    print(f"Delete repo response: {response.status_code}, {response.text}")
    return response.status_code == 204

def create_repository(repo_id, sparql_endpoint1, sparql_endpoint2, label):
    if check_repository_exists(repo_id):
        print(f"Repository '{repo_id}' already exists. Attempting to delete...")
        if not delete_repository(repo_id):
            print("Failed to delete existing repository.")
            return  # Stop if deletion fails

    config_ttl = fedx_config_ttl_template.format(repo_id, sparql_endpoint1, sparql_endpoint2, label)
    config_file_path = f'{repo_id}_fedx_config.ttl'
    with open(config_file_path, 'w') as file:
        file.write(config_ttl)

    with open(config_file_path, 'rb') as file:
        files = {'config': file}
        url = f'{GRAPHDB_BASE_URL}/rest/repositories'
        response = requests.post(url, files=files)
        print(f"Create repo response: {response.status_code}, {response.text}")
        if response.status_code == 201:
            print(f"Federation repository '{repo_id}' created successfully.")
        else:
            print(f"Failed to create federation repository '{repo_id}': {response.text}")

# Main script
repo_id = 'fedx_sparql_repo'
sparql_endpoint1 = 'http://example.org/sparql1'
sparql_endpoint2 = 'http://example.org/sparql2'
label = 'FedX Virtual SPARQL Repository'

create_repository(repo_id, sparql_endpoint1, sparql_endpoint2, label)
