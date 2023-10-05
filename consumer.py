import os
import mqtt
from os.path import dirname, join
from dotenv import load_dotenv
from uuid import uuid4

load_dotenv(join(dirname(__file__), ".env"))

def subscribe(client, topic):
    def on_message(client, userdata, msg):
        print(f"[INFO] Received message '{msg.payload.decode()}' from topic '{msg.topic}'")

    client.subscribe(topic)
    client.on_message = on_message


if __name__ == "__main__":
    client = mqtt.connect_mqtt(
        client_id=f"subscribe-{str(uuid4())}",
        username=os.environ.get("USERNAME"),
        password=os.environ.get("PASSWORD"),
    )
    subscribe(client, str(os.environ.get("TOPIC")))
    client.loop_forever()
