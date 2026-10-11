import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

### call d b credntials

MYSQL_HOST=os.getenv("")
MYSQL_USER=os.getenv("")
MYSQL_PASSWORD=os.getenv("")
MYSQL_DATABASE=os.getenv("")
MYSQL_PORT=os.getenv("MYSQL_PORT", "3386")

DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

engine= create_engine(DATABASE_URL, echo=True)

def test_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            print("Connection successful")
    except Exception as e:
        print(f"Connection failed: {e}")