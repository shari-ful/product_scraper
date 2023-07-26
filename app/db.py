import os
import pathlib
from dotenv import load_dotenv
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

BASE_DIR = pathlib.Path(__file__).parent
BUNDLE_PATH = str(BASE_DIR / "astradb_bundle" / "bundle.zip")

load_dotenv()

ASTRA_DB_CLIENT_ID=os.environ.get("ASTRA_DB_CLIENT_ID")
ASTRA_DB_CLIENT_SECRET=os.environ.get("ASTRA_DB_CLIENT_SECRET")
ASTRA_DB_TOKEN=os.environ.get("ASTRA_DB_CLIENT_SECRET")


def get_cluster():
    cloud_config= {
        'secure_connect_bundle': BUNDLE_PATH
    }
    auth_provider = PlainTextAuthProvider(ASTRA_DB_CLIENT_ID, ASTRA_DB_CLIENT_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)

    return cluster


def get_session():
    cluster = get_cluster()
    session = cluster.connect()
    return session

session = get_session()
row = session.execute("select release_version from system.local").one()
if row:
  print(row[0])
else:
  print("An error occurred.")

