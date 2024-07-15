import pandas as pd
from rdflib import Graph, URIRef, Literal, Namespace, RDF, XSD
from urllib.parse import quote

# Define namespaces
pub = Namespace("http://www.example.edu/spicy_bytes/")
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")

# Create an RDF graph
g = Graph()


def customer_location():
    customer_location_df = pd.read_csv('./data/customer_location.csv')

    for index, row in customer_location_df.iterrows():
        subject = URIRef(pub + 'customer_location/customer='+str(row['customer_id'])+'/location_id='+str(row['location_id']))

        customer_literal = Literal(row['customer_id'], datatype = XSD.string)
        location_literal = Literal(row['location_id'], datatype = XSD.string)
        
        # Add triples to the RDF graph
        g.add((subject, RDF.type, pub.CustomerLocation))
        g.add((subject, pub.customer_id, customer_literal))
        g.add((subject, pub.location_id, location_literal))

    return g


if __name__ == "__main__":
    kg = customer_location()

    turtle = kg.serialize(format='turtle')
    kg.serialize(destination='./output/abox/abox_customer_location.ttl', format='turtle')
    print(turtle)
