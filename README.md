# Selenium + Pytest + Requests Automation Framework

## Project Overview

This project is a scalable UI and API automation framework built using Selenium, Pytest, and Python.

The framework follows the Page Object Model (POM) design pattern to seperate test logic from page elements, improving maintainability and readability.

The framework automates core functionality across multiple test applications such as: 

- SauceDemo
- OrangeHRM
- DemoQA
- HerokuApp

The goal of this project is to demonstrate:

- Clean automation framework architecture
- Reusable test components
- Reliable element handling using explicit waits
- Positive and negative test coverage 
- API testing integration
- Logging and failure debugging tools

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

--- 

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Requests (API Testing)
- Page Object Model (POM)
- Pytest Parametrize (Data-Driven Testing)
- Git & GitHub
 - pytest-html (Test Reporting)
 - Python logging module
 Addtional:
 - Explicit Waits (WebDriverWait, ExpectedConditions)
 - JSON Validation
 - REST API Testing
 - VS Code
 - HTML test reporting
 - Environment-based configuration
 - Structured logging

---

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

---

## Future Improvements 
- Data-driven testing 
- API validation tests
- HTML reporting
- CI/CD integration