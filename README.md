# Selenium PyTest Automation Framework

A portfolio-grade UI test automation framework built with Selenium WebDriver, 
PyTest, and Python using the Page Object Model (POM) design pattern.

## Tech Stack

- Python 3.11+
- Selenium WebDriver
- PyTest
- WebDriver Manager
- pytest-html (HTML reports)
- GitHub Actions (CI/CD)

## Project Structure
```
selenium-pytest-framework/
├── pages/              # Page Object classes
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/              # Test files
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_cart.py
├── reports/            # Generated HTML reports
├── .github/workflows/  # GitHub Actions CI pipeline
├── conftest.py         # PyTest fixtures (driver setup/teardown)
├── pytest.ini          # PyTest configuration
└── requirements.txt    # Dependencies
```

## Test Coverage

| Module | Tests |
|---|---|
| Login | 4 |
| Inventory | 6 |
| Cart | 5 |
| **Total** | **15** |

## Setup & Run

**1. Clone the repo**
```bash
git clone https://github.com/scariajanthomas/selenium-pytest-framework.git
cd selenium-pytest-framework
```

**2. Create virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run tests**
```bash
pytest
```

**5. View report**

Open `reports/report.html` in your browser after the run.

## CI/CD

Tests run automatically on every push to `main` via GitHub Actions.
HTML report is uploaded as a build artifact after each run.