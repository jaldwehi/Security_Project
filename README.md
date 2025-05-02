# Security Project – Vulnerable Login App

This project is part of the **SWE 481 - Software Security** course. It presents a simple login system built with Flask, designed to demonstrate common web security vulnerabilities for ethical testing.

---

## Technologies
- Python 3.11
- Flask
- SQLite3
- HTML + Bootstrap
- OWASP ZAP

---
## Features
- Vulnerable login form (no input validation)
- Login feedback message
- Database with sample user (admin / 1234)
---
## How to Run

1. Install Flask:
    ```bash
   pip install flask

2. Set up the database:
     python setup_db.py

3. Run the app:
      python run.py
4. Open: http://127.0.0.1:5000/
        Test login: admin / 1234

---

## Known Vulnerabilities
- SQL Injection
- No CSRF protection
- Missing security headers


