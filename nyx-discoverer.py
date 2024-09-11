from nyx_client.extensions.langchain import NyxLangChain
from nyx_client.configuration import ConfigProvider, ConfigType
from langchain_openai import ChatOpenAI
import os
import sys
import csv

env_file = os.path.join(os.getenv("GPTSCRIPT_WORKSPACE_DIR", "."), ".env")
config = ConfigProvider.create_config(env_file=env_file, config_type=ConfigType.OPENAI)
llm = ChatOpenAI(model_name="gpt-4o-mini", api_key=config.api_key)
client = NyxLangChain(config=config, llm=llm)

def print_as_csv(data):
    if not data:
        print("No data to print")
        return
    fieldnames = data[0].keys()
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

found_products = client._federated_sparql_query("""
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX pnyx: <http://data.iotics.com/pnyx#>
PREFIX adms: <http://www.w3.org/ns/adms#>
PREFIX dc: <http://purl.org/dc/terms/>
PREFIX iotics: <http://data.iotics.com/iotics#>

SELECT ?resource ?name ?title ?publisher ?content_type ?description
WHERE {
  ?resource adms:status "published" ;
            pnyx:productName ?name ;
            dcat:mediaType ?mediaTypeFull ;
            dc:description ?description ;
            dc:title ?title ;
            dc:creator ?publisher .
  
  # Extract the substring after "http://www.iana.org/assignments/media-types/"
  BIND(REPLACE(STR(?mediaTypeFull), "http://www.iana.org/assignments/media-types/", "") AS ?content_type)
}
""")

print_as_csv(found_products)