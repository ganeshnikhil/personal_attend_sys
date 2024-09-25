

def date_month(date):
    return int(date.split('-')[1])

def month_analysis(decision_list , month):
    month_list = []
    for _ , date , _ , persent in decision_list:
        if date_month(date) == month:
            month_list.append([date , persent])
    return month_list 
            
def year_analysis(decision_list):
    month_in_year = 12
    month_dict = {i:0 for i in range(1,month_in_year+1)}
    for _ ,date , _ , persent in decision_list:
        month = date_month(date)
        month_dict[month]+= persent
    return month_dict

