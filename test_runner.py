import json
from test_case import TestCase
from test_report import TestReport
# Automated Game Test Runner
# Runs test cases and reports PASS, FAIL, or ERROR.

if __name__ == "__main__":
    with open("test_cases.json", "r") as file:
        test_cases = json.load(file)

    tests_passed = 0
    tests_failed = 0
    tests_error = 0

    for data in test_cases:
        if "a" not in data or "b" not in data or "expected" not in data:
            print(data["test_name"], "Error Missing score")
            tests_error += 1
            continue

        test = TestCase(
            data["test_name"], 
            data["operation"], 
            data.get("a"), 
            data.get("b"), 
            data.get("expected"))

        report = TestReport(test)
        try:
            actual = report.test_case.calculate()

            if actual == report.test_case.expected:
                print(report.test_case.test_name, "PASS")
                tests_passed += 1
            else:
                print(report.test_case.test_name, "FAIL")
                tests_failed += 1

        except ValueError as e:
            print(report.test_case.test_name, "ERROR:", e)
            tests_error += 1

print(f"Tests Passed: {tests_passed}")
print(f"Tests Failed: {tests_failed}")
print(f"Tests Error: {tests_error}")
print("---")