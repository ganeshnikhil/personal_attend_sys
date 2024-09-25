from src.date_time import next_day, today_date, date_month, date_year 
from src.graph import cl_plot, br_plot
from src.db import conn_db
from src.db_op import get_data , get_month_data
from src.date_anly import  year_analysis
import base64
from src.holiday import HOLIDAY 

def month_end():
    cur_date = today_date()
    next_date = next_day()
    cur_month = date_month(cur_date)
    next_month = date_month(next_date)
    return next_month != cur_month

def year_end():
    cur_date = today_date()
    next_date = next_day()
    cur_year = date_year(cur_date)
    next_year = date_year(next_date)
    return next_year != cur_year

def month_path(month_data):
    month = date_month(today_date())
    year = date_year(today_date())
    #month_data = month_analysis(month_data , month)
    _ , dates,_,pr_details = zip(*month_data)
    dates = list(dates)
    pr_details = list(pr_details)
    month_path = cl_plot(dates, pr_details ,month , year)
    return month_path 

def year_path(all_data):
    year = date_year(today_date())
    year_data = year_analysis(all_data)
    month_data = list(year_data.keys())
    pre_pr_month = list(year_data.values())
    year_path = br_plot(month_data, pre_pr_month , year)
    return year_path 


def total_month_pr(month_data):
    month = date_month(today_date())
    # month_data = month_analysis(all_data , month)
    _ , pr_details = zip(*month_data)
    pr_details = list(pr_details)
    return sum(pr_details)

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def decision_msg(all_data , month_threshold = 16):
    cur_month = date_month(today_date())
    week_in_month = sum(1 for date in HOLIDAY if date_month(date) == cur_month)
    month_threshold -=  week_in_month
    decision_list = []
    paths = []
    if month_end():
        month_prnset = total_month_pr(all_data)
        if  month_prnset >= month_threshold:
            decision_list.append("<h1> Monthly performance is STEADY.</h1>")
        else:
            decision_list.append("<h1> Monthly performance needs ATTENTION.</h1>")
        month_img_path = month_path(all_data)
        month_image_tag = '<img src="cid:month_image" alt="Month Image" />'
        paths.append(("month_image" ,month_img_path))
        decision_list.append(month_image_tag)
        
    if year_end():
        year_img_path = year_path(all_data)
        year_image_tag = '<img src="cid:year_image" alt="Year Image" />'
        paths.append(("year_image",year_img_path))
        decision_list.append(year_image_tag)
        
    return decision_list , paths 

def generate_html():
    conn = conn_db()
    if not year_end():
        year = date_year(today_date())
        month = date_month(today_date())
        all_data = get_month_data(conn , year , month)
    else:
        all_data = get_data(conn , all=True)
    conn.close()
    
    decision_list , image_paths = decision_msg(all_data)
    
    html_content = r"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Attendance Report</title>
        <style>
            body {{
                font-family: 'Helvetica Neue', Arial, sans-serif;
                background-color: #f4f7f6;
                color: #333;
                margin: 0;
                padding: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }}
            .recommendation {{
                max-width: 600px;
                width: 100%;
                background-color: #ffffff;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
                overflow: hidden;
                text-align: center;
                padding: 40px 20px;
            }}
            .recommendation h1 {{
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 20px;
                color: #1e88e5;
            }}
            .recommendation p {{
                font-size: 16px;
                margin: 15px 0;
                line-height: 1.5;
                color: #555555;
            }}
            .recommendation img {{
                max-width: 100%;
                border-radius: 8px;
                margin-top: 20px;
            }}
            .recommendation .alert {{
                background-color: #ffe082;
                color: #ff6f00;
                padding: 10px;
                margin-top: 20px;
                border-radius: 8px;
            }}
            .footer {{
                margin-top: 40px;
                font-size: 12px;
                color: #888;
            }}
            @media (max-width: 768px) {{
                .recommendation {{
                    padding: 30px 15px;
                }}
                .recommendation h1 {{
                    font-size: 22px;
                }}
                .recommendation p {{
                    font-size: 15px;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="recommendation">
            {0}
        </div>
        <div class="footer">
            <p>&copy; {1} Attendance Report. All rights reserved.</p>
        </div>
    </body>
    </html>""".format("\n".join(decision_list), date_year(today_date()))
    return html_content , image_paths

