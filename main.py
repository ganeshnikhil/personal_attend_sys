from src.db import conn_db 
from src.ui import main_gradio
from src.report import generate_html, month_end, year_end
from src.send_email import send_email 
from dotenv import load_dotenv
from os import environ 
from src.db_op import delete_table, check_and_add_absent , initialize_db 
from src.file_op import open_and_update_json, load_month_data 
from src.date_time import today_date, date_month, is_after_noon, calculate_sleep_duration 
from src.logger import log_err , log_info 
import threading 
import time 
import sys 

load_dotenv() 

file_path = "emailed.json"
mont_data = load_month_data(file_path)
month = date_month(today_date())
weekends = []
def report_script():
    """Check month and year end to generate and send reports."""
    if month_end() and month not in mont_data and is_after_noon():
        html_code , image_paths = generate_html()
        SENDER_EMAIL = environ.get("Sender_email")
        RECIEVER_EMAIL = environ.get("Receiver_email")
        PASSWORD = environ.get("Password")
        
        if send_email(html_code,image_paths, PASSWORD, SENDER_EMAIL, RECIEVER_EMAIL):
            log_info("Email sent successfully.")
            open_and_update_json(file_path, month)
        else:
            log_err("Failed to send email.")
    
    if year_end() and is_after_noon():
        conn = conn_db()
        try:
            delete_table(conn)
            log_info("End of year report processed. Dropping table.")
            initialize_db(conn)
            log_info("New SQL table is created.")
        except Exception as e:
            log_err(f"Error processing year end report: {e}")
        finally:
            conn.close()
        

def main():
    demo = main_gradio()
    demo.launch()

def update_today_abs():
    """Update today's attendance and return success flag."""
    conn = conn_db()
    try:
        flag = check_and_add_absent(conn)
    except Exception as e:
        log_err(f"Error updating attendance: {e}")
        flag = False
    finally:
        conn.close()
    return flag 

def threaded_report_script():
    """Continuously run the report script every hour."""
    while True:
        try:
            report_script()
        except Exception as e:
            log_err(f"Error in report script: {e}")
        time.sleep(60 * 60)  # Run the script every hour

def threaded_update_today_abs():
    """Continuously update today's absences at specified intervals."""
    while True:
        flag = update_today_abs()
        log_info(f"Attendance update flag: {flag}")
        seconds = calculate_sleep_duration()
        time.sleep(int(seconds))

if __name__ == "__main__":
    try:
        report_thread = threading.Thread(target=threaded_report_script)
        report_thread.daemon = True
        report_thread.start()
        
        update_abs_thread = threading.Thread(target=threaded_update_today_abs)
        update_abs_thread.daemon = True
        update_abs_thread.start()
        
        main()
    except KeyboardInterrupt:
        log_info("Program terminated by user.")
        sys.exit(0)