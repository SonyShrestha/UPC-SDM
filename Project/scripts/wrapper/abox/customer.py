import pandas as pd
from rdflib import Graph, URIRef, Literal, Namespace, RDF, XSD
from urllib.parse import quote

# Define namespaces
pub = Namespace("http://www.example.edu/spicy_bytes/")
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")

# Create an RDF graph
g = Graph()



def customers():
    customers_df = pd.read_csv('./data/customers.csv')

    for index, row in customers_df.iterrows():
        subject = URIRef(pub + 'customer/'+str(row['customer_id']))

        customer_id_literal = Literal(row['customer_id'], datatype = XSD.string)
        customer_name_literal = Literal(row['customer_name'], datatype = XSD.string)
        # email_id_literal = Literal(row['email_id'], datatype = XSD.string)
        
        # Add triples to the RDF graph
        g.add((subject, RDF.type, pub.Customer))
        g.add((subject, pub.customer_id, customer_id_literal))
        g.add((subject, pub.customer_name, customer_name_literal))
        #g.add((subject, pub.email_id, email_id_literal))

    return g



if __name__ == "__main__":
    kg = customers()

    turtle = kg.serialize(format='turtle')
    kg.serialize(destination='./output/abox/abox_customer.ttl', format='turtle')
    print(turtle)
