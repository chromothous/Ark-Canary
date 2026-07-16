import json

class Finding:
    def __init__(self, text, reason, severity, category, start_index, end_index):
        self.text = text
        self.reason = reason
        self.severity = severity
        self.category = category
        self.start_index = start_index
        self.end_index = end_index

    def to_dict(self):
        return {
            "text": self.text,
            "reason": self.reason,
            "severity": self.severity,
            "category": self.category,
            "start_index": self.start_index,
            "end_index": self.end_index
        }
    
    def to_json(self):
        return json.dumps(self.to_dict())