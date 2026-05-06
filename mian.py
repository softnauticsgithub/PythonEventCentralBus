from core.event_bus import EventBus
from core.router import Router
from adapters.mqtt_adapter import MQTTAdapter

def main():
    event_bus = EventBus()
    router = Router(event_bus)

    mqtt_adapter = MQTTAdapter(router)
    event_bus.register(mqtt_adapter)

    mqtt_adapter.start()

    print("Python MQTT Router Engine running...")

    # keep alive
    import time
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()