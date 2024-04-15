"""Calculate days from now to specific date"""

from datetime import datetime

def get_days_from_today(date: str) -> int:
    """Returns number of days between input date and today's date

    date
        the date with which the days difference must be calculated from today
    """
    days = 0

    try:
        now = datetime.today()
        date_format = '%Y-%m-%d'
        date = datetime.strptime(date, date_format)

        days = now.toordinal() - date.toordinal()
    except ValueError as error:
        print(error) # logger should be here
    except TypeError as error:
        print(error) # logger should be here

    return days

print(get_days_from_today('2023-04-14')) # 366
