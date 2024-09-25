import  sqlite3
from src.logger import log_err , log_info
from os.path import exists , dirname , abspath
from os import makedirs
# FILE_PATH  = "DATABASE/Attendance.db"

FILE_PATH = "DATABASE/Attendance.db"
DIRECTORY = dirname(abspath(FILE_PATH))


def conn_db():
    # Check if the directory exists; if not, create it
    if not exists(DIRECTORY):
        try:
            makedirs(DIRECTORY)
            log_info(f"[=] Created directory: {DIRECTORY}")
        except Exception as e:
            log_err(f"[!] Failed to create directory: {e}")
            return None
    try:
        conn = sqlite3.connect(FILE_PATH)
        log_info("[=] Database connection successful.")
        return conn
    except sqlite3.Warning as e:
        log_err(f"SQLite Warning: {e}")
    except sqlite3.Error as e:
        log_err(f"SQLite Error: {e}")
    except sqlite3.InterfaceError as e:
        log_err(f"SQLite Interface Error: {e}")
    except sqlite3.DatabaseError as e:
        log_err(f"SQLite Database Error: {e}")
    except sqlite3.DataError as e:
        log_err(f"SQLite Data Error: {e}")
    except sqlite3.OperationalError as e:
        log_err(f"SQLite Operational Error: {e}")
    except sqlite3.IntegrityError as e:
        log_err(f"SQLite Integrity Error: {e}")
    except sqlite3.InternalError as e:
        log_err(f"SQLite Internal Error: {e}")
    except sqlite3.ProgrammingError as e:
        log_err(f"SQLite Programming Error: {e}")
    except sqlite3.NotSupportedError as e:
        log_err(f"SQLite Not Supported Error: {e}")
    except Exception as e:
        log_err(f"Unexpected Error: {e}")
    return None 


