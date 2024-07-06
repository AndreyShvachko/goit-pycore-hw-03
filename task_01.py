from datetime import datetime

def get_days_from_today(date):
    
    needed_date = datetime.strptime(date, '%Y-%m-%d')
    today_date = datetime.today().date()
    needed_date = needed_date.date()
    delta = today_date - needed_date
    return delta.days

print(get_days_from_today('1987-07-07'))