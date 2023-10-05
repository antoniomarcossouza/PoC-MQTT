import os, paho, time
import mqtt
from os.path import dirname, join
from dotenv import load_dotenv
from uuid import uuid4

load_dotenv(join(dirname(__file__), ".env"))


def publish(client, topic) -> None:
    count = 1
    while True:
        msg = f"Message {count}"
        time.sleep(1)
        result = client.publish(topic, msg)
        if result[0] == 0:
            print(f"[INFO] Sent message '{msg}' to topic '{topic}'")
        else:
            print(f"[ERROR] Failed to send message to topic '{topic}'")
        count += 1
        if count > 5:
            break


if __name__ == "__main__":
    client = mqtt.connect_mqtt(
        client_id=f"publish-{str(uuid4())}",
        username=os.environ.get("USERNAME"),
        password=os.environ.get("PASSWORD"),
    )
    client.loop_start()
    publish(client, str(os.environ.get("TOPIC")))
    client.loop_stop()
