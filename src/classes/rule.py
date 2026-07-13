from classes.finding import Finding

class Rule:
    def __init__(self, name, description, severity):
        self.name = name
        self.description = description
        self.severity = severity

    def evaluate(self, document):
        if "URGENT" in document.content.upper():
            finding = Finding(
                "URGENT",
                self.description,
                self.severity,
                "Social Engineering"
            )

            document.add_finding(finding)