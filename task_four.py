"""Upcoming birthdays"""

from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list:
    """Returns list of users that have birthday withing 7 days including current date

    users
        list of user dictionalries with name and birthday in format of YYYY.MM.DD
    """
    today = datetime.today().date()
    current_year =datetime.now().year
    end_of_week_date = today + timedelta(days=7)
    upcoming_birthdays = []

    try:
        for user in users:
            birth_date = user['birthday']
            birth_date = datetime.strptime(birth_date, '%Y.%m.%d').date()
            birthday_this_year = birth_date.replace(year=current_year)

            if birthday_this_year < today:
                birth_date = birth_date.replace(year=current_year + 1)
            else:
                birth_date = birthday_this_year

            if today <= birth_date <= end_of_week_date:
                if birth_date.weekday() > 4:
                    days_delta = 7 - birth_date.weekday()
                    birth_date += timedelta(days=days_delta)
            
                upcoming_birthdays.append({
                    'name': user['name'], 
                    'congratulation_date': birth_date.strftime('%Y.%m.%d')
                })
    except TypeError as e:
        print(e) # logger
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Tod Brown", "birthday": "1990.04.15"},
    {"name": "Barbara Drinkwater", "birthday": "1990.04.21"},
]
upcoming_birthdays = get_upcoming_birthdays(users)
print(upcoming_birthdays)
