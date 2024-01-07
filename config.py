import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Get API key


def get_api_key():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        logging.error("OPENAI_API_KEY not found in environment variables.")
        exit("Please set your OPENAI_API_KEY in the .env file.")
    return api_key
