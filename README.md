# Selenium QA Automation Framework

## Project Overview
This project is an automated test framework built using Selenium and pytest.

The framework tests core functionality of the SauceDemo web application:
https://www.saucedemo.com/ 

The goal of this project is to demonstrate:
- Page Object Model (POM) structure 
- Explicit waits implementation
- Positive and negative test coverage 
- Clean framework design
- Git version control workflow

---

## Tech Stack

- Python
- Selenium WebDriver
- Page Object Model (POM)
- Git & GitHub

---

## Test Coverage 

Current automated scenarios include:

- Valid login
- Invalid login (negative test)
- Add to cart
- Checkout process

---

## Project Structure
Pages/ -> Page classes (POM)
tests/ -> Test cases
conftest.py -> Pytest fixtures
helpers.py -> Reusable methods

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

---

## Future Improvements 
- Data-driven testing 
- API validation tests
- HTML reporting
- CI/CD integration