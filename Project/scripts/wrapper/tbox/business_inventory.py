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
g.add((sb.BusinessInventory, RDF.type, RDFS.Class))


# Properties of class location
g.add((sb.store_id, RDF.type, RDF.Property))
g.add((sb.store_id, RDFS.domain, sb.BusinessInventory))
g.add((sb.store_id, RDFS.range, XSD.string))

g.add((sb.store_name, RDF.type, RDF.Property))
g.add((sb.store_name, RDFS.domain, sb.BusinessInventory))
g.add((sb.store_name, RDFS.range, XSD.string))

g.add((sb.product_name, RDF.type, RDF.Property))
g.add((sb.product_name, RDFS.domain, sb.BusinessInventory))
g.add((sb.product_name, RDFS.range, XSD.string))

g.add((sb.unit_price, RDF.type, RDF.Property))
g.add((sb.unit_price, RDFS.domain, sb.BusinessInventory))
g.add((sb.unit_price, RDFS.range, XSD.float))

g.add((sb.quantity, RDF.type, RDF.Property))
g.add((sb.quantity, RDFS.domain, sb.BusinessInventory))
g.add((sb.quantity, RDFS.range, XSD.float))

g.add((sb.manufacture_date, RDF.type, RDF.Property))
g.add((sb.manufacture_date, RDFS.domain, sb.BusinessInventory))
g.add((sb.manufacture_date, RDFS.range, XSD.date))

g.add((sb.expiry_date, RDF.type, RDF.Property))
g.add((sb.expiry_date, RDFS.domain, sb.BusinessInventory))
g.add((sb.expiry_date, RDFS.range, XSD.date))

g.serialize(destination='./output/tbox/tbox_business_inventory.ttl', format='turtle')