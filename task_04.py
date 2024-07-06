from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
        
    end_date = today + timedelta(days=7)
    
    
    upcoming_birthdays = []
    
    for user in users:
        
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        
        birthday_this_year = birthday.replace(year=today.year)
        
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        
        if today <= birthday_this_year <= end_date:
            
            if birthday_this_year.weekday() == 5:  
                congratulation_date = birthday_this_year + timedelta(days=2)
            elif birthday_this_year.weekday() == 6:  
                congratulation_date = birthday_this_year + timedelta(days=1)
            else:
                congratulation_date = birthday_this_year
            
            
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Ringo Starr", "birthday": "1940.07.07"},
    {"name": "George Bush Jr.", "birthday": "1946.06.07"},
    {"name": "David Gilmour", "birthday": "1946.03.06"},
    {"name": "Carol White", "birthday": "1990.01.31"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
 

        
    
