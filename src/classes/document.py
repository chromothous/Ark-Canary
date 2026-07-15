class Document:
    def __init__(self, content):
        self.content = content
        self.findings = []

    def add_finding(self, finding):
        self.findings.append(finding)

    def get_finding_count(self):
        return len(self.findings)