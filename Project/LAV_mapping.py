# Function to execute a SPARQL CONSTRUCT query
from SPARQLWrapper import SPARQLWrapper, N3
from rdflib import Graph, Namespace, Literal, RDF, XSD
from datetime import datetime
import requests

GRAPHDB_BASE_URL = 'http://localhost:7200'
FEDERATED_REPO_URL = f'{GRAPHDB_BASE_URL}/repositories/federation'
GLOBAL_REPO_URL = f'{GRAPHDB_BASE_URL}/repositories/schema_global/statements'
METADATA_REPO_URL = f'{GRAPHDB_BASE_URL}/repositories/metadata/statements'


meta = Namespace("http://www.example.edu/spicy_bytes/metadata#")


# Function to execute a SPARQL CONSTRUCT query
def execute_construct_query(repo_url, query):
    sparql = SPARQLWrapper(repo_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(N3)  # Request N-Triples format
    try:
        results = sparql.query().convert()
        return results
    except Exception as e:
        print(f"Error executing query on {repo_url}: {e}")
        return None

# Function to insert RDF data into a repository
def insert_data_into_repository(repo_url, rdf_data):
    headers = {'Content-Type': 'application/x-turtle'}
    response = requests.post(repo_url, data=rdf_data, headers=headers)
    if response.status_code == 204:  # 204 No Content is the expected success status for SPARQL UPDATE
        print(f"Data inserted successfully into {repo_url}.")
    else:
        print(f"Error inserting data into {repo_url}: {response.text}")
        
        
# Function to create metadata instances for source tracking and audit trails
def create_metadata(entity, action, graph_uri):
    metadata_graph = Graph()
    metadata_graph.bind("meta", meta)
    timestamp = datetime.now().isoformat()
    source_instance = meta[entity]
    audit_instance = meta[f'audit_{entity}_{timestamp}']

    metadata_graph.add((source_instance, RDF.type, meta.Source))
    metadata_graph.add((source_instance, meta.sourceId, Literal(entity, datatype=XSD.string)))
    metadata_graph.add((source_instance, meta.sourceName, Literal(entity, datatype=XSD.string)))

    metadata_graph.add((audit_instance, RDF.type, meta.AuditTrail))
    metadata_graph.add((audit_instance, meta.timestamp, Literal(timestamp, datatype=XSD.dateTime)))
    metadata_graph.add((audit_instance, meta.action, Literal(action, datatype=XSD.string)))
    metadata_graph.add((audit_instance, meta.performedBy, Literal("Automated System", datatype=XSD.string)))
    metadata_graph.add((audit_instance, meta.relatedSource, source_instance))

    return metadata_graph.serialize(format='turtle')
        

# Define SPARQL CONSTRUCT queries for each entity
construct_queries = {
    'SupermarketInventory': """
    PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
    PREFIX local: <http://www.example.edu/spicy_bytes/>

    CONSTRUCT {
      ?s a global:SupermarketInventory ;
         global:unitPrice ?unitPrice ;
         global:quantityRemaining ?quantityRemaining ;
         global:dateExpiry ?dateExpiry ;
         global:date ?date .
    }
    WHERE {
      SERVICE <http://localhost:7200/repositories/business_inventory> {
        ?s a local:BusinessInventory ;
           local:unit_price ?unitPrice ;
           local:quantity ?quantityRemaining ;
           local:expiry_date ?dateExpiry ;
           local:manufacture_date ?date .
      }
    }
    """,
    'Customer': """
    PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
    PREFIX local: <http://www.example.edu/spicy_bytes/>

    CONSTRUCT {
      ?s a global:Customer ;
         global:idCustomer ?idCustomer ;
         global:nameCustomer ?nameCustomer .
    }
    WHERE {
      SERVICE <http://localhost:7200/repositories/customer> {
        ?s a local:Customer ;
           local:customer_id ?idCustomer ;
           local:customer_name ?nameCustomer .
      }
    }
    """,
    'CustomerInventory': """
    PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
    PREFIX local: <http://www.example.edu/spicy_bytes/>

    CONSTRUCT {
      ?s a global:CustomerInventory ;
         global:unitPrice ?unitPrice ;
         global:quantityRemaining ?quantityRemaining ;
         global:dateExpiry ?dateExpiry ;
         global:date ?date .
    }
    WHERE {
      SERVICE <http://localhost:7200/repositories/customer_inventory> {
        ?s a local:CustomerInventory ;
           local:unit_price ?unitPrice ;
           local:quantity ?quantityRemaining ;
           local:purchase_date ?date .
      }
    }
    """,
    'CustomerLocation': """
    PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
    PREFIX local: <http://www.example.edu/spicy_bytes/>

    CONSTRUCT {
      ?s a global:Location ;
         global:idLocation ?idLocation ;
         global:idcustomer ?idcustomer .
    }
    WHERE {
      SERVICE <http://localhost:7200/repositories/customer_location> {
        ?s a local:CustomerLocation ;
           local:location_id ?idLocation ;
           local:customer_id ?idcustomer .
      }
    }
    """,
    'Location': """
    PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
    PREFIX local: <http://www.example.edu/spicy_bytes/>

    CONSTRUCT {
      ?s a global:Location ;
         global:idLocation ?idLocation ;
         global:namePlace ?namePlace ;
         global:codePostal ?codePostal ;
         global:codeCountry ?codeCountry ;
         global:latitude ?latitude ;
         global:longitude ?longitude .
    }
    WHERE {
      SERVICE <http://localhost:7200/repositories/location> {
        ?s a local:Location ;
           local:location_id ?idLocation ;
           local:place_name ?namePlace ;
           local:postal_code ?codePostal ;
           local:country_code ?codeCountry ;
           local:latitude ?latitude ;
           local:longitude ?longitude .
      }
    }
    """,
    'Supermarket': """
    PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
    PREFIX local: <http://www.example.edu/spicy_bytes/>

    CONSTRUCT {
      ?s a global:Supermarket ;
         global:idStore ?idStore ;
         global:codeCounty ?codeCounty ;
         global:nameCommercial ?nameCommercial ;
         global:NIFCompany ?NIFCompany .
    }
    WHERE {
      SERVICE <http://localhost:7200/repositories/supermarkets> {
        ?s a local:Supermarket ;
           local:supermarket_id ?idStore ;
           local:country_code ?codeCounty ;
           local:commercial_name ?nameCommercial ;
           local:company_NIF ?NIFCompany .
      }
    }
    """,
    'BusinessPurchase': """
    PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
    PREFIX local: <http://www.example.edu/spicy_bytes/>

    CONSTRUCT {
      ?b2c a global:BusinessPurchase ;
           global:datePurchased ?datePurchased ;
           global:quantityPurchased ?quantityPurchased ;
           global:unitPrice ?unitPrice ;
           global:seller ?seller ;
           global:buyer ?buyer ;
           global:productPurchased ?productPurchased .
    }
    WHERE {
      SERVICE <http://localhost:7200/repositories/spicybytes_b2c> {
        ?b2c a local:BusinessPurchase ;
             local:quantity ?quantityPurchased ;
             local:unit_price ?unitPrice ;
             local:seller_id ?seller ;
             local:buyer_id ?buyer ;
             local:product_name ?productPurchased .
      }
    }
    """,
    'CustomerPurchase': """
    PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
    PREFIX local: <http://www.example.edu/spicy_bytes/>

    CONSTRUCT {
      ?c2c a global:CustomerPurchase ;
           global:datePurchased ?datePurchased ;
           global:quantityPurchased ?quantityPurchased ;
           global:unitPrice ?unitPrice ;
           global:seller ?seller ;
           global:buyer ?buyer ;
           global:productPurchased ?productPurchased .
    }
    WHERE {
      SERVICE <http://localhost:7200/repositories/spicybytes_c2c> {
        ?c2c a local:CustomerPurchase ;
             local:date_purchase ?datePurchased ;
             local:quantity ?quantityPurchased ;
             local:unit_price ?unitPrice ;
             local:seller_id ?seller ;
             local:buyer_id ?buyer ;
             local:product_name ?productPurchased .
      }
    }
    """
}

# Execute each CONSTRUCT query and collect the results
# Execute each CONSTRUCT query and collect the results
rdf_data_collections = {}
for entity, query in construct_queries.items():
    print(f"Executing CONSTRUCT query for {entity}...")
    rdf_data = execute_construct_query(FEDERATED_REPO_URL, query)
    if rdf_data:
        rdf_data_collections[entity] = rdf_data
        print(f"Data for {entity} fetched successfully.")
    else:
        print(f"No results for {entity}.")

# Insert the constructed triples into the global repository along with metadata
for entity, rdf_data in rdf_data_collections.items():
    print(f"Inserting data for {entity} into the global repository...")
    insert_data_into_repository(GLOBAL_REPO_URL, rdf_data)
    metadata = create_metadata(entity, "Data Insertion", GLOBAL_REPO_URL)
    insert_data_into_repository(METADATA_REPO_URL, metadata) 

print("Local to Global Mapping done using LAV with metadata tracking.")


