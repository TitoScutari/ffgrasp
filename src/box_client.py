import boxsdk as box
import os
from dotenv import load_dotenv

load_dotenv()

auth = box.OAuth2(
        client_id = os.getenv('BOXAPP-CLIENT-ID'),
        client_secret = os.getenv('BOXAPP-CLIENT-SECRET'),
        access_token = os.getenv('BOXAPP-DEV-TOKEN')
        )

client = box.Client(auth)

user = client.user().get()
print('user: '+ user.id)
