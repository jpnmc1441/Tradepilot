"""
TradePilot Settings Manager
---------------------------

Handles loading and saving application settings.
"""

import json
from pathlib import Path


class SettingsManager:
    """Loads and saves application settings."""

    def __init__(self):
        self.settings_file = Path("config/settings.json")
        self.settings = {}

    def load(self):
        """Load settings from JSON file."""

        if not self.settings_file.exists():
            self.create_default_settings()

        with open(self.settings_file, "r", encoding="utf-8") as file:
            self.settings = json.load(file)

        return self.settings

    def save(self):
        """Save settings to disk."""

        with open(self.settings_file, "w", encoding="utf-8") as file:
            json.dump(self.settings, file, indent=4)

    def create_default_settings(self):
        """Create default settings."""

        self.settings = {
            "application": {
                "name": "TradePilot",
                "version": "0.4.0"
            },
            "broker": {
                "provider": "tastytrade",
                "paperTrading": True
            },
            "theme": {
                "mode": "dark"
            },
            "risk": {
                "maxDailyLoss": 100,
                "maxOpenTrades": 5
            }
        }

        self.save()

    def get(self, section, key):
        return self.settings[section][key]

    def set(self, section, key, value):
        self.settings[section][key] = value
        self.save()
