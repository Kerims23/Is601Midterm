import pandas as pd
import os

class HistoryManager:
    def __init__(self, filename, operations):
        self.filename = filename
        self.operations = operations  # Store the operations reference

    def save(self, data):
        """Save operation results to CSV."""
        df = pd.DataFrame([data])  # Create a DataFrame from the data
        # Append to the CSV, ensure no index is created
        df.to_csv(self.filename, mode='a', index=False, header=not os.path.exists(self.filename))

    def load(self):
        """Load history from CSV."""
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            return pd.read_csv(self.filename)
        else:
            return pd.DataFrame(columns=['name', 'operation', 'result'])  
        
    def delete(self, index):
        """Delete a specific entry from history."""
        df = self.load()
        df = df.drop(index)  # Drop the specified index
        df.to_csv(self.filename, index=False)  # Save back to CSV

    def clear(self):
        """Clear all entries from history."""
        open(self.filename, 'w').close()  # Clear the file
