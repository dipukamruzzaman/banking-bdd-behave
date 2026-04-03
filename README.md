![Behave BDD Tests](https://github.com/dipukamruzzaman/banking-bdd-behave/actions/workflows/tests.yml/badge.svg)
# Banking API BDD Tests — Behave & Gherkin

A BDD test automation project for a Banking REST API using **Behave** and **Gherkin** syntax.
Demonstrates behaviour-driven development with plain English feature files readable by both
technical and non-technical stakeholders.

## Tech Stack

| Tool | Purpose |
|---|---|
| Behave | BDD test framework |
| Gherkin | Plain English test scenarios |
| FastAPI | Banking API backend |
| Requests | HTTP client for API calls |
| GitHub Actions | CI/CD pipeline |

## Project Structure
```
banking-bdd-behave/
│
├── app/
│   └── main.py                  # FastAPI banking API
│
├── features/
│   ├── auth.feature             # Login scenarios
│   ├── accounts.feature         # Account management scenarios
│   ├── transactions.feature     # Deposit & withdrawal scenarios
│   └── steps/
│       ├── auth_steps.py        # Step definitions for auth
│       ├── account_steps.py     # Step definitions for accounts
│       └── transaction_steps.py # Step definitions for transactions
│
└── requirements.txt
```

## How To Run

### 1. Clone the repository
```bash
git clone https://github.com/dipukamruzzaman/banking-bdd-behave.git
cd banking-bdd-behave
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the banking API
```bash
uvicorn app.main:app --reload
```

### 5. Run all BDD scenarios
```bash
behave features/
```

### 6. Run a single feature
```bash
behave features/auth.feature
```

## Key Concepts Demonstrated

- **Gherkin syntax** — Given/When/Then scenarios readable by non-developers
- **Feature files** — plain English descriptions of system behaviour
- **Step definitions** — Python functions that execute each Gherkin step
- **Context object** — shares state between steps within a scenario
- **BDD approach** — tests describe behaviour from the user's perspective

## Related Project

This project is the BDD counterpart to my Robot Framework test suite:
[banking-api-rf-tests](https://github.com/dipukamruzzaman/robot_framework_tests)

## Author

Md Kamruzzaman — [LinkedIn](www.linkedin.com/in/md-kamruzzaman-54507149) | [GitHub](https://github.com/dipukamruzzaman)