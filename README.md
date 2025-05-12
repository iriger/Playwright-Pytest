# Playwright-Pytest Web Testing Framework

## Project Summary

This repository contains an automated testing framework for **https://automationexercise.com/** using Playwright with Pytest and Page Object Model (POM) design pattern. The project focuses on testing web application functionality including user registration, login, product filtering, search functionality, and other key features.

### Key Features:
- 🎭 **Playwright** 
- 🧪 **Pytest** as the testing framework
- 📄 **Page Object Model (POM)** for maintainable test code
- 📊 **Allure Reports** for detailed test reporting

## Requirements

### System Requirements:
- Python 3.13
- Git

### Python Dependencies:
- pytest
- playwright
- allure-pytest

## Installation

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd playwright-pytest
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Playwright
```bash
# Install Playwright
playwright install

# Install Playwright with dependencies
playwright install --with-deps
```

### 5. Install Allure (Optional - for report generation)
```bash
# Install Allure command line tool

# On Windows (using Scoop):
scoop install allure
```
## Running Tests

### Basic Test Execution

#### Run All Tests
```bash
# Run all tests with default configuration
pytest

# Run tests with verbose output
pytest -v

# Run tests in headed mode
pytest --headed
```
### Generate Allure Reports

#### During Test Execution
```bash
# Run tests and generate Allure results
pytest --alluredir=allure-results

# Run tests with clean Allure results
pytest --alluredir=allure-results --clean-alluredir
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request
