from nyx_client.extensions.langchain import NyxLangChain
from nyx_client.configuration import ConfigProvider, ConfigType
from langchain_openai import ChatOpenAI
import urllib.request 
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


# Fetch the environment variable and handle the case when it's None or an empty string
name_list = os.getenv('DATANAMES', '')

name_list = name_list.split(',') if name_list else []

data_path = "data"

if not os.path.exists(data_path):
    os.makedirs(data_path)

my_subscriptions = client.get_subscribed_datasets()
# Loop through each subscription
for s in my_subscriptions:
    if s.name in name_list:
        # Build the file path dynamically
        file_name = os.path.join(data_path, f"{s.name}.{s.content_type}")
        
        try:
            # Attempt to download the file
            urllib.request.urlretrieve(s.url, file_name)
        except Exception as e:
            # Print or log the error for debugging
            print(f"Failed to download {s.name}: {str(e)}")

