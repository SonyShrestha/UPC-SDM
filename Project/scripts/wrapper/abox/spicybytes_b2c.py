import pandas as pd
from rdflib import Graph, URIRef, Literal, Namespace, RDF, XSD
from urllib.parse import quote
import datetime

# Define namespaces
pub = Namespace("http://www.example.edu/spicy_bytes/")
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")

# Create an RDF graph
g = Graph()

def spicybytes_b2c():
    # Read the CSV file with specified encoding
    spicybytes_b2c_df = pd.read_csv('./data/spicybytes_b2c.csv')
    
    # Normalize product names to lowercase and URL-encode
    spicybytes_b2c_df['product_name'] = spicybytes_b2c_df['product_name'].str.lower().apply(quote)

    for index, row in spicybytes_b2c_df.iterrows():
        subject = URIRef(pub + 'spicybytes_b2c/seller=' + str(row['store_id']) + "/buyer=" + str(row['customer_id']) + "/product=" + str(row['product_name'])+ "/date=" + str(row['purchase_date']))

        buyer_id_literal = Literal(row['customer_id'], datatype=XSD.string)
        seller_id_literal = Literal(row['store_id'], datatype=XSD.string)
        product_name_literal = Literal(row['product_name'], datatype=XSD.string) 
        product_price_literal = Literal(row['unit_price'], datatype=XSD.float)
        quantity_literal = Literal(row['quantity'], datatype=XSD.float)
        purchase_date_literal = Literal(row['purchase_date'], datatype=XSD.date)
        
        # Add triples to the RDF graph
        g.add((subject, RDF.type, pub.BusinessPurchase))
        g.add((subject, pub.buyer_id, buyer_id_literal))
        g.add((subject, pub.seller_id, seller_id_literal))
        g.add((subject, pub.product_name, product_name_literal))
        g.add((subject, pub.unit_price, product_price_literal))
        g.add((subject, pub.quantity, quantity_literal))
        g.add((subject, pub.purchase_date, purchase_date_literal))

    return g

if __name__ == "__main__":
    kg = spicybytes_b2c()
    
    turtle = kg.serialize(format='turtle')
    kg.serialize(destination='./output/abox/abox_spicybytes_b2c.ttl', format='turtle')
    print(turtle)
