<h1 align="center">GRAFTAE</h1>

![Badge em Desenvolvimento](https://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

# Descrição do Projeto
Este trabalho propõe a construção de um gráfico de conhecimento acadêmico que reúne fontes, como artigos, conjuntos de dados e outros recursos, focados em ferramentas de suporte visual digital aplicadas ao ensino de crianças com autismo.

## Etapas

### 1ª Etapa: Revisão Bibliográfica e Nivelamento
Nesta fase, foi conduzido um estudo detalhado do artigo de revisão bibliográfica intitulado *"Scholarly Knowledge Graphs Through Structuring Scholarly Communication: A Review"*. A análise permitiu identificar os trabalhos mais recentes e relevantes na área, que fornecerão as bases teóricas e técnicas possíveis para o desenvolvimento deste projeto. Esse processo de nivelamento foi essencial para garantir a compreensão das abordagens atuais e das principais tendências no campo dos gráficos de conhecimento.
Link para o artigo: https://drive.google.com/file/d/1leFuuP_6tqMSTUkc2db9v2h7AagR01ep/view?usp=sharing

### 2ª Etapa: Estudo sobre Grafo de Conhecimento Acadêmico
Nesta etapa, realizamos um estudo aprofundado sobre gráficos de conhecimento acadêmico, explorando as principais ferramentas e tecnologias utilizadas para sua construção. Entre os tópicos abordados, destacam-se conceitos fundamentais como ontologias, além de ferramentas e padrões essenciais, como RDF, Turtle e Protégé, que são amplamente utilizados na modelagem e implementação de gráficos de conhecimento. Essas ferramentas e conceitos servirão como técnica base para o desenvolvimento deste projeto.
Link da plalist de estudos: [https://youtu.be/XLV416Gjl4g?si=V_ZD-LQ5_gC4pyQq](https://www.youtube.com/watch?v=XLV416Gjl4g&list=PLLrlHSmC0Mw6lEj060psXrt3BSATBFVzV)

### 3ª Etapa: Construção da ontologia
A contrução ontológica utilizou como base duas ontologias já consolidadas. A primeira foi inspirada no mapeamento de estudos científicos apresentado por Verma et al. (2023), enquanto a segunda, denominada OpenAIRE Graph (Manghi et al. 2023), fornece uma estrutura voltada à representação de softwares e conjuntos de dados, enriquecendo os estudos com informações sobre ferramentas, dados e linguagens utilizadas. Com base nessas referências, foram identificadas as principais entidades e seus relacionamentos, organizando-se esse conhecimento por meio da ferramenta Protégé. Está em RDF no arquivo `ontologia.rdf` . E sua estrutura gráfica está representada da segunte forma:

![Ontology GRAFTAE](img/screenshot.png)

### 4º Etapa: Mapenado informações na ontologia
Para mapear e adicionar instâncias ao grafo, desenvolvemos um script em linguagem Python `scripts/gerar_grafo_publicacoes.py` que extrai e organiza informações de artigos científicos que foram anteriormente armazenadas em planilhas no formato CSV. Após a extração dos arquivos, realizamos a normalização dos textos para garantir a criação de URIs consistentes. Os dados coletados foram estruturados em formato de triplas RDF, representando os relacionamentos entre as entidades conforme o modelo ontológico. O grafo seguiu o padrão RDF, que possibilita consultas semânticas por meio da linguagem SPARQL. Para armazenamento e visualizacão, utilizamos uma ferramenta consolidada, denominada GraphDB.

### 5ª Etapa: Enriquecendo o GRAFTAE
Para enriquecer o GRAFTEA com dados na temática, utilizamos a plataforma Zenodo.org. Por meio de uma API disponível na plataforma, os dados foram mapeados para o GRAFTEA. Inicialmente, definiu-se uma consulta com os termos "autism" e "visual support" ou "storytelling", com o objetivo de recuperar publicações relacionadas ao uso de suportes visuais e narrativas digitais no contexto do autismo. Essa consulta foi executada por meio de uma requisição HTTP, utilizando a biblioteca requests, que retornou os dados em formato JSON.

## Estrutura

- `scripts/gerar_grafo_publicacoes.py`: Lê CSVs com artigos, autores e ferramentas e gera grafo RDF.
- `scripts/importar_artigos_zenodo.py`: Consulta a API do Zenodo e gera grafo RDF.
- `data/`: Contém os arquivos CSV de entrada.
- `output/`: Arquivos RDF gerados no formato Turtle.

## Requisitos

Instale com:

```bash
pip install -r requirements.txt
