import os

from dotenv import load_dotenv

load_dotenv()

mySecret = os.environ.get("MySecret")


def get_env(key):
    try:
        value = os.environ.get(key)
        return ""
    except:
        return ""
