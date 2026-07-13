class Finding:
    def __init__(self, text, reason, severity, category, start_index, end_index):
        self.text = text
        self.reason = reason
        self.severity = severity
        self.category = category
        self.start_index = start_index
        self.end_index = end_index