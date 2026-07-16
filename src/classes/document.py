from constants.severity import HIGH, MEDIUM, LOW

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
    
    def get_category_count(self,category):
        count = 0
        for finding in self.findings:
            if finding.category == category:
                count += 1
        return count
    
    def get_highest_severity(self):
        if self.get_severity_count(HIGH) > 0:
            return HIGH
        if self.get_severity_count(MEDIUM) > 0:
            return MEDIUM
        if self.get_severity_count(LOW) > 0:
            return LOW
        return None
    
    def to_dict(self):
        return {
            "content": self.content,
            "finding_count": self.get_finding_count(),
            "risk_score": self.get_risk_score(),
            "findings": [finding.to_dict() for finding in self.findings]
        }