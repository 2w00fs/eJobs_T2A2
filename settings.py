import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

client_id = os.environ.get("client_id")
client_secret = os.environ.get("client_secret")
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
OAUTHLIB_INSECURE_TRANSPORT = os.environ.get("OAUTHLIB_INSECURE_TRANSPORT")
OAUTHLIB_RELAX_TOKEN_SCOPE = os.environ.get("OAUTHLIB_RELAX_TOKEN_SCOPE")
secret_key = os.urandom(24)