from SPARQLWrapper import SPARQLWrapper, JSON

# Define the queries
queries = {
    "SupermarketInventory": """
    PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
    SELECT ?s ?unitPrice ?quantityRemaining ?dateExpiry ?date
    WHERE {
      ?s a global:SupermarketInventory ;
         global:unitPrice ?unitPrice ;
         global:quantityRemaining ?quantityRemaining ;
         global:dateExpiry ?dateExpiry ;
         global:date ?date .
    }
    LIMIT 100
    """,
    "Customer": """
    PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
    SELECT ?s ?idCustomer ?nameCustomer
    WHERE {
      ?s a global:Customer ;
         global:idCustomer ?idCustomer ;
         global:nameCustomer ?nameCustomer .
    }
    LIMIT 100
    """,
    "CustomerInventory": """
    PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
    SELECT ?s ?unitPrice ?quantityRemaining ?dateExpiry ?date
    WHERE {
      ?s a global:CustomerInventory ;
         global:unitPrice ?unitPrice ;
         global:quantityRemaining ?quantityRemaining ;
         global:date ?date .
    }
    LIMIT 100
    """,
    "CustomerLocation": """
    PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
    SELECT ?s ?idLocation ?idcustomer
    WHERE {
      ?s a global:Location ;
         global:idLocation ?idLocation ;
         global:idcustomer ?idcustomer .
    }
    LIMIT 100
    """,
    "Location": """
    PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
    SELECT ?s ?idLocation ?namePlace ?codePostal ?codeCountry ?latitude ?longitude
    WHERE {
      ?s a global:Location ;
         global:idLocation ?idLocation ;
         global:namePlace ?namePlace ;
         global:codePostal ?codePostal ;
         global:codeCountry ?codeCountry ;
         global:latitude ?latitude ;
         global:longitude ?longitude .
    }
    LIMIT 100
    """,
    "Supermarket": """
    PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
    SELECT ?s ?idStore ?codeCounty ?nameCommercial ?NIFCompany
    WHERE {
      ?s a global:Supermarket ;
         global:idStore ?idStore ;
         global:codeCounty ?codeCounty ;
         global:nameCommercial ?nameCommercial ;
         global:NIFCompany ?NIFCompany .
    }
    LIMIT 100
    """,
    "BusinessPurchase": """
    PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
    SELECT ?b2c ?datePurchased ?quantityPurchased ?unitPrice ?seller ?buyer ?productPurchased
    WHERE {
      ?b2c a global:BusinessPurchase ;
           global:quantityPurchased ?quantityPurchased ;
           global:unitPrice ?unitPrice ;
           global:seller ?seller ;
           global:buyer ?buyer ;
           global:productPurchased ?productPurchased .
    }
    LIMIT 100
    """,
    "CustomerPurchase": """
    PREFIX global: <http://www.example.edu/spicy_bytes/schema#>
    SELECT ?c2c ?datePurchased ?quantityPurchased ?unitPrice ?seller ?buyer ?productPurchased
    WHERE {
      ?c2c a global:CustomerPurchase ;
           global:datePurchased ?datePurchased ;
           global:quantityPurchased ?quantityPurchased ;
           global:unitPrice ?unitPrice ;
           global:seller ?seller ;
           global:buyer ?buyer ;
           global:productPurchased ?productPurchased .
    }
    LIMIT 100
    """
}

# Define the URL for the SPARQL endpoint
SPARQL_ENDPOINT = 'http://localhost:7200/repositories/federation'

# Function to execute a SPARQL query and print results
def execute_sparql_query(query):
    sparql = SPARQLWrapper(SPARQL_ENDPOINT)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    try:
        results = sparql.query().convert()
        return results
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

# Execute each query and print the results
for query_name, query in queries.items():
    print(f"Executing query for {query_name}...")
    results = execute_sparql_query(query)
    if results:
        print(f"Results for {query_name}:")
        for result in results["results"]["bindings"]:
            print(result)
    else:
        print(f"No results found for {query_name}.")
