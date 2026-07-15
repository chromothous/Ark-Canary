from classes.finding import Finding

class Rule:
    def __init__(self, name, description, severity, keyword, category):
        self.name = name
        self.description = description
        self.severity = severity
        self.keyword = keyword
        self.category = category

    def evaluate(self, document):
        search_start = 0

        while True:
            start_index = document.content.upper().find(
                self.keyword.upper(),
                search_start
            )

            if start_index == -1:
                break

            end_index = start_index + len(self.keyword)

            finding = Finding(
                document.content[start_index:end_index],
                self.description,
                self.severity,
                self.category,
                start_index,
                end_index
            )

            document.add_finding(finding)

            search_start = end_index