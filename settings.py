import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
db_name = os.environ.get("DB_NAME")
db_address = os.environ.get("DB_ADDRESS")
db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
OAUTHLIB_INSECURE_TRANSPORT = os.environ.get("OAUTHLIB_INSECURE_TRANSPORT")
OAUTHLIB_RELAX_TOKEN_SCOPE = os.environ.get("OAUTHLIB_RELAX_TOKEN_SCOPE")

secret_key = os.urandom(24)

"""

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
db_name = os.environ.get("DB_NAME")
db_address = os.environ.get("DB_ADDRESS")
db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
OAUTHLIB_INSECURE_TRANSPORT = os.environ.get("OAUTHLIB_INSECURE_TRANSPORT")
OAUTHLIB_RELAX_TOKEN_SCOPE = os.environ.get("OAUTHLIB_RELAX_TOKEN_SCOPE")

client_id = input("Client ID: ")
client_secret = input("Client ID: ")
db_name = input("DB NAME: ")
db_address = input("DB ADDRESS: ")
db_user = input("DB USER: ")
db_pass = input("DB PASS: ")
OAUTHLIB_INSECURE_TRANSPORT = input("OAUTHLIB_INSECURE_TRANSPORT: ")
OAUTHLIB_RELAX_TOKEN_SCOPE = input("OAUTHLIB_RELAX_TOKEN_SCOPE: ")

"""