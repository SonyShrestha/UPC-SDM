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
g.add((sb.BusinessPurchase, RDF.type, RDFS.Class))


# Properties of class location
g.add((sb.buyer_id, RDF.type, RDF.Property))
g.add((sb.buyer_id, RDFS.domain, sb.BusinessPurchase))
g.add((sb.buyer_id, RDFS.range, XSD.string))

g.add((sb.seller_id, RDF.type, RDF.Property))
g.add((sb.seller_id, RDFS.domain, sb.BusinessPurchase))
g.add((sb.seller_id, RDFS.range, XSD.string))

g.add((sb.product_name, RDF.type, RDF.Property))
g.add((sb.product_name, RDFS.domain, sb.BusinessPurchase))
g.add((sb.product_name, RDFS.range, XSD.string))

g.add((sb.unit_price, RDF.type, RDF.Property))
g.add((sb.unit_price, RDFS.domain, sb.BusinessPurchase))
g.add((sb.unitPrice, RDFS.range, XSD.float))

g.add((sb.quantity, RDF.type, RDF.Property))
g.add((sb.quantity, RDFS.domain, sb.BusinessPurchase))
g.add((sb.quantity, RDFS.range, XSD.float))

g.add((sb.date_purchase, RDF.type, RDF.Property))
g.add((sb.date_purchase, RDFS.domain, sb.BusinessPurchase))
g.add((sb.date_purchase, RDFS.range, XSD.date))

g.serialize(destination='./output/tbox/tbox_spicybytes_b2c.ttl', format='turtle')