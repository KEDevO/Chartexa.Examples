"""
main.py — Chartexa Pro generated FastAPI application.

Run
---
pip install fastapi uvicorn
uvicorn main:app --reload --port 5000

Then open http://127.0.0.1:5000
"""

from __future__ import annotations

from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from data_adapter import DataAdapter

app = FastAPI(title="BTC-USD Tactical View")
_adapter = DataAdapter()
_html = (Path(__file__).parent / "templates" / "dashboard.html").read_text(encoding="utf-8")


@app.get("/", response_class=HTMLResponse)
async def dashboard():
    return _html


@app.get("/api/dashboard")
async def api_dashboard():
    return JSONResponse(_adapter.get_dashboard_payload())
