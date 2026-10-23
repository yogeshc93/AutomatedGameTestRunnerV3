# Automated Game Test Runner V3

## 1. Overview

Automated Game Test Runner V3 is a Python-based project that executes test cases defined in a JSON file, performs calculations, compares actual results with expected results, and summarizes test outcomes.

The project demonstrates Python programming, JSON file handling, object-oriented programming, exception handling, automated testing with pytest, dependency management, and Git workflow practices.

## 2. Features

- Loads test cases from `test_cases.json`.
- Supports addition, subtraction, and multiplication.
- Compares actual results against expected results.
- Classifies outcomes as `PASS`, `FAIL`, or `ERROR`.
- Detects missing required fields in test cases.
- Handles unsupported operations.
- Displays totals for passed, failed, and errored test cases.
- Includes automated tests using pytest.

## 3. Project Structure

```text
AutomatedGameTestRunnerV3/
├── test_runner.py
├── test_case.py
├── test_report.py
├── test_cases.json
├── test_test_case.py
├── test_test_runner.py
├── pytest.ini
├── requirements.txt
├── .gitignore
├── GIT_WORKFLOW.md
├── Notes.txt
└── README.md
```

### File Descriptions

- `test_runner.py` — Loads JSON test cases, executes calculations, classifies outcomes, and prints a summary.
- `test_case.py` — Defines the `TestCase` class and calculation logic.
- `test_report.py` — Defines a class that stores a reference to a test case.
- `test_cases.json` — Contains sample test data.
- `test_test_case.py` — Tests calculation behavior and supported operations.
- `test_test_runner.py` — Checks whether the test runner executes without an uncaught exception.
- `pytest.ini` — Configures pytest test-file discovery.
- `requirements.txt` — Lists the pytest dependency.
- `.gitignore` — Excludes generated files and the local virtual environment.
- `GIT_WORKFLOW.md` — Documents basic Git commands and workflow.
- `Notes.txt` — Contains project learning notes.
- `README.md` — Provides project documentation and setup instructions.

## 4. Requirements

- Python 3.10 or newer.
- pip, the Python package installer.
- pytest, for running the automated test suite.

The project uses Python's built-in `json` module, so no separate installation is required for JSON processing.

## 5. Installation and Setup

### Step 1: Open the project directory

Open a terminal in the project directory.

### Step 2: Create a virtual environment

```powershell
python -m venv .venv
```

### Step 3: Activate the virtual environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 4: Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### Step 5: Verify the installation

```powershell
python -m pytest --version
```

## 6. Usage

### Run the test runner

Execute the sample test cases stored in `test_cases.json`:

```powershell
python test_runner.py
```

### Run the automated test suite

Execute the pytest tests:

```powershell
python -m pytest -v
```

The test runner and pytest serve different purposes. The runner processes the sample JSON test cases, while pytest executes the automated tests defined in the test files.

## 7. Sample Test Scenarios

The current `test_cases.json` contains five scenarios