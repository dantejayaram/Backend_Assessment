import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# GitHub Configuration
GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Check if token is present
if not GITHUB_TOKEN:
    raise ValueError("❌ GITHUB_TOKEN is not set in environment variables")
