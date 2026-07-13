from classes.finding import Finding

class Rule:
    def __init__(self, name, description, severity):
        self.name = name
        self.description = description
        self.severity = severity

    def evaluate(self, document):
        keyword = "URGENT"

        start_index = document.content.upper().find(keyword)
        end_index = start_index + len(keyword)

        if "URGENT" in document.content.upper():
            finding = Finding(
                "URGENT",
                self.description,
                self.severity,
                "Social Engineering",
                start_index,
                end_index
            )

            document.add_finding(finding)