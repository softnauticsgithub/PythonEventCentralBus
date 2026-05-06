import json
import paho.mqtt.client as mqtt
from config import settings
from core.logger import get_logger

logger = get_logger("MQTTAdapter")

class MQTTAdapter:
    def __init__(self, router):
        self.router = router
        self.client = mqtt.Client()

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.connect(
            settings.BROKER_HOST,
            settings.BROKER_PORT,
            settings.KEEPALIVE
        )

    def on_connect(self, client, userdata, flags, rc):
        logger.info(f"Connected to MQTT broker: {rc}")
        client.subscribe(settings.TOPIC_SUBSCRIBE)

    def on_message(self, client, userdata, msg):
        try:
            payload = json.loads(msg.payload.decode())
        except:
            payload = msg.payload.decode()

        logger.info(f"Incoming: {msg.topic} → {payload}")
        self.router.route(msg.topic, payload)

    def publish(self, topic, payload):
        self.client.publish(topic, json.dumps(payload))

    def start(self):
        self.client.loop_start()