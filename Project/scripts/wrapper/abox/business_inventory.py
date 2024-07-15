import pandas as pd
from rdflib import Graph, URIRef, Literal, Namespace, RDF, XSD
from urllib.parse import quote
import datetime

# Define namespaces
pub = Namespace("http://www.example.edu/spicy_bytes/")
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")

# Create an RDF graph
g = Graph()

def business_inventory():
    # Read the CSV file with specified encoding
    business_inventory_df = pd.read_csv('./data/business_inventory.csv')
    
    # Normalize product names to lowercase and URL-encode
    business_inventory_df['product_name'] = business_inventory_df['product_name'].str.lower().apply(quote)

    for index, row in business_inventory_df.iterrows():
        subject = URIRef(pub + 'business_inventory/business=' + str(row['store_id']) + "/product=" + str(row['product_name']))

        store_id_literal = Literal(row['store_id'], datatype=XSD.string)
        store_name_literal = Literal(row['store_name'], datatype=XSD.string)
        product_name_literal = Literal(row['product_name'], datatype=XSD.string)  # Corrected typo
        product_price_literal = Literal(row['product_price'].replace(',',''), datatype=XSD.float)
        date_manufacture_literal = Literal(datetime.datetime.strptime(row['manufacture_date'], "%d %b %Y").strftime("%Y-%m-%d"), datatype=XSD.date)
        date_expiry_literal = Literal(datetime.datetime.strptime(row['expiry_date'], "%d %b %Y").strftime("%Y-%m-%d"), datatype=XSD.date)
        quantity_literal = Literal(row['quantity'], datatype=XSD.float)
        
        # Add triples to the RDF graph
        g.add((subject, RDF.type, pub.BusinessInventory))
        g.add((subject, pub.store_id, store_id_literal))
        g.add((subject, pub.store_name, store_name_literal))
        g.add((subject, pub.product_name, product_name_literal))
        g.add((subject, pub.unit_price, product_price_literal))
        g.add((subject, pub.manufacture_date, date_manufacture_literal))
        g.add((subject, pub.expiry_date, date_expiry_literal))
        g.add((subject, pub.quantity, quantity_literal))

    return g

if __name__ == "__main__":
    kg = business_inventory()
    
    turtle = kg.serialize(format='turtle')
    kg.serialize(destination='./output/abox/abox_business_inventory.ttl', format='turtle')
    print(turtle)
