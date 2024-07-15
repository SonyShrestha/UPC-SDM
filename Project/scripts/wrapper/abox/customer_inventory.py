import pandas as pd
from rdflib import Graph, URIRef, Literal, Namespace, RDF, XSD
from urllib.parse import quote

# Define namespaces
pub = Namespace("http://www.example.edu/spicy_bytes/")
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")

# Create an RDF graph
g = Graph()


def customer_inventory():
    customer_purchase_df = pd.read_csv('./data/customer_inventory.csv')
    customer_purchase_df['product_name'] = customer_purchase_df['product_name'].str.lower().apply(quote)

    for index, row in customer_purchase_df.iterrows():
        subject = URIRef(pub + 'customer_inventory/customer='+str(row['customer_id'])+"/product="+str(row['product_name'])+"/purchase_date="+str(row['purchase_date']))

        customer_id_literal = Literal(row['customer_id'], datatype = XSD.string)
        customer_name_literal = Literal(row['customer_name'], datatype = XSD.string)
        product_name_literal = Literal(row['product_name'], datatype = XSD.string)
        unit_price_literal = Literal(row['unit_price'].replace(",",""), datatype = XSD.float)
        quantity_literal = Literal(row['quantity'], datatype = XSD.integer)
        purchased_date_literal = Literal(row['purchase_date'], datatype = XSD.date)
        
        # Add triples to the RDF graph
        g.add((subject, RDF.type, pub.CustomerInventory))
        g.add((subject, pub.customer_id, customer_id_literal))
        g.add((subject, pub.customer_name, customer_name_literal))
        g.add((subject, pub.product_name, product_name_literal))
        g.add((subject, pub.unit_price, unit_price_literal))
        g.add((subject, pub.quantity, quantity_literal))
        g.add((subject, pub.purchase_date, purchased_date_literal))

    return g


if __name__ == "__main__":
    kg = customer_inventory()

    turtle = kg.serialize(format='turtle')
    kg.serialize(destination='./output/abox/abox_customer_inventory.ttl', format='turtle')
    print(turtle)
