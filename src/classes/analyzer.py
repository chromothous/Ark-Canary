class Analyzer:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def analyze(self, document):
        for rule in self.rules:
            rule.evaluate(document)