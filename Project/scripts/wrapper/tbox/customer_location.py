from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, RDFS, XSD

# Define namespaces
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
sb = Namespace("http://www.example.edu/spicy_bytes/")

# Create an empty graph
g = Graph()

# Add triples to the graph
g.add((sb.CustomerLocation, RDF.type, RDFS.Class))


# Properties of class location
g.add((sb.customer_id, RDF.type, RDF.Property))
g.add((sb.customer_id, RDFS.domain, sb.CustomerLocation))
g.add((sb.customer_id, RDFS.range, XSD.string))

g.add((sb.location_id, RDF.type, RDF.Property))
g.add((sb.location_id, RDFS.domain, sb.CustomerLocation))
g.add((sb.location_id, RDFS.range, XSD.string))


g.serialize(destination='./output/tbox/tbox_customer_location.ttl', format='turtle')