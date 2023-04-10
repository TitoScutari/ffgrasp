import boxsdk as box
import os
from dotenv import load_dotenv
import json

load_dotenv()

auth = box.OAuth2(
        client_id = os.getenv('BOXAPP-CLIENT-ID'),
        client_secret = os.getenv('BOXAPP-CLIENT-SECRET'),
        access_token = os.getenv('BOXAPP-DEV-TOKEN')
        )

client = box.Client(auth)

items = client.get_recent_items()
for item in items:
    print(item.item.name)

