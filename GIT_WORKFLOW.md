# Git Workflow — Automated Game Test Runner V3

## 1. Initialize Git
git init

## 2. Ignore unnecessary files
Created .gitignore to exclude:
- .venv/
- __pycache__/
.pytest_cache/
*.py[cod]

## 3. Check and stage files
git status
git add .
git status

## 4. Create a commit
git commit -m "Initial commit: Automated Game Test Runner"

## 5. Create a feature branch
git switch -c feature/add-test-description

## 6. Save a change
git add test_runner.py
git commit -m "Add test runner description"

## 7. Merge a branch
git switch master
git merge feature/add-test-description

## 8. Resolve a merge conflict
- Edit the conflicted file.
- Remove conflict markers by choosing the desired content.
- Run git add test_runner.py.
- Run git commit to complete the merge.

## 9. Inspect history and older code
git log --oneline
git show 2757863:test_runner.py

## 10. Check project status
git status