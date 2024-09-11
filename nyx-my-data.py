from nyx_client.extensions.langchain import NyxLangChain
from nyx_client.configuration import ConfigProvider, ConfigType
from langchain_openai import ChatOpenAI
import os

config = ConfigProvider.create_config(ConfigType.OPENAI)
llm = ChatOpenAI(model_name="gpt-4o-mini", api_key=config.api_key)
client = NyxLangChain(config=config, llm=llm)

files_path = [os.path.abspath(x) for x in os.listdir()]
print(files_path)
 
data_name = os.getenv('DATANAME', None)

data_path = "data"

if not os.path.exists(data_path):
    os.makedirs(data_path)

my_subscriptions = client.get_subscribed_datasets()
print(f"name, title, content_type, description")
for s in my_subscriptions:
    print(f"{s.name}, {s.title}, {s.content_type}, ")
