from config import VERSION, APP_NAME

from constants.severity import LOW, MEDIUM, HIGH

from constants.severity_weights import SEVERITY_HIGH_WEIGHT, SEVERITY_MEDIUM_WEIGHT, SEVERITY_LOW_WEIGHT

from classes.finding import Finding

from classes.document import Document

from classes.rule import Rule

from classes.analyzer import Analyzer

def green(text):
    return f"\033[32m{text}\033[0m"

def red(text):
    return f"\033[31m{text}\033[0m"

success = 0
failure = 0
tests = 0

def full_test():
    global success, failure, tests

    try:
        tests += 1
        print(VERSION)
        print(APP_NAME)
        print(green("Version 0.0.2 online."))
        success += 1
    except Exception as e:
        print(red(e))
        print(red("Version 0.0.2 failed."))
        failure += 1
        
    try:
        tests += 1
        finding = Finding(
            "URGENT",
            "Urgency language detected",
            HIGH,
            "Social Engineering",
            0,
            0
        )
        print(finding.text)
        print(finding.reason)
        print(finding.severity)
        print(finding.category)
        print(green("Version 0.0.3 online."))
        success += 1
    except Exception as e:
        print(red(e))
        print(red("Version 0.0.3 failed."))
        failure += 1

    try:
        tests += 1
        document = Document(
            "URGENT: Verify your account immediately."
        )
        finding = Finding(
            "URGENT",
            "Urgency language detected",
            HIGH,
            "Social Engineering",
            0,
            0
        )
        document.add_finding(finding)
        assert len(document.findings) == 1
        print(green("Version 0.0.4 online."))
        success += 1
    except Exception as e:
        print(red(e))
        print(red("Version 0.0.4 failed."))
        failure += 1

    try:
        tests += 1
        rule = Rule(
            "Urgency Rule",
            "Detects urgency language",
            HIGH,
            "URGENT",
            "PHISHING"
        )
        print(rule.name)
        print(rule.description)
        print(rule.severity)
        success += 1
        print(green("Version 0.0.5 online."))
    except Exception as e:
        print(red(e))
        print(red("Version 0.0.5 failed."))
        failure += 1

    try:
        tests += 1
        document = Document(
            "URGENT: Verify your account immediately."
        )
        rule = Rule(
            "Urgency Rule",
            "Urgency language detected",
            HIGH,
            "URGENT",
            "PHISHING"
        )
        before = len(document.findings)
        rule.evaluate(document)
        after = len(document.findings)
        assert before == 0
        assert after == 1
        print(green("Version 0.0.6 online."))
        success += 1
    except Exception as e:
        print(red(e))
        print(red("Version 0.0.6 failed."))
        failure += 1

    try:
        tests += 1
        document = Document(
            "URGENT: Verify your account immediately."
        )
        rule = Rule(
            "Urgency Rule",
            "Urgency language detected",
            HIGH,
            "URGENT",
            "PHISHING"
        )
        rule.evaluate(document)
        assert len(document.findings) == 1
        finding = document.findings[0]
        assert finding.text == "URGENT"
        assert finding.reason == "Urgency language detected"
        assert finding.severity == "High"
        assert finding.category == "PHISHING"
        assert finding.start_index == 0
        assert finding.end_index == 6
        print(green("Version 0.0.7 online."))
        success += 1
    except Exception as e:
        print(red(e))
        print(red("Version 0.0.7 failed."))
        failure += 1

    try:
        tests += 1
        urgency_rule = Rule(
            "Urgency Rule",
            "Urgency language detected",
            HIGH,
            "URGENT",
            "PHISHING"
        )
        verify_rule = Rule(
            "Verification Rule",
            "Verification request detected",
            MEDIUM,
            "VERIFY",
            "PHISHING"
        )
        document = Document(
            "URGENT: Verify your account immediately."
        )
        urgency_rule.evaluate(document)
        verify_rule.evaluate(document)
        assert len(document.findings) == 2
        print(green("Version 0.0.8 is online."))
        success += 1
    except Exception as e:
        print(red(e))
        print(red("Version 0.0.8 failed."))
        failure += 1

    try:
        tests += 1
        document = Document(
            "URGENT: Verify your account immediately."
        )
        analyzer = Analyzer()
        analyzer.add_rule(
            Rule(
                "Urgency Rule",
                "Urgency language detected",
                HIGH,
                "URGENT",
                "PHISHING"
            )
        )
        analyzer.add_rule(
            Rule(
                "Verification Rule",
                "Verification request detected",
                MEDIUM,
                "VERIFY",
                "PHISHING"
            )
        )
        analyzer.analyze(document)
        assert len(document.findings) == 2
        print(green("Version 0.0.9 is online."))
        success += 1
    except Exception as e:
        print(red(e))
        print(red("Version 0.0.9 failed."))
        failure += 1

    try:
        tests += 1
        document = Document(
            "URGENT: Verify your account immediately."
        )
        analyzer = Analyzer()
        analyzer.add_rule(
            Rule(
                "Urgency Rule",
                "Urgency language detected",
                HIGH,
                "URGENT",
                "PHISHING"
            )
        )
        analyzer.add_rule(
            Rule(
                "Verification Rule",
                "Verification request detected",
                MEDIUM,
                "VERIFY",
                "PHISHING"
            )
        )
        analyzer.analyze(document)
        assert len(document.findings) == 2
        assert document.findings[0].text == "URGENT"
        assert document.findings[0].severity == "High"
        assert document.findings[1].text == "Verify"
        assert document.findings[1].severity == "Medium"
        for finding in document.findings:
            print(f"Text: {finding.text}")
            print(f"Reason: {finding.reason}")
            print(f"Severity: {finding.severity}")
            print(f"Category: {finding.category}")
            print(f"Start: {finding.start_index}")
            print(f"End: {finding.end_index}")
            print()
        print(green("Version 0.1.0 is online."))
        success += 1
    except Exception as e:
        print(red(e))
        print(red("Version 0.1.0 failed."))
        failure += 1

    try:
        tests += 1
        document = Document(
            "URGENT URGENT URGENT"
        )
        analyzer = Analyzer()
        analyzer.add_rule(
            Rule(
                "Urgency Rule",
                "Urgency language detected",
                HIGH,
                "URGENT",
                "PHISHING"
            )
        )
        analyzer.analyze(document)
        assert len(document.findings) == 3
        assert document.findings[0].start_index == 0
        assert document.findings[1].start_index == 7
        assert document.findings[2].start_index == 14
        print(green("Version 0.1.1 is online."))
        success += 1
    except Exception as e:
        print(red(e))
        print(red("Version 0.1.1 failed."))
        failure += 1

    try:
        tests += 1
        document = Document("URGENT: Verify your account.")
        analyzer = Analyzer()
        urgency_rule = Rule("Urgency Rule","Urgency language detected",HIGH,"URGENT","Social Engineering")
        verify_rule = Rule("Verification Rule","Verification request detected",MEDIUM,"Verify","Credential Theft")
        analyzer.add_rule(urgency_rule)
        analyzer.add_rule(verify_rule)
        analyzer.analyze(document)
        assert len(document.findings) == 2
        assert document.findings[0].text == "URGENT"
        assert document.findings[0].category == "Social Engineering"
        assert document.findings[0].severity == HIGH
        assert document.findings[1].text == "Verify"
        assert document.findings[1].category == "Credential Theft"
        assert document.findings[1].severity == MEDIUM
        for finding in document.findings:
            print(f"Text: {finding.text}")
            print(f"Reason: {finding.reason}")
            print(f"Severity: {finding.severity}")
            print(f"Category: {finding.category}")
            print(f"Start: {finding.start_index}")
            print(f"End: {finding.end_index}")
        print(green("Version 0.1.2 is online."))
        success += 1
    except Exception as e:
        print(red(e))
        print(red("Version 0.1.2 failed."))
        failure += 1

    try:
        tests += 1
        document = Document("URGENT")
        analyzer = Analyzer()
        rule = Rule(
            "Urgency Rule",
            "Urgency language detected",
            HIGH,
            "URGENT",
            "PHISHING"
        )
        analyzer.add_rule(rule)
        analyzer.analyze(document)
        assert document.findings[0].severity == HIGH
        print(green("Version 0.1.3 is online."))
        success += 1
    except Exception as e:
        print(red(e))
        print(red("Version 0.1.3 failed."))
        failure += 1

    try:
        tests += 1
        document = Document("Urgent: Verify your account.")
        analyzer = Analyzer()
        rule = Rule("Urgency Rule","Urgency language detected",HIGH,"URGENT","PHISHING")
        analyzer.add_rule(rule)
        analyzer.analyze(document)
        assert len(document.findings) == 1
        assert document.findings[0].text == "Urgent"
        print(green("Version 0.1.4 is online."))
        success += 1
    except Exception as e:
        print(red(e))
        print(red("Version 0.1.4 failed."))
        failure += 1

    try:
        tests += 1
        document = Document("URGENT: Verify your account.")
        analyzer = Analyzer()
        analyzer.add_rule(Rule("Urgency Rule","Urgency language detected",HIGH,"URGENT","PHISHING"))
        analyzer.add_rule(Rule("Verification Rule","Verification request detected",MEDIUM,"VERIFY","CREDENTIAL_THEFT"))
        analyzer.analyze(document)
        assert document.get_finding_count() == 2
        print(green("Version 0.1.5 is online."))
        success += 1
    except Exception as e:
        print(red(e))
        print(red("Version 0.1.5 failed."))
        failure += 1

    try:
        tests += 1
        document = Document("URGENT VERIFY")
        analyzer = Analyzer()
        analyzer.add_rule(Rule("Urgency Rule","Urgency language detected",HIGH,"URGENT","PHISHING"))
        analyzer.add_rule(Rule("Verification Rule","Verification request detected",MEDIUM,"VERIFY","CREDENTIAL_THEFT"))
        analyzer.analyze(document)
        assert document.get_finding_count() == 2
        assert document.get_severity_count(HIGH) == 1
        assert document.get_severity_count(MEDIUM) == 1
        assert document.get_severity_count(LOW) == 0
        print(green("Version 0.1.6 is online."))
        success += 1
    except Exception as e:
        print(red(e))
        print(red("Version 0.1.6 failed."))
        failure += 1

    try:
        tests += 1
        document = Document("URGENT VERIFY")
        analyzer = Analyzer()
        analyzer.add_rule(Rule("Urgency Rule","Urgency language detected",HIGH,"URGENT","PHISHING"))
        analyzer.add_rule(Rule("Verification Rule","Verification request detected",MEDIUM,"VERIFY","CREDENTIAL_THEFT"))
        analyzer.analyze(document)
        assert document.get_risk_score() == 15
        print(green("Version 0.1.7 is online."))
        success += 1
    except Exception as e:
        print(red(e))
        print(red("Version 0.1.7 failed."))
        failure += 1

    try:
        tests += 1
        document = Document("URGENT VERIFY")
        analyzer = Analyzer()
        analyzer.add_rule(Rule("Urgency Rule","Urgency language detected",HIGH,"URGENT","PHISHING"))
        analyzer.add_rule(Rule("Verification Rule","Verification request detected",MEDIUM,"VERIFY","CREDENTIAL_THEFT"))
        analyzer.analyze(document)
        assert document.get_category_count("PHISHING") == 1
        assert document.get_category_count("CREDENTIAL_THEFT") == 1
        assert document.get_category_count("ATTACHMENTS") == 0
        print(green("Version 0.1.8 is online."))
        success += 1
    except Exception as e:
        print(red(e))
        print(red("Version 0.1.8 failed."))
        failure += 1

    try:
        tests += 1
        document = Document("URGENT VERIFY")
        analyzer = Analyzer()
        analyzer.add_rule(Rule("Urgency Rule","Urgency language detected",HIGH,"URGENT","PHISHING"))
        analyzer.add_rule(Rule("Verification Rule","Verification request detected",MEDIUM,"VERIFY","CREDENTIAL_THEFT"))
        analyzer.analyze(document)
        assert document.get_highest_severity() == HIGH
        print(green("Version 0.1.9 is online."))
        success += 1
    except Exception as e:
        print(red(e))
        print(red("Version 0.1.9 failed."))
        failure += 1

    try:
        tests += 1
        document = Document("URGENT")
        analyzer = Analyzer()
        analyzer.add_rule(Rule("Urgency Rule","Urgency language detected",HIGH,"URGENT","PHISHING"))
        analyzer.analyze(document)
        finding = document.findings[0]
        data = finding.to_dict()
        assert data["text"] == "URGENT"
        assert data["reason"] == "Urgency language detected"
        assert data["severity"] == HIGH
        assert data["category"] == "PHISHING"
        assert data["start_index"] == 0
        assert data["end_index"] == 6
        print(green("Version 0.1.10 is online."))
        success += 1
    except Exception as e:
        print(red(e))
        print(red("Version 0.1.10 failed."))
        failure += 1

    try:
        tests += 1
        document = Document("URGENT")
        analyzer = Analyzer()
        analyzer.add_rule(Rule("Urgency Rule","Urgency language detected",HIGH,"URGENT","PHISHING"))
        analyzer.analyze(document)
        data = document.to_dict()
        assert data["content"] == "URGENT"
        assert data["finding_count"] == 1
        assert data["risk_score"] == 10
        assert len(data["findings"]) == 1
        assert data["findings"][0]["text"] == "URGENT"
        print(green("Version 0.1.11 is online."))
        success += 1
    except Exception as e:
        print(red(e))
        print("Version 0.1.11 failed.")
        failure += 1

    try:
        tests += 1
        document = Document("URGENT")
        analyzer = Analyzer()
        analyzer.add_rule(Rule("Urgency Rule","Urgency language detected",HIGH,"URGENT","PHISHING"))
        analyzer.analyze(document)
        finding = document.findings[0]
        data = finding.to_json()
        assert '"text": "URGENT"' in data
        assert '"category": "PHISHING"' in data
        print(green("Version 0.1.12 is online."))
        success += 1
    except Exception as e:
        print(red(e))
        print(red("Version 0.1.12 failed."))
        failure += 1

    if failure > 0:
        print(red(f"{failure} Failures detected, please fix."))
    else:
        print(green(f"All tests were successful! {success}/{tests}"))