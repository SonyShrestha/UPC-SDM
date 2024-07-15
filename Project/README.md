# SDM_Project

## Overview
This project demonstrates a virtual data integration solution using a knowledge graph in GraphDB. The solution involves integrating data from multiple local repositories into a global schema using Local-As-View (LAV) mapping. The integration is done virtually, enabling real-time querying of distributed data sources without physically moving the data. Metadata tracking is implemented to ensure transparency and auditability of data integration actions.


## Prerequisites
1. Python 3.x
2. GraphDB installed and running locally
3. DFLib Python library
4. SPARQLWrapper Python library
5. TBox and ABox data files for various repositories

### Step 1: Create Local Repositories and Load Data

1. **Create Repositories**: Use the `repository_creation.py` script to create local repositories. It automatically Load **TBox (schema) and Abox (instance)** into the created respository. It also create different config files (DO NOT LOAD the config to GraphDB)

### Step 2: Create Global Schema Repository

1. **Create Global Schema Repository**: Manually Create a repository for the global schema with namespace http://www.example.edu/spicy_bytes/schema# in the GraphDB's workbench (you can call it schema_global) and load only the global TBox data in the output folder .

### Step 3: Create Federated Repository

1. **Create Federated Repository**: In GraphDB, create a federated repository anmed federation and add all local repositories and the global schema repository as members.

### Step 4: Run LAV Mapping

1. **Run LAV Mapping Script**: Execute the `LAV_mapping.py` script to perform the virtual data integration.
    - **Construct Queries**: For each entity type, CONSTRUCT queries are executed to fetch and reshape data from local repositories.
    - **Data Insertion**: The resulting RDF data is inserted into the global schema repository.
    - **Metadata Tracking**: Metadata about the data insertion operations is generated and stored in the metadata repository.

### Step 5: Query the Global Schema

1. **Run Query Script**: Use the `query_global_schema.py` script to query the global schema and retrieve integrated data.

## Repository Contents

### Scripts

- `repository_creation.py`: Script to create local repositories and load TBox data.
- `LAV_mapping.py`: Script to perform LAV mapping and data integration, with metadata tracking.
- `query_global_schema.py`: Script to query the global schema and retrieve integrated data.

### Example Metadata Query

To retrieve metadata from the metadata repository, you can use a SPARQL query like this:

```sparql

PREFIX meta: <http://www.example.edu/spicy_bytes/metadata#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?source ?sourceId ?sourceName ?audit ?timestamp ?action ?performedBy
WHERE {
  ?source a meta:Source ;
          meta:sourceId ?sourceId ;
          meta:sourceName ?sourceName .
  
  ?audit a meta:AuditTrail ;
         meta:relatedSource ?source ;
         meta:timestamp ?timestamp ;
         meta:action ?action ;
         meta:performedBy ?performedBy .
}
ORDER BY ?source ?timestamp
```

## Usage Instructions

1. **Clone the Repository**: Clone this GitHub repository to your local machine.
2. **Set Up GraphDB**: Ensure you have GraphDB installed and running.
3. **Run `repository_creation.py`**: Execute this script to create the local repositories and load the TBox data automatically.
4. **Create Global Schema Repository**: Manually create the global schema repository in GraphDB and load your TBox.
5. **Load ABox Data**: Load the ABox data into each of the local repositories created by `repository_creation.py`.
6. **Create Federated Repository**: In GraphDB, create a federated repository and add all local repositories and the global schema repository as members.
7. **Run `LAV_mapping.py`**: Execute this script to map the local views/wrappers to the global schema and perform the data integration with metadata tracking.
8. **Run `query_global_schema.py`**: Execute this script to query the global schema and retrieve the integrated data.
