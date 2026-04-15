"""
data_adapter.py — Chartexa Pro generated stub.

INSTRUCTIONS
============
This is the ONLY file you need to edit.

Implement ``DataAdapter.get_dashboard_payload()`` so that it returns
a dict matching the schema documented below.  Everything else
(HTTP server, routing, HTML, JS polling) is already wired for you.

Payload schema
--------------
{
    "status": "ok",
    "clock":  "YYYY-MM-DD HH:MM:SS",
    "series": {
        "<panel_id>": {
            # For line / stepped_line / bar:
            "type": "line",
            "data": [
                {"name": "Device A", "points": [{"x": "ISO-timestamp", "y": 42.0}]}
            ]
        },
        "<panel_id>": {
            # For heatmap:
            "type": "heatmap",
            "devices":     ["Dev A", "Dev B"],
            "time_labels": ["13:00", "14:00"],
            "matrix":      [[108, 112], [0, 100]],
            "min": 0, "max": 120
        },
        "<panel_id>": {
            # For digital (binary 0/1):
            "type": "digital",
            "points": [{"x": "ISO-timestamp", "y": 1}]
        },
    },
    "cards": {
        "<card_id>": "any string value displayed on the card"
    },
    "events": [
        "14:30:00  Device A  LQ 108",
    ]
}
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

# Panel IDs in this dashboard:
        # (no chart panels)

# Stat card IDs in this dashboard:
        # (no stat cards)


class DataAdapter:
    """
    Connect this class to your data source.

    The simplest approach is to instantiate a background thread here
    (or an asyncio task for FastAPI) that tails a log file / reads from
    an MQTT broker / queries a database, and stores the latest state
    in instance variables.  Then read those variables in
    ``get_dashboard_payload()``.
    """

    def __init__(self) -> None:
        # TODO: initialise your data source here
        pass

    def get_dashboard_payload(self) -> dict[str, Any]:
        """Return the payload dict that the frontend JavaScript consumes."""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "status": "ok",
            "clock":  now,
            "series": {

            },
            "cards": {},
            "events": [],
        }
