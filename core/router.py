from core.logger import get_logger
from core.routing_engine import RoutingEngine

logger = get_logger("Router")

class Router:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.engine = RoutingEngine("config/routing.yaml")

    def route(self, topic, payload):
        try:
            targets = self.engine.get_targets(topic, payload)

            if not targets:
                logger.warning(f"No route for {topic}")
                return

            for t in targets:
                self.event_bus.publish(t, payload)

            logger.info(f"Routed {topic} → {targets}")

        except Exception as e:
            logger.error(f"Routing error: {e}")