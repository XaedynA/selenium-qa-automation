# Selenium QA Automation — Helpdesk regression lab

![Quality checks](https://github.com/XaedynA/selenium-qa-automation/actions/workflows/tests.yml/badge.svg)

A repeatable Selenium + pytest suite for a small, local helpdesk ticket workflow. Demonstrates page objects, positive and negative cases, data-driven tests, explicit waits, isolated browser sessions, failure screenshots, and CI evidence for QA and IT-support roles.

## Quick start

Install Python 3.12+ and Chrome, then:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -v --html=report.html --self-contained-html
```

Headless Chrome is the default. Use `HEADLESS=0` for visible execution. Selenium Manager obtains a compatible driver (network needed on first use). For preinstalled/offline tools, set `CHROME_BINARY` and `CHROMEDRIVER` to their executable paths. `CHROME_NO_SANDBOX=1` is only for an isolated container that requires it; normal runs preserve Chrome's sandbox.

## Test plan

| Case | Expected result |
| --- | --- |
| Create Normal/High priority tickets | Correct summary and priority, success status |
| Empty/whitespace summary | No ticket created |
| Case-insensitive search | Matching rows only; clearing restores all |
| Reset | Removes all tickets |
| HTML-like input | Displays as text; no executable markup |
| Overlong summary | Browser enforces 120-character limit |

`fixtures/helpdesk.html` is a deliberately small synthetic application, not a production helpdesk. Each test gets a fresh browser, so tests do not depend on order. The page object in `pages/helpdesk.py` centralizes interactions without hiding assertions. There are no hard-coded sleep calls.

## Optional external smoke tests

The original example.com checks remain available:

```bash
python -m pytest --external -v
```

These depend on internet access and an external site's uptime. Default CI runs only the local regression suite. Three external cases are reported as skipped in default runs.

## CI and failure evidence

GitHub Actions runs on pushes, pull requests, and manual dispatch with a 10-minute timeout and read-only repository permissions. Every run uploads HTML/JUnit reports; failing browser cases capture PNG screenshots in `artifacts/`. Artifacts expire after 14 days. Do not point screenshot-enabled tests at sensitive production data.

For a failure, open the HTML report, inspect the screenshot, reproduce the exact case, then determine whether the problem is an assertion, fixture behavior, or browser setup. A driver startup failure is not a passing test. The fixture always quits an initialized browser even after a failed test.
