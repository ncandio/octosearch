import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Flask application secret key for session security
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-secret-key'
    
    # GitHub API token for authenticated requests (increases rate limits)
    # Create a token at https://github.com/settings/tokens
    GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
