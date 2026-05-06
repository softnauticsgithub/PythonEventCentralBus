import yaml
import re

class RoutingEngine:
    def __init__(self, config_path):
        with open(config_path, "r") as f:
            self.rules = yaml.safe_load(f)["routes"]

    def match_topic(self, pattern, topic):
        # Convert MQTT wildcard to regex
        pattern = pattern.replace("+", "[^/]+").replace("#", ".*")
        return re.fullmatch(pattern, topic) is not None

    def match_payload(self, rule_payload, payload):
        if not rule_payload:
            return True

        for key, val in rule_payload.items():
            if payload.get(key) != val:
                return False
        return True

    def get_targets(self, topic, payload):
        targets = []

        for rule in self.rules:
            match = rule.get("match", {})
            topic_match = self.match_topic(match.get("topic", ""), topic)
            payload_match = self.match_payload(match.get("payload"), payload)

            if topic_match and payload_match:
                for t in rule.get("targets", []):
                    targets.append(t["topic"])

        return targets