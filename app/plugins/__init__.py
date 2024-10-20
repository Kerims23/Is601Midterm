# app/commands/__init__.py
from app.plugins.operations import Operations
from app.plugins.history import HistoryManager

class CommandHandler:
    def __init__(self):
        self.operations = Operations()
        # Only pass the filename to HistoryManager
        self.history_manager = HistoryManager("data/account.csv")  # Pass only the filename

    def execute_operation(self, operation_name, *args):
        """Execute a mathematical operation and return the result."""
        if operation_name == "add":
            return self.operations.add(*args)
        elif operation_name == "subtract":
            return self.operations.subtract(*args)
        elif operation_name == "multiply":
            return self.operations.multiply(*args)
        elif operation_name == "divide":
            return self.operations.divide(*args)
        else:
            raise ValueError(f"Unknown operation: {operation_name}")

    def save_history(self, data):  # Accept data to be saved
        """Save operation results to CSV."""
        self.history_manager.save(data)  # Pass data to history manager

    def load_history(self):
        """Load history from CSV."""
        return self.history_manager.load()

    def delete_history(self, index):
        """Delete a specific entry from history."""
        self.history_manager.delete(index)

    def clear_history(self):
        """Clear all entries from history."""
        self.history_manager.clear()
