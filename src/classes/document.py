class Document:
    def __init__(self, content):
        self.content = content
        self.findings = []

    def add_finding(self, finding):
        self.findings.append(finding)