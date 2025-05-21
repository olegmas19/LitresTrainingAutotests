import pytest
from dotenv import load_dotenv
import os

@pytest.fixture(scope="session", autouse=True)
def litres_user():
    load_dotenv()
    litres_login = os.getenv("LITRES_LOGIN")
    litres_password = os.getenv("LITRES_PASSWORD")
    return litres_login, litres_password
