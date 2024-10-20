import logging
import os
import pandas as pd
from app.commands import CommandHandler

class App:
    def __init__(self):
        self.command_handler = CommandHandler()  # Initialize the command handler
        self.last_result = None  # Initialize last result to None
        self.history_file = "data/account.csv"  # Path to the history file
        
        # Ensure the CSV file has headers
        if not os.path.exists(self.history_file) or os.path.getsize(self.history_file) == 0:
            self._initialize_csv_with_headers()
        
        logging.basicConfig(level=logging.INFO)
        logging.info("App initialized.")

    def _initialize_csv_with_headers(self):
        """Initialize the CSV with the required headers."""
        headers = ['index', 'name', 'operation', 'result']
        df = pd.DataFrame(columns=headers)  # Create an empty DataFrame with headers
        df.to_csv(self.history_file, index=False)  # Save it to the CSV file
        logging.info("Initialized CSV with headers: %s", headers)
        print("CSV initialized with headers.")

    def start(self):
        """Start the application."""
        name = input("Input your name: ")
        print(f"Hello, {name}! You can now perform operations.")
        
        while True:
            command = input("Enter a command (add, subtract, multiply, divide, save, load, delete, clear, exit): ").strip()
            
            if command == "exit":
                break
                
            if command in ["add", "subtract", "multiply", "divide"]:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = self.command_handler.execute_operation(command, num1, num2)
                print(f"Result: {result}")
                self.last_result = result  # Save only the last result

            elif command == "save":
                if self.last_result is not None:  # Check if there is a result to save
                    current_history = self.command_handler.load_history()
                    new_index = len(current_history)
                    self.command_handler.save_history({
                        "index": new_index,  # Placeholder index, actual index is handled by the history system
                        "name": name,
                        "operation": command,
                        "result": self.last_result,
                    })
                    logging.info("Saving history: %s", self.last_result)
                    print("History saved.")
                    self.last_result = None  # Reset after saving
                else:
                    print("No results to save. Please perform an operation first.")

            elif command == "load":
                history = self.command_handler.load_history()
                if history.empty:
                    logging.info("Loaded empty history.")
                    print("History is empty.")
                else:
                    logging.info("Loaded history: \n%s", history)
                    print("Loaded history:\n", history.to_string(index=False))  # Remove default index

            elif command == "delete":
                try:
                    index = int(input("Enter the index of the record to delete: "))
                    # Attempt to delete the history entry
                    self.command_handler.delete_history(index)
                except ValueError:
                    print("Error: Please enter a valid integer for the index.")
                except Exception as e:
                    print(f"Error: {str(e)}")
        
            elif command == "clear":
                self.command_handler.clear_history()
                logging.info("History cleared.")
