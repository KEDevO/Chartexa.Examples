"""
views.py — Chartexa Pro generated Django views.

Edit data_adapter.py only — do not modify this file.
"""

from __future__ import annotations

import json
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from .data_adapter import DataAdapter

_adapter = DataAdapter()


def dashboard(request):
    html = render_to_string("dashboard.html")
    return HttpResponse(html, content_type="text/html")


def api_dashboard(request):
    return JsonResponse(_adapter.get_dashboard_payload())
