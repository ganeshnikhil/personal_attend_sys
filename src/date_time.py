from datetime import date
from datetime import datetime , timedelta

def today_date():
    current_date = date.today()
    return  current_date.strftime("%Y-%m-%d")

def cur_time():
    current_time = datetime.now().time()
    return current_time.strftime("%I:%M:%S %p")

def cur_dt_time():
    return datetime.now()

def date_month(date):
    return int(date.split('-')[1])

def date_year(date):
    return int(date.split('-')[0])

def next_day():
    # Current date
    current_date = datetime.now()

    # Add one day
    next_day = current_date + timedelta(days=1)

    # Format the next day as "Next day: YYYY-MM-DD"
    formatted_next_day = next_day.strftime("%Y-%m-%d")

    return formatted_next_day

def calculate_sleep_duration():
    current_time = datetime.now()
    if current_time.hour >= 12:
        # Calculate the time until 12 PM the next day
        tomorrow_noon = (current_time + timedelta(days=1)).replace(hour=12, minute=0, second=0, microsecond=0)
        return (tomorrow_noon - current_time).total_seconds()
    else:
        # Sleep until 12 PM today
        today_noon = current_time.replace(hour=12, minute=0, second=0, microsecond=0)
        return (today_noon - current_time).total_seconds()

def is_weekend():
    """
    Check if a given date is a Saturday or Sunday.
    
    :param date_str: Date in the format 'YYYY-MM-DD'
    :return: True if the date is Saturday or Sunday, False otherwise
    """
    date_obj = cur_dt_time()
    
    # Get the day of the week (0 = Monday, 6 = Sunday)
    day_of_week = date_obj.weekday()
    
    # Check if it's Saturday (5) or Sunday (6)
    return day_of_week == 5 or day_of_week == 6

def days_psd_month():
    # Get today's date
    today = datetime.today()
    
    # Calculate the number of days passed in the year
    day_of_year = today.timetuple().tm_yday  # tm_yday gives the day of the year
    
    # Calculate the number of days passed in the current month
    day_of_month = today.day  # Directly gives the day of the month
    
    return day_of_month

def days_psd_year():
    today = datetime.today()
    # Calculate the number of days passed in the year
    day_of_year = today.timetuple().tm_yday  # tm_yday gives the day of the year
    return day_of_year 

def is_after_noon():
    current_time = datetime.now().time()
    return current_time.hour >= 12