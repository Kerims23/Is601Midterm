'''history.py'''
import pandas as pd

class HistoryManager:
    def __init__(self):
        self.history = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])

    def add_to_history(self, operation, operand1, operand2, result):
        new_entry = {'operation': operation, 'operand1': operand1, 'operand2': operand2, 'result': result}
        self.history = self.history.append(new_entry, ignore_index=True)

    def show_history(self):
        print(self.history)

    def clear_history(self):
        self.history = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])
        print("History cleared.")
