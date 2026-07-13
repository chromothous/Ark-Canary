from config import VERSION, APP_NAME

from classes.finding import Finding

from classes.document import Document

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
            "High",
            "Social Engineering"
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
            "High",
            "Social Engineering"
        )
        document.add_finding(finding)
        assert len(document.findings) == 1
        print(green("Version 0.0.4 online."))
        success += 1
    except Exception as e:
        print(red(e))
        print(red("Version 0.0.4 failed."))
        failure += 1

    if failure > 0:
        print(red(f"{failure} Failures detected, please fix."))
    else:
        print(green(f"All tests were successful! {success}/{tests}"))