"""
TradePilot Logger
"""

import logging
from pathlib import Path


class Logger:

    def __init__(self):

        Path("logs").mkdir(exist_ok=True)

        logging.basicConfig(
            filename="logs/tradepilot.log",
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
        )

        self.logger = logging.getLogger("TradePilot")

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)
