import os
from os.path import dirname, join
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__), ".env"))

if __name__ == "__main__":
    print(os.environ.get("TOPIC"))