import os
from os.path import dirname, join
from dotenv import load_dotenv
from paho.mqtt import client as mqtt_client

load_dotenv(join(dirname(__file__), ".env"))


def connect_mqtt(client_id: str, username: str, password: str) -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("[INFO] Connected to MQTT Broker!")
        else:
            print(f"[ERROR] Failed to connect, return code {rc}")

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(str(os.environ.get("BROKER")), int(os.environ.get("PORT")))
    return client
