# plugins/greet/__init__.py
import logging
from app.commands import Command

class GreetCommand(Command):
    def execute(self):
        print("Hello, World!")
        logging.info("GreetCommand executed: Hello, World!")
