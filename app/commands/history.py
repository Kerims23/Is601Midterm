# app/commands/history.py
import pandas as pd
import os

class HistoryManager:
    def __init__(self, filename):
        self.filename = filename
    
    def save(self, data):
        """Save operation results to CSV with a blank line at the top."""
        df = pd.DataFrame([data], columns=['index', 'name', 'operation', 'result'])  # Specify columns

        # Check if the file exists
        file_exists = os.path.exists(self.filename)
        
        # If the file doesn't exist, create it and write a blank line
        if not file_exists:
            with open(self.filename, mode='w') as file:
                file.write('\n')  # Write a blank line

        # Now append the actual data
        df.to_csv(self.filename, mode='a', index=False, header=not file_exists)

    def load(self):
        """Load history from CSV."""
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            try:
                df = pd.read_csv(self.filename)
                if df.empty:
                    print("History is empty.")
                    return pd.DataFrame(columns=['index', 'name', 'operation', 'result'])
                else:
                    return df
            except pd.errors.EmptyDataError:
                print("CSV file is empty.")
                return pd.DataFrame(columns=['index', 'name', 'operation', 'result'])
        else:
            print("History is empty.")
            return pd.DataFrame(columns=['index', 'name', 'operation', 'result'])


    def delete(self, index):
        """Delete a specific entry from history."""
        df = self.load()
        # Check if the DataFrame is empty
        if df.empty:
            print("Error: No records found in history to delete.")
            return
        # Reset the index to ensure it matches the row positions
        df = df.reset_index(drop=True)
        # Check if the provided index is valid
        if index < 0 or index >= len(df):
            print(f"Error: Index {index} is out of bounds. Please provide a valid index.")
            return  # Exit the method early if the index is invalid
        # Drop the specified index
        df = df.drop(index)
        # Save back to CSV
        df.to_csv(self.filename, index=False)
        print("Record deleted.")

    def clear(self):
            """Clear all entries from history by deleting the file."""
            if os.path.exists(self.filename):  # Check if the file exists
                os.remove(self.filename)  # Delete the file
                print("History file deleted.")
            else:
                print("No history file found to delete.")
                