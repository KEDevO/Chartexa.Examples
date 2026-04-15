"""
app.py — Chartexa Pro generated Flask application.

Run
---
pip install flask
python app.py

Then open http://127.0.0.1:5000
"""

from __future__ import annotations

import os
from flask import Flask, jsonify, render_template_string, request
from data_adapter import DataAdapter

app = Flask(__name__)
_adapter = DataAdapter()


@app.get("/")
def dashboard():
    with open("templates/dashboard.html", encoding="utf-8") as f:
        return render_template_string(f.read())


@app.get("/api/dashboard")
def api_dashboard():
    return jsonify(_adapter.get_dashboard_payload())


if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "5000"))
    app.run(host=host, port=port, debug=False)
