from nyx_client.configuration import ConfigProvider, ConfigType
from nyx_client import NyxClient
import os

env_file = os.path.join(os.getenv("GPTSCRIPT_WORKSPACE_DIR", "."), ".env")
config = ConfigProvider.create_config(env_file=env_file, config_type=ConfigType.BASE)
client = NyxClient(config=config)

data_name = os.getenv('DATANAME', None)

my_subscriptions = client.get_subscribed_datasets()
print(f"name, title, content_type, description")
for s in my_subscriptions:
    print(f"{s.name}, {s.title}, {s.content_type}, ")