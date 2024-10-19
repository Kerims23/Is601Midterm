# app/commands/operations.py
class Operations:
    def __init__(self):
        self.results = []  # Store results in memory

    def add(self, num1, num2):
        result = num1 + num2
        self.results.append({"operation": "add", "result": result})  # Save result in memory
        return result

    def subtract(self, num1, num2):
        result = num1 - num2
        self.results.append({"operation": "subtract", "result": result})
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.results.append({"operation": "multiply", "result": result})
        return result

    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        result = num1 / num2
        self.results.append({"operation": "divide", "result": result})
        return result

    def get_results(self):
        return self.results  # Return results for viewing if needed
