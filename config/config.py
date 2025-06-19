from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
API_KEY = os.getenv('API_KEY')
DATABASE_URL = os.getenv('DATABASE_URL')

# Print to verify if the variables were loaded correctly
print(API_KEY)
print(DATABASE_URL)
