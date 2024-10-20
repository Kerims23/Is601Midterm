'''app/__init__.py'''
import logging
import os
import pandas as pd
from dotenv import load_dotenv
from app.plugins import CommandHandler

# Load environment variables
load_dotenv()

# Get log level and file path from environment variables
ENVIRONMENT = os.getenv("ENVIRONMENT", "production") 
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")

# Create the logs directory if it doesn't exist
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Configure logging
logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

class App:
    def __init__(self):
        '''init app'''
        self.command_handler = CommandHandler()  # Initialize the command handler
        self.last_result = None  # Initialize last result to None
        self.history_file = os.getenv("HISTORY_FILE", "data/account.csv")  # Get history file path from env
        
        # Ensure the CSV file has headers
        if not os.path.exists(self.history_file) or os.path.getsize(self.history_file) == 0:
            self._initialize_csv_with_headers()

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
        logging.info("App started.")
        name = input("Input your name: ")
        print(f"Hello, {name}! You can now perform operations.")
        logging.info(f"{name} is in application")
        while True:
            command = input("Enter a command (add, subtract, multiply, divide, save, load, delete, clear, exit): ").strip()
            if command == "exit":
                logging.info(f"{command} exiting app")
                break
            if command in ["add", "subtract", "multiply", "divide"]:
                logging.info(f"{command} is an operation")
                num1 = float(input("Enter first number: "))
                logging.info(f"{num1}")
                num2 = float(input("Enter second number: "))
                logging.info(f"{num2}")
                result = self.command_handler.execute_operation(command, num1, num2)
                logging.info(f"{result}")
                print(f"Result: {result}")
                self.last_result = result
            elif command == "save":
                logging.info(f"{command} is a save")
                if self.last_result is not None:
                    current_history = self.command_handler.load_history()
                    new_index = len(current_history)
                    self.command_handler.save_history({
                        "index": new_index,  
                        "name": name,
                        "operation": command,
                        "result": self.last_result,
                    })
                    logging.info("Saving history: %s", self.last_result)
                    print("History saved.")
                    self.last_result = None
                else:
                    logging.info(f"{command}No results to save. Need operation")
                    print("No results to save. Please perform an operation first.")
            elif command == "load":
                logging.info(f"{command} is a load")
                history = self.command_handler.load_history()
                if history.empty:
                    logging.info("Loaded empty history.")
                    print("History is empty.")
                else:
                    logging.info("Loaded history: \n%s", history)
                    print("Loaded history:\n", history.to_string(index=False)) 
            elif command == "delete":
                logging.info(f"{command} is a delete")
                try:
                    logging.info(f"{command} trying delete")                    
                    index = int(input("Enter the index of the record to delete: "))
                    self.command_handler.delete_history(index)
                except ValueError:
                    logging.info(f"{command} not in index")
                    print("Error: Please enter a valid integer for the index.")
                except Exception as e:
                    print(f"Error: {str(e)}")        
            elif command == "clear":
                logging.info(f"{command} is a clear")
                self.command_handler.clear_history()
                logging.info("History cleared.")
