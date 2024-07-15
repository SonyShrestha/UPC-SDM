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
g.add((sb.Supermarket, RDF.type, RDFS.Class))

# Properties of class location
g.add((sb.supermarket_id, RDF.type, RDF.Property))
g.add((sb.supermarket_id, RDFS.domain, sb.Supermarket))
g.add((sb.supermarket_id, RDFS.range, XSD.string))

g.add((sb.commercial_name, RDF.type, RDF.Property))
g.add((sb.commercial_name, RDFS.domain, sb.Supermarket))
g.add((sb.commercial_name, RDFS.range, XSD.string))

g.add((sb.company_NIF, RDF.type, RDF.Property))
g.add((sb.company_NIF, RDFS.domain, sb.Supermarket))
g.add((sb.company_NIF, RDFS.range, XSD.string))

g.add((sb.country_code, RDF.type, RDF.Property))
g.add((sb.country_code, RDFS.domain, sb.Supermarket))
g.add((sb.country_code, RDFS.range, XSD.string))

g.add((sb.UTMx, RDF.type, RDF.Property))
g.add((sb.UTMx, RDFS.domain, sb.Supermarket))
g.add((sb.UTMx, RDFS.range, XSD.string))

g.add((sb.UTMy, RDF.type, RDF.Property))
g.add((sb.UTMy, RDFS.domain, sb.Supermarket))
g.add((sb.UTMy, RDFS.range, XSD.string))

g.add((sb.latitude, RDF.type, RDF.Property))
g.add((sb.latitude, RDFS.domain, sb.Supermarket))
g.add((sb.latitude, RDFS.range, XSD.string))

g.add((sb.longitude, RDF.type, RDF.Property))
g.add((sb.longitude, RDFS.domain, sb.Supermarket))
g.add((sb.longitude, RDFS.range, XSD.string))

g.serialize(destination='./output/tbox/tbox_supermarket.ttl', format='turtle')