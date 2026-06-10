import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / "finance.db"


def get_connection():
    return sqlite3.connect(str(DB_PATH))


def create_tables():
    conn = get_connection()

    schema_path = BASE_DIR / "database" / "schema.sql"

    with open(schema_path, "r", encoding="utf-8") as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()