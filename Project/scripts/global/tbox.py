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
g.add((sb.FoodSystem, RDF.type, RDFS.Class))
g.add((sb.Inventory, RDF.type, RDFS.Class))
g.add((sb.CustomerInventory, RDF.type, RDFS.Class))
g.add((sb.SupermarketInventory, RDF.type, RDFS.Class))
g.add((sb.Purchases, RDF.type, RDFS.Class))
g.add((sb.CustomerPurchases, RDF.type, RDFS.Class))
g.add((sb.BusinessPurchases, RDF.type, RDFS.Class))
g.add((sb.Customer, RDF.type, RDFS.Class))
g.add((sb.Location, RDF.type, RDFS.Class))
g.add((sb.Supermarket, RDF.type, RDFS.Class))
g.add((sb.Product, RDF.type, RDFS.Class))


# Properties of class location
# FoodSystem
g.add((sb.has, RDF.type, RDF.Property))
g.add((sb.has, RDFS.domain, sb.FoodSystem))
g.add((sb.has, RDFS.range, sb.Inventory))

g.add((sb.has, RDF.type, RDF.Property))
g.add((sb.has, RDFS.domain, sb.FoodSystem))
g.add((sb.has, RDFS.range, sb.Purchases))


# Inventory
g.add((sb.contains, RDF.type, RDF.Property))
g.add((sb.contains, RDFS.domain, sb.Inventory))
g.add((sb.contains, RDFS.range, sb.CustomerInventory))

g.add((sb.contains, RDF.type, RDF.Property))
g.add((sb.contains, RDFS.domain, sb.Inventory))
g.add((sb.contains, RDFS.range, sb.SupermarketInventory))


# Purchases
g.add((sb.contains, RDF.type, RDF.Property))
g.add((sb.contains, RDFS.domain, sb.Purchases))
g.add((sb.contains, RDFS.range, sb.CustomerPurchases))

g.add((sb.contains, RDF.type, RDF.Property))
g.add((sb.contains, RDFS.domain, sb.Purchases))
g.add((sb.contains, RDFS.range, sb.BusinessPurchases))


# CustomerInventory
g.add((sb.unitPrice, RDF.type, RDF.Property))
g.add((sb.unitPrice, RDFS.domain, sb.CustomerInventory))
g.add((sb.unitPrice, RDFS.range, xsd.float))

g.add((sb.quantityRemaining, RDF.type, RDF.Property))
g.add((sb.quantityRemaining, RDFS.domain, sb.CustomerInventory))
g.add((sb.quantityRemaining, RDFS.range, xsd.float))

g.add((sb.datePurchased, RDF.type, RDF.Property))
g.add((sb.datePurchased, RDFS.domain, sb.CustomerInventory))
g.add((sb.datePurchased, RDFS.range, xsd.date))

g.add((sb.ofCustomer, RDF.type, RDF.Property))
g.add((sb.ofCustomer, RDFS.domain, sb.CustomerInventory))
g.add((sb.ofCustomer, RDFS.range, sb.Customer))

g.add((sb.hasProduct, RDF.type, RDF.Property))
g.add((sb.hasProduct, RDFS.domain, sb.CustomerInventory))
g.add((sb.hasProduct, RDFS.range, sb.Product))


# SupermarketInventory
g.add((sb.unitPrice, RDF.type, RDF.Property))
g.add((sb.unitPrice, RDFS.domain, sb.SupermarketInventory))
g.add((sb.unitPrice, RDFS.range, xsd.float))

g.add((sb.quantityRemaining, RDF.type, RDF.Property))
g.add((sb.quantityRemaining, RDFS.domain, sb.SupermarketInventory))
g.add((sb.quantityRemaining, RDFS.range, xsd.float))

g.add((sb.dateExpiry, RDF.type, RDF.Property))
g.add((sb.dateExpiry, RDFS.domain, sb.SupermarketInventory))
g.add((sb.dateExpiry, RDFS.range, xsd.date))

g.add((sb.date, RDF.type, RDF.Property))
g.add((sb.date, RDFS.domain, sb.SupermarketInventory))
g.add((sb.date, RDFS.range, xsd.date))

g.add((sb.ofSupermarket, RDF.type, RDF.Property))
g.add((sb.ofSupermarket, RDFS.domain, sb.SupermarketInventory))
g.add((sb.ofSupermarket, RDFS.range, sb.Supermarket))

g.add((sb.hasProduct, RDF.type, RDF.Property))
g.add((sb.hasProduct, RDFS.domain, sb.SupermarketInventory))
g.add((sb.hasProduct, RDFS.range, sb.Product))



# Product
g.add((sb.product_name, RDF.type, RDF.Property))
g.add((sb.product_name, RDFS.domain, sb.Product))
g.add((sb.product_name, RDFS.range, sb.string))



# Customer
g.add((sb.idCustomer, RDF.type, RDF.Property))
g.add((sb.idCustomer, RDFS.domain, sb.Customer))
g.add((sb.idCustomer, RDFS.range, xsd.string))

g.add((sb.nameCustomer, RDF.type, RDF.Property))
g.add((sb.nameCustomer, RDFS.domain, sb.Customer))
g.add((sb.nameCustomer, RDFS.range, xsd.string))

g.add((sb.idEmail, RDF.type, RDF.Property))
g.add((sb.idEmail, RDFS.domain, sb.Customer))
g.add((sb.idEmail, RDFS.range, xsd.string))

g.add((sb.stays, RDF.type, RDF.Property))
g.add((sb.stays, RDFS.domain, sb.Customer))
g.add((sb.stays, RDFS.range, sb.Location))



# Location
g.add((sb.idLocation, RDF.type, RDF.Property))
g.add((sb.idLocation, RDFS.domain, sb.Location))
g.add((sb.idLocation, RDFS.range, xsd.string))

g.add((sb.namePlace, RDF.type, RDF.Property))
g.add((sb.namePlace, RDFS.domain, sb.Location))
g.add((sb.namePlace, RDFS.range, xsd.string))

g.add((sb.codePostal, RDF.type, RDF.Property))
g.add((sb.codePostal, RDFS.domain, sb.Location))
g.add((sb.codePostal, RDFS.range, xsd.string))

g.add((sb.codeCountry, RDF.type, RDF.Property))
g.add((sb.codeCountry, RDFS.domain, sb.Location))
g.add((sb.codeCountry, RDFS.range, xsd.string))

g.add((sb.latitude, RDF.type, RDF.Property))
g.add((sb.latitude, RDFS.domain, sb.Location))
g.add((sb.latitude, RDFS.range, xsd.float))

g.add((sb.longitude, RDF.type, RDF.Property))
g.add((sb.longitude, RDFS.domain, sb.Location))
g.add((sb.longitude, RDFS.range, xsd.float))


# Supermarket
g.add((sb.idStore, RDF.type, RDF.Property))
g.add((sb.idStore, RDFS.domain, sb.Supermarket))
g.add((sb.idStore, RDFS.range, xsd.string))

g.add((sb.codeCounty, RDF.type, RDF.Property))
g.add((sb.codeCounty, RDFS.domain, sb.Supermarket))
g.add((sb.codeCounty, RDFS.range, xsd.string))

g.add((sb.nameCommercial, RDF.type, RDF.Property))
g.add((sb.nameCommercial, RDFS.domain, sb.Supermarket))
g.add((sb.nameCommercial, RDFS.range, xsd.string))

g.add((sb.NIFCompany, RDF.type, RDF.Property))
g.add((sb.NIFCompany, RDFS.domain, sb.Supermarket))
g.add((sb.NIFCompany, RDFS.range, xsd.string))


# CustomerPurchases
g.add((sb.datePurchased, RDF.type, RDF.Property))
g.add((sb.datePurchased, RDFS.domain, sb.CustomerPurchases))
g.add((sb.datePurchased, RDFS.range, xsd.date))

g.add((sb.quantityPurchased, RDF.type, RDF.Property))
g.add((sb.quantityPurchased, RDFS.domain, sb.CustomerPurchases))
g.add((sb.quantityPurchased, RDFS.range, xsd.float))

g.add((sb.unitPrice, RDF.type, RDF.Property))
g.add((sb.unitPrice, RDFS.domain, sb.CustomerPurchases))
g.add((sb.unitPrice, RDFS.range, xsd.float))

g.add((sb.seller, RDF.type, RDF.Property))
g.add((sb.seller, RDFS.domain, sb.CustomerPurchases))
g.add((sb.seller, RDFS.range, sb.Customer))

g.add((sb.buyer, RDF.type, RDF.Property))
g.add((sb.buyer, RDFS.domain, sb.CustomerPurchases))
g.add((sb.buyer, RDFS.range, sb.Customer))

g.add((sb.productPurchased, RDF.type, RDF.Property))
g.add((sb.productPurchased, RDFS.domain, sb.CustomerPurchases))
g.add((sb.productPurchased, RDFS.range, sb.Product))



# BusinessPurchases
g.add((sb.datePurchased, RDF.type, RDF.Property))
g.add((sb.datePurchased, RDFS.domain, sb.BusinessPurchases))
g.add((sb.datePurchased, RDFS.range, xsd.date))

g.add((sb.quantityPurchased, RDF.type, RDF.Property))
g.add((sb.quantityPurchased, RDFS.domain, sb.BusinessPurchases))
g.add((sb.quantityPurchased, RDFS.range, xsd.float))

g.add((sb.unitPrice, RDF.type, RDF.Property))
g.add((sb.unitPrice, RDFS.domain, sb.BusinessPurchases))
g.add((sb.unitPrice, RDFS.range, xsd.float))

g.add((sb.seller, RDF.type, RDF.Property))
g.add((sb.seller, RDFS.domain, sb.BusinessPurchases))
g.add((sb.seller, RDFS.range, sb.Superamrket))

g.add((sb.buyer, RDF.type, RDF.Property))
g.add((sb.buyer, RDFS.domain, sb.BusinessPurchases))
g.add((sb.buyer, RDFS.range, sb.Customer))

g.add((sb.productPurchased, RDF.type, RDF.Property))
g.add((sb.productPurchased, RDFS.domain, sb.BusinessPurchases))
g.add((sb.productPurchased, RDFS.range, sb.Product))

g.serialize(destination='./output/tbox/tbox_global.ttl', format='turtle')