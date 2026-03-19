# Selenium + Pytest + Requests Automation Framework

[![Selenium Test Pipeline](https://github.com/Fernando-Rubio/selenium-qa-framework/actions/workflows/tests.yml/badge.svg)](https://github.com/Fernando-Rubio/selenium-qa-framework/actions/workflows/tests.yml)

A scalable Selenium automation framework demostrating Page Object Model design, Pytest execution, and CI integration using GitHub Actions.

## Project Overview

This project is a scalable UI and API automation framework built using Selenium, Pytest, and Python.

The framework follows the Page Object Model (POM) design pattern to seperate test logic from page elements, improving maintainability and readability.

The framework automates core functionality test within: 

- SauceDemo

And addtional tests in: 

- OrangeHRM
- DemoQA
- HerokuApp

The goal of this project is to demonstrate:

- Clean automation framework architecture
- Reusable test components
- Reliable element handling using explicit waits
- Positive and negative test coverage 
- UI and API testing integration
- Logging and failure debugging tools
- CI-compatible test execution 
---

## Framework Features 
- Page Object Model (POM) design pattern
- Reusable BasePage class for common Selenium actions
- Explicit waits for reliable element interaction
- Pytest fixtures for browser setup and teardown
- Data-driven testing using pytest parametrize
- Screenshot capture on test failures 
- Structured logging for debugging
- HTML test reporting using pytest-html
- API testing using Python Requests
- Enviorment-based configuration
- Continuous Intergration using GitHub Actions (CI pipeline)

---

## Core Automation Utilities 
- Element click handling 
- Input field typing
- Explicit wait handling
- URL synchronization
- Page navigation helpers

--- 

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Requests (API Testing)
- Page Object Model (POM)
- Pytest Parametrize (Data-Driven Testing)
- Git & GitHub
- GitHub Actions (CI/CD)
 - pytest-html (Test Reporting)
 - Python logging module
 
 Addtional Tools & Concepts:
 - Explicit Waits (WebDriverWait, ExpectedConditions)
 - JSON Validation
 - REST API Testing
 - VS Code
 - HTML test reporting
 - Environment-based configuration
 - Structured logging

---

## CI Pipeline 

This project uses GitHub Actions to automatically execute the test suite on every push.

Pipeline workflow includes:

- Environment setup
- Dependency installation
- Headless browser execution
- Automated Pytest test runs
- Failure detection and reporting

## Example Automated Tests

UI Tests
- Login functionality
- Invalid login scenarios
- Add item to cart
- Navigation validation

API Tests
- Requests library
- Parametrize login tests
- JSON response validation
- API client abstraction layer
- GET request validation
- response status verification

---

## Test Coverage 

Current automated scenarios include:

- Valid login
- Invalid login (negative test)
- Add to cart
- Checkout process

---

## Project Structure

qa_project/

pages/ -> Page Object classes
tests/ -> Test cases
api/ -> API client tests
utils/ -> Helper utilities
config/ -> Environment settings
screenshots/ -> Failure screenshots
conftest.py/ -> Pytest fixtures
pytest.ini/ -> Pytest configuration

---

## > How To Run Tests
1. Clone the repository
git clone https://github.com/Fernando-Rubio/selenium-qa-framework.git

2. Navigate into project:
cd selenium-qa-framework 

3. Install dependencies:
pip install -r requirements.txt

4. Run tests:
pytest -v

5. Generate HTML report:
pytest --html=report.html 