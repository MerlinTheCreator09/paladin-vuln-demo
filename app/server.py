"""
INTENTIONALLY VULNERABLE demo app -- a test fixture for the Paladin scanner.
Do not deploy. Every credential below is a fake, obvious placeholder.
"""
import os
import sqlite3

from flask import Flask, request

app = Flask(__name__)

# CWE-798: hard-coded credentials (fake placeholder values, not real)
API_KEY = "EXAMPLE_FAKE_API_KEY_0000"
DB_PASSWORD = "EXAMPLE_FAKE_PASSWORD_0000"


@app.route("/user")
def get_user():
    uid = request.args.get("id", "")
    conn = sqlite3.connect("app.db")
    # CWE-89: SQL assembled by string concatenation from user input
    conn.execute("SELECT * FROM users WHERE id = " + uid)
    return "ok"


@app.route("/calc")
def calc():
    expr = request.args.get("expr", "")
    # CWE-95: evaluates attacker-controlled input as code
    return str(eval(expr))


@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    # CWE-78: OS command built from user input and run through the shell
    os.system("ping -c 1 " + host)
    return "ok"


if __name__ == "__main__":
    # CWE-489: debug mode left enabled
    app.run(debug=True)
