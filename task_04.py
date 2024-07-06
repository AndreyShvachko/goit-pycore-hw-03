from datetime import datetime, timedelta

def get_upcoming_bithdays(users):

    today = datetime.today().date()
    end_date = today + timedelta(days=7)

upcoming_birthdays = []

     for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y .%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

    if birthday_this_year < today:
        birthday_this_year = birthday_this_year.replace(year = today.year + 1)

    if today <= birthday_this_year <= end_date:
        if birthday_this_year.weekday() == 5:
            congratulation_date = birthday_this_year + timedelta(days = 2)
        elif birthday_this_year.weekday() == 6:
            congratulation_date = birthday_this_year +timedelta(days == 1)
        else:
            congratulation_date = birthday_this_year

        upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
        return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alice Johnson", "birthday": "1992.01.28"},
    {"name": "Bob Brown", "birthday": "1995.01.30"},
    {"name": "Carol White", "birthday": "1990.01.31"}
]
upcoming_birthdays = get_upcoming_bithdays (users)
print("List of congrats for this week:", upcoming_birthdays)     

        
    
