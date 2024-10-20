import logging
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get log level and log file path from environment variables
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")

# Create a logger
logger = logging.getLogger("calculator")
logger.setLevel(LOG_LEVEL)

# Create file handler which logs messages to the file specified in .env
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(LOG_LEVEL)

# Create console handler to output logs to the terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(LOG_LEVEL)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("Logging is configured.")