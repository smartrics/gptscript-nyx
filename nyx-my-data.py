from nyx_client.extensions.langchain import NyxLangChain
from nyx_client.configuration import ConfigProvider, ConfigType
from langchain_openai import ChatOpenAI
import os
import sys

env_file=os.getenv("GPTSCRIPT_WORKSPACE_DIR", None) 
if env_file is None:
    print("you must specify the --workspace flag pointing to a directory where the nyx .env file exists")
    sys.exit()    
env_file = os.path.join(env_file, ".env")

config = ConfigProvider.create_config(env_file=env_file, config_type=ConfigType.OPENAI)
llm = ChatOpenAI(model_name="gpt-4o-mini", api_key=config.api_key)
client = NyxLangChain(config=config, llm=llm)

data_name = os.getenv('DATANAME', None)

my_subscriptions = client.get_subscribed_datasets()
print(f"name, title, content_type, description")
for s in my_subscriptions:
    print(f"{s.name}, {s.title}, {s.content_type}, ")