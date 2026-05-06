class EventBus:
    def __init__(self):
        self.adapters = []

    def register(self, adapter):
        self.adapters.append(adapter)

    def publish(self, topic, payload):
        for adapter in self.adapters:
            adapter.publish(topic, payload)