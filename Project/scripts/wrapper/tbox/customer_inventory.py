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
g.add((sb.CustomerInventory, RDF.type, RDFS.Class))


# Properties of class location
g.add((sb.customer_id, RDF.type, RDF.Property))
g.add((sb.customer_id, RDFS.domain, sb.CustomerInventory))
g.add((sb.customer_id, RDFS.range, XSD.string))

g.add((sb.customer_name, RDF.type, RDF.Property))
g.add((sb.customer_name, RDFS.domain, sb.CustomerInventory))
g.add((sb.customer_name, RDFS.range, XSD.string))

g.add((sb.product_name, RDF.type, RDF.Property))
g.add((sb.product_name, RDFS.domain, sb.CustomerInventory))
g.add((sb.product_name, RDFS.range, XSD.string))

g.add((sb.unit_price, RDF.type, RDF.Property))
g.add((sb.unit_price, RDFS.domain, sb.CustomerInventory))
g.add((sb.unit_price, RDFS.range, XSD.float))

g.add((sb.quantity, RDF.type, RDF.Property))
g.add((sb.quantity, RDFS.domain, sb.CustomerInventory))
g.add((sb.quantity, RDFS.range, XSD.float))

g.add((sb.purchase_date, RDF.type, RDF.Property))
g.add((sb.purchase_date, RDFS.domain, sb.CustomerInventory))
g.add((sb.purchase_date, RDFS.range, XSD.date))

g.serialize(destination='./output/tbox/tbox_customer_inventory.ttl', format='turtle')