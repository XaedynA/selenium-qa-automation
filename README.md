# Selenium QA Automation Portfolio

A beginner-friendly Python test automation project demonstrating Selenium WebDriver, pytest, explicit waits, assertions, reusable browser fixtures, and GitHub Actions CI.

## What it tests

Three browser tests on the public demonstration page [example.com](https://example.com):

1. Verifies the page title.
2. Checks that the main heading is visible and correct.
3. Verifies the More information link points to IANA.

## Tech stack

- Python 3.12+
- Selenium WebDriver 4
- pytest
- pytest-html
- GitHub Actions (headless Chrome)

## Run locally

Install Python and Google Chrome, then in the project folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
pytest -v --html=report.html --self-contained-html
```

For headless execution:

```bash
HEADLESS=1 pytest -v
```

Selenium Manager normally handles the ChromeDriver download automatically. Internet access may be required for the first run.

## CI

The GitHub Actions workflow runs the tests on pushes, pull requests, and manual dispatch. The generated HTML report is uploaded as an artifact. Look under the **Actions** tab for results.

## Learning goals

This portfolio sample demonstrates how to structure repeatable automated UI tests. The tests use a public sample website and do not exercise authentication or production systems.

## Status

Starter project prepared for local and CI execution. **Tests have not been executed in this packaging environment.** Check the Actions tab after publishing to confirm they pass.

## Interview talking points

Explain why explicit waits reduce flaky tests, why browser setup is handled by a pytest fixture, what assertions verify, and how headless tests run in CI. Review and run the tests yourself before describing the project as your own practical experience.
