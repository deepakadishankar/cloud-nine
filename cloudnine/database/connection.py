from pathlib import Path
import sqlite3

# Root directory of the project
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

# Data directory
DATA_DIR = ROOT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# SQLite database file
DATABASE_PATH = DATA_DIR / "cloudnine.db"


def get_connection() -> sqlite3.Connection:
    """
    Return a connection to the Cloud Nine database.
    """
    return sqlite3.connect(DATABASE_PATH)


def initialize_database() -> None:
    """
    Initialize the SQLite database and create all required tables.
    """

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS device_passports (
                c9_id TEXT PRIMARY KEY,
                fingerprint TEXT UNIQUE NOT NULL,
                nickname TEXT,
                first_seen TEXT NOT NULL,
                last_seen TEXT NOT NULL,
                import_count INTEGER DEFAULT 0,
                favorite INTEGER DEFAULT 0
            );
            """
        )

        connection.commit()