# plugins/data.py
import pandas as pd
import os

class DataManager:
    def __init__(self, filename='data/account.csv'):
        self.filename = filename

    def save(self, history_data):
        """Save current history data to a CSV file."""
        df = pd.DataFrame(history_data)
        if os.path.isfile(self.filename):
            df.to_csv(self.filename, mode='a', header=False, index=False)
        else:
            df.to_csv(self.filename, index=False)

    def load(self):
        """Load history data from a CSV file."""
        if os.path.isfile(self.filename):
            return pd.read_csv(self.filename)
        else:
            return pd.DataFrame()

    def delete_record(self, index):
        """Delete a record by index from the CSV file."""
        if os.path.isfile(self.filename):
            df = pd.read_csv(self.filename)
            if 0 <= index < len(df):
                df = df.drop(index)
                df.to_csv(self.filename, index=False)

    def clear_all(self):
        """Clear all records from the CSV file."""
        if os.path.isfile(self.filename):
            os.remove(self.filename)
