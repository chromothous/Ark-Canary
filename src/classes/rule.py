from classes.finding import Finding

class Rule:
    def __init__(self, name, description, severity, keyword):
        self.name = name
        self.description = description
        self.severity = severity
        self.keyword = keyword

    def evaluate(self, document):
        start_index = document.content.upper().find(
            self.keyword.upper()
        )

        if start_index != -1:
            end_index = start_index + len(self.keyword)

            finding = Finding(
                self.keyword,
                self.description,
                self.severity,
                "Social Engineering",
                start_index,
                end_index
            )

            document.add_finding(finding)