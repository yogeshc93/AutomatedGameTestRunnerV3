from test_report import TestReport

import pytest
from test_case import TestCase

@pytest.fixture
def addition_test_case():
    return TestCase("Addition Test", "add", 10, 5, 15)

@pytest.fixture
def subtraction_test_case():
    return TestCase("Subtraction Test", "subtract", 10, 5, 5)

@pytest.fixture
def multiplication_test_case():
    return TestCase("Multiplication Test", "multiply", 4, 5, 20)

def test_addition(addition_test_case):
    assert addition_test_case.calculate() == 15
   

def test_subtraction(subtraction_test_case):
    assert subtraction_test_case.calculate() == 5

def test_multiplication(multiplication_test_case):
    assert multiplication_test_case.calculate() == 20 

def test_addition_with_zero():
    test_case = TestCase("Zero Test", "add", 0, 0, 0)
    assert test_case.calculate() == 0

def test_addition_with_negative_numbers():
    test_case = TestCase("Negative Numbers Test", "add", -10, 5, -5)
    assert test_case.calculate() == -5

def test_unsupported_operation():
    test_case = TestCase("Unsupported Operation Test", "divide", 10, 5, None)

    with pytest.raises(ValueError):
        test_case.calculate()

def test_test_case_with_report():
    test_case = TestCase("Addition_Test", "add", 10, 5, 15)
    report = TestReport(test_case)

    assert report.test_case.test_name == "Addition_Test"
    assert report.test_case.calculate() == 15

@pytest.mark.parametrize("operation,a, b, expected", [
    ("add", 10, 5, 15),
    ("subtract", 10, 5, 5),
    ("multiply", 4, 5, 20)
])
def test_calculate(operation, a, b, expected):
    test_case = TestCase("Calculation Test", operation, a, b, expected)
    assert test_case.calculate() == expected