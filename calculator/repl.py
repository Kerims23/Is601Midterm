'''repl.py'''
import logging
from calculator.operations import add, subtract, multiply, divide
from calculator.history import HistoryManager

class CalculatorREPL:
    def __init__(self):
        self.history = HistoryManager()
        self.commands = {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide,
            'history': self.history.show_history,
            'clear_history': self.history.clear_history,
            # Later, dynamically add plugins here
        }
        logging.basicConfig(filename='logs/app.log', level=logging.INFO)

    def run(self):
        print("Welcome to the Calculator REPL. Type 'exit' to quit.")
        while True:
            command = input("> ").strip().lower()
            if command == "exit":
                break
            self.execute_command(command)

    def execute_command(self, command):
        parts = command.split()
        if parts[0] in self.commands:
            try:
                if parts[0] == 'history' or parts[0] == 'clear_history':
                    self.commands[parts[0]]()
                else:
                    # Expecting operation followed by two numbers
                    result = self.commands[parts[0]](float(parts[1]), float(parts[2]))
                    print(f"Result: {result}")
                    self.history.add_to_history(parts[0], parts[1], parts[2], result)
            except Exception as e:
                logging.error(f"Error executing command {command}: {e}")
                print(f"Error: {e}")
        else:
            print(f"Unknown command: {command}")
