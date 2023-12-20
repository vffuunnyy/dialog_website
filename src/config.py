import os

from pathlib import Path


# from dotenv import load_dotenv
# load_dotenv()

# mongodb

MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
MONGO_DB = os.environ.get("MONGO_DATABASE", "dialog_app")
MONGO_USERNAME = os.environ.get("MONGO_USERNAME", "root")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", "root")
MONGO_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}/"
