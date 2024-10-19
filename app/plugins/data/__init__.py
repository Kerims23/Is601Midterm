# plugins/data/__init__.py
import logging
from app.commands import Command

class DataCommand(Command):
    def execute(self):
        # Example data handling and logging
        logging.info("DataCommand executed with sample data.")
        print("Executing data command with sample data")
