import pandas as pd
from rdflib import Graph, URIRef, Literal, Namespace, RDF, XSD
from urllib.parse import quote

# Define namespaces
pub = Namespace("http://www.example.edu/spicy_bytes/")
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")

# Create an RDF graph
g = Graph()


def location():
    customer_location_df = pd.read_csv('./data/location.csv')

    for index, row in customer_location_df.iterrows():
        subject = URIRef(pub + 'location/location_id='+str(row['location_id']))

        location_id_literal = Literal(row['location_id'], datatype = XSD.string)
        country_code_literal = Literal(row['country_code'], datatype = XSD.string)
        postal_code_literal = Literal(row['postal_code'], datatype = XSD.string)
        place_name_literal = Literal(row['place_name'], datatype = XSD.string)
        latitude_literal = Literal(row['latitude'], datatype = XSD.string)
        longitude_literal = Literal(row['longitude'], datatype = XSD.string)
        
        # Add triples to the RDF graph
        g.add((subject, RDF.type, pub.Location))
        g.add((subject, pub.location_id, location_id_literal))
        g.add((subject, pub.country_code, country_code_literal))
        g.add((subject, pub.postal_code, postal_code_literal))
        g.add((subject, pub.place_name, place_name_literal))
        g.add((subject, pub.latitude, latitude_literal))
        g.add((subject, pub.longitude, longitude_literal))

    return g


if __name__ == "__main__":
    kg = location()

    turtle = kg.serialize(format='turtle')
    kg.serialize(destination='./output/abox/abox_location.ttl', format='turtle')
    print(turtle)
