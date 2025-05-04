import os
from pathlib import Path
from dotenv import load_dotenv

def  load_env():
    load_dotenv()
    litres_login = os.getenv("LITRES_LOGIN")
    litres_password = os.getenv("LITRES_PASSWORD")
    return litres_login, litres_password
# dotenv_path=Path(__file__).resolve().parent.parent.parent / f".env"