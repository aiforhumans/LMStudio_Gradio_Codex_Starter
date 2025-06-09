import os
import sys

# Ensure the project root is on the Python path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api_client import chat_with_model

def test_dummy():
    # Dummy test example
    assert True
