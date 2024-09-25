from src.date_time import today_date , cur_time , date_month , date_year , is_weekend
from src.db import conn_db 
from src.db_op import write_to_db , get_data , get_dates , get_month_data
from src.holiday import HOLIDAY 
#Get all dates from the database 
def get_all_dates():
    conn = conn_db()
    date = today_date()
    dates = get_dates(conn)
    conn.close()
    if date not in dates:
        dates.insert(0,date)
    return dates


# Gradio function to write attendance
def submit_attendance(date, persent):
    conn = conn_db()
    time = cur_time()  # You can dynamically set the current time or let the user input
    persent_value = 1 if persent == "Present" else 0
    write_to_db(persent_value, date, time, conn)
    conn.close()
    return "Attendance updated successfully."

# Gradio function to display database contents in tabular form
def display_database():
    conn = conn_db()
    data = get_data(conn, all=True)
    conn.close()
    # Format data for Dataframe component
    formatted_data = [[row[0], row[1], row[2], "Present" if row[3] == 1 else "Absent"] for row in data]
    return formatted_data

def month_dates():
    tod_date = today_date()
    month = date_month(tod_date)
    year = date_year(tod_date)
    conn = conn_db()
    month_data = get_month_data(conn , year , month)
    conn.close()
    date = today_date()
    dates = [data[1] for data in month_data]
    if date not in dates and not is_weekend():
        if date not in HOLIDAY:
            dates.insert(0,date)
    return dates 

