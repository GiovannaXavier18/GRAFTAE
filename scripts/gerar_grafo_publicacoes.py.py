import pandas as pd
from rdflib import Graph, Namespace
from rdflib.namespace import RDF
import unicodedata
import re

csv_file_0 = "data_extraction.xlsx - Articles.csv"  
csv_file_1 = "data_extraction (1).xlsx - Articles.csv"  
colunas = ["article", "Autores", "Ferramenta"]  
df_0 = pd.read_csv(csv_file_0, usecols=colunas)
df_1 = pd.read_csv(csv_file_1, usecols=colunas)
df = pd.concat([df_0, df_1], ignore_index=True)

def normaliza_str(texto):
    texto_norm = unicodedata.normalize('NFD', texto)
    texto_sem_acentos = texto_norm.encode('ascii', 'ignore').decode('utf-8')
    texto_limpo = re.sub(r'[^A-Za-z0-9 ]', '', texto_sem_acentos)
    return texto_limpo.replace(' ', '_').replace('-', '_').lower()

def split_authors(author_string): 
    if pd.isna(author_string):
        return []
    author_string = author_string.replace(" e ", ", ").replace(" and ", ", ")
    authors = re.split(r",\s*", author_string)
    return [author.strip() for author in authors]

def creat_graph(data):
    g = Graph()
    g.parse("ontologia.rdf", format="xml") 
    
    
    ONT = Namespace("http://www.semanticweb.org/xavie/ontologies/2025/2/untitled-ontology-25/")
    g.bind("ont", ONT)
    
    
    for _, row in data.iterrows():
        article_uri = ONT[normaliza_str(row["article"])]
        g.add((article_uri, RDF.type, ONT.Publication))
        
        authors = split_authors(row["Autores"])
        for author in authors:
            author_uri = ONT[normaliza_str(author)]
            g.add((author_uri, RDF.type, ONT.Author))
            g.add((article_uri, ONT.written_by, author_uri))

       
        if not pd.isna(row["Ferramenta"]):
            ferramenta_nome = row["Ferramenta"]
            ferramenta_uri = ONT[normaliza_str(ferramenta_nome)]
            g.add((ferramenta_uri, RDF.type, ONT.Software))
            g.add((article_uri, ONT.has_software, ferramenta_uri))
    
    g.serialize("skg.ttl", format="turtle")
    print(f"Total de triplas geradas: {len(g)}")

creat_graph(df)

