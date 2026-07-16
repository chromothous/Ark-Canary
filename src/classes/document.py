class Document:
    def __init__(self, content):
        self.content = content
        self.findings = []

    def add_finding(self, finding):
        self.findings.append(finding)

    def get_finding_count(self):
        return len(self.findings)
    
    def get_severity_count(self,severity):
        count = 0
        for finding in self.findings:
            if finding.severity == severity:
                count += 1
        return count
    
    def get_risk_score(self):
        score = 0

        for finding in self.findings:
            if finding.severity == "High":
                score += 10
            elif finding.severity == "Medium":
                score += 5
            elif finding.severity == "Low":
                score += 1

        return score