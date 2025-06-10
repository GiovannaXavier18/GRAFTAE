import requests
from rdflib import Graph, Namespace
from rdflib.namespace import RDF

g = Graph()
g.parse("ontologia.rdf", format="xml")

ONT = Namespace("http://www.semanticweb.org/xavie/ontologies/2025/2/untitled-ontology-25/")
g.bind("ont", ONT)

# Função para buscar registros do Zenodo
def fetch_records(query, size=10):
    url = "https://zenodo.org/api/records"
    params = {
        "q": query,
        "size": size
    }
    response = requests.get(url, params=params)
    return response.json()["hits"]["hits"]

def process_records(records):
    for record in records:
        metadata = record.get("metadata", {})
        
        title = metadata.get("title")
        article_uri = ONT[title.replace(' ', '_')]
        if title:
            g.add((article_uri, RDF.type, ONT.Publication))
       
query = 'autism AND ("visual support" OR "storytelling")'
records = fetch_records(query, size=10)
process_records(records)
print(records)
# Serialização do grafo
g.serialize("zenodo_articles.ttl", format="turtle")
print(f"Grafo RDF gerado com {len(g)} triplas.")
