import pandas as pd
from rdflib import Graph, URIRef, Literal, Namespace, RDF, XSD
from urllib.parse import quote

# Define namespaces
pub = Namespace("http://www.example.edu/spicy_bytes/")
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")

# Create an RDF graph
g = Graph()



def supermarket():
    customers_df = pd.read_csv('./data/supermarket.csv')

    for index, row in customers_df.iterrows():
        subject = URIRef(pub + 'supermarket/'+str(row['id']))

        supermarket_id_literal = Literal(row['id'], datatype = XSD.string)
        commercial_name_literal = Literal(row['commercial_name'], datatype = XSD.string)
        company_nif_literal = Literal(row['company_NIF'], datatype = XSD.string)
        county_code_literal = Literal(row['county_code'], datatype = XSD.string)
        utmx_literal = Literal(row['UTMx'], datatype = XSD.string)
        utmy_literal = Literal(row['UTMy'], datatype = XSD.string)
        latitude = Literal(row['location'].split(',')[0], datatype = XSD.string)
        longitude = Literal(row['location'].split(',')[1], datatype = XSD.string)
        # email_id_literal = Literal(row['email_id'], datatype = XSD.string)
        
        # Add triples to the RDF graph
        g.add((subject, RDF.type, pub.Supermarket))
        g.add((subject, pub.supermarket_id, supermarket_id_literal))
        g.add((subject, pub.commercial_name, commercial_name_literal))
        g.add((subject, pub.company_NIF, company_nif_literal))
        g.add((subject, pub.country_code, county_code_literal))
        g.add((subject, pub.UTMx, utmx_literal))
        g.add((subject, pub.UTMy, utmy_literal))
        g.add((subject, pub.latitude, latitude))
        g.add((subject, pub.longitude, longitude))

    return g



if __name__ == "__main__":
    kg = supermarket()

    turtle = kg.serialize(format='turtle')
    kg.serialize(destination='./output/abox/abox_supermarket.ttl', format='turtle')
    print(turtle)
