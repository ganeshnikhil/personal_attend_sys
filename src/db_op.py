from src.date_time import today_date , cur_time , cur_dt_time , is_weekend
from src.holiday import HOLIDAY 
TABLE_NAME = "ATTENDANCE" 

# intialize database with parameters 
def initialize_db(conn):
    conn.execute('''CREATE TABLE ATTENDANCE
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        DATE TEXT NOT NULL,
        TIME TEXT NOT NULL,
        PERSENT INTEGER NOT NULL);''')  # Column name is PERSENT
    conn.commit()

# check if table already exist in the databse 
def already_exists(conn):
    result = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (TABLE_NAME,))
    return result.fetchone() is not None

# check if given date already exist in the table 
def date_exists(date: str, conn):
    result = conn.execute("SELECT PERSENT FROM ATTENDANCE WHERE DATE = ?", (date,))
    return result.fetchone() is not None

# write to the table 
def write_to_db(persent: int, date: str, time:str, conn):
    if not already_exists(conn):
        initialize_db(conn)
    if date_exists(date, conn):
        conn.execute("UPDATE ATTENDANCE SET PERSENT = ?, TIME = ? WHERE DATE = ?", (persent, time, date))
    else:
        conn.execute("INSERT INTO ATTENDANCE (DATE, TIME, PERSENT) VALUES (?, ?, ?)", (date, time, persent))
    conn.commit()

# get specific date attendance 
def spec_date_atten(date: str, conn):
    result = conn.execute("SELECT PERSENT FROM ATTENDANCE WHERE DATE = ?", (date,))
    return result.fetchone()

# get all the data persent in the databse 
def get_data(conn, all=False):
    if all:
        result = conn.execute("SELECT * FROM ATTENDANCE")
    else:
        result = conn.execute("SELECT * FROM ATTENDANCE LIMIT 50")
    return result.fetchall()

def get_month_data(conn, year, month):
    # Ensure the month is in two-digit format (e.g., '02' for February)
    month_str = f"{month:02d}"
    query = """
    SELECT * FROM ATTENDANCE 
    WHERE strftime('%Y', DATE) = ? 
    AND strftime('%m', DATE) = ?;
    """
    cursor = conn.cursor()
    cursor.execute(query, (str(year), month_str))
    results = cursor.fetchall()
    return results


# Function to check and insert absent entry
def check_and_add_absent(conn):
    # Get today's date and current time
    toda_date = today_date()
    current_time = cur_dt_time()
    entry_time = cur_time()
    flag = spec_date_atten(toda_date , conn)
    # If it's 12 PM and no entry exists, insert absent
    if not is_weekend() and toda_date not in HOLIDAY:
        if current_time.hour > 12 and flag is None:
            write_to_db(0 , toda_date , entry_time , conn)
            print("Absent entry added for", toda_date)
            return True 
        elif flag is not None:
            return True 
    return False 


def get_dates(conn):
    result = conn.execute("SELECT DATE FROM ATTENDANCE")
    return [row[0] for row in result.fetchall()]

def get_time(conn):
    result = conn.execute("SELECT TIME FROM ATTENDANCE")
    return [row[0] for row in result.fetchall()]

def get_attendance(conn):
    result = conn.execute("SELECT PERSENT FROM ATTENDANCE")
    return [row[0] for row in result.fetchall()]

def delete_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME};")
        conn.commit()
        print(f"Table {TABLE_NAME} deleted successfully.")
    except Exception as e:
        print(f"Error deleting table {TABLE_NAME}: {e}")
    finally:
        cursor.close()
