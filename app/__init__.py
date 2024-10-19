# app/__init__.py
import logging
from app.commands import CommandHandler

class App:
    def __init__(self):
        self.command_handler = CommandHandler()  # Initialize the command handler
        self.last_result = None  # Initialize last result to keep track of it
        logging.basicConfig(level=logging.INFO)
        logging.info("App initialized.")

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
                self.last_result = result  # Save the last result for future reference

            elif command == "save":
                if self.last_result is not None:
                    # Load current history to determine the new index
                    history = self.command_handler.load_history()
                    index = len(history)  # The new index will be the length of the history
                    # Save the last operation result to history, including the index
                    self.command_handler.save_history({
                        "index": index,  # Include index in the same row
                        "name": name,
                        "operation": command,
                        "result": self.last_result,
                    })
                    print("History saved.")
                else:
                    print("No result to save. Please perform an operation first.")

            elif command == "load":
                history = self.command_handler.load_history()
                # Display the history with indices included
                print("Loaded history:\n", history.to_string(index=False))  # Remove default index

            elif command == "delete":
                index = int(input("Enter the index of the record to delete: "))
                self.command_handler.delete_history(index)
                print("Record deleted.")
            
            elif command == "clear":
                self.command_handler.clear_history()
                print("History cleared.")
