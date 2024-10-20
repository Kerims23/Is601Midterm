# app/commands/history.py
import pandas as pd
import os

class HistoryManager:
    def __init__(self, filename):
        self.filename = filename
    
    def save(self, data):
        """Save operation results to CSV."""
        df = pd.DataFrame([data], columns=['index', 'name', 'operation', 'result'])
        
        file_exists = os.path.exists(self.filename)
        
        # If file doesn't exist, create it and append the blank line
        if not file_exists:
            with open(self.filename, mode='w') as file:
                file.write('\n')

        # Append data
        df.to_csv(self.filename, mode='a', index=False, header=not file_exists)

    def load(self):
        """Load history from CSV."""
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            try:
                df = pd.read_csv(self.filename)
                if df.empty:
                    return pd.DataFrame(columns=['index', 'name', 'operation', 'result'])
                return df
            except pd.errors.EmptyDataError:
                return pd.DataFrame(columns=['index', 'name', 'operation', 'result'])
        return pd.DataFrame(columns=['index', 'name', 'operation', 'result'])

    def delete(self, index):
        """Delete a specific entry from history."""
        df = self.load()  # Load the existing history
        if df.empty:
            print("Error: No records found in history to delete.")
            return

        print("Current history before deletion:")
        print(df)  # Debug print to see current history

        if index < 0 or index >= len(df):
            print(f"Error: Index {index} is out of bounds. Provide a valid index.")
            return
        
        df = df.drop(index)  # Drop the specified index
        df.to_csv(self.filename, index=False)  # Save back to CSV
        
        print("Record deleted.")
        print("Updated history after deletion:")
        print(df)  # Debug print to see updated history


    def clear(self):
        """Clear all history by deleting the file."""
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print("History cleared.")
        else:
            print("No history file found.")
