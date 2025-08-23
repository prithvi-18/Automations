# Selenium Capstone Project

## Overview
This project covers **Day 1 to Day 14** of Selenium learning:
- WebDriver basics
- Explicit waits
- POM (Page Object Model)
- Pytest fixtures
- Parallelization with xdist
- Selenium Grid
- GitHub Actions CI/CD
- Allure/HTML Reports
- Flaky test handling with retries + screenshots

## Run locally
```bash
pip install -r requirements.txt
pytest -v --html=artifacts/report.html --self-contained-html
```

## Run in parallel
```bash
pytest -n 2
```

## Run on CI
Push to GitHub → check Actions tab → download artifacts.
