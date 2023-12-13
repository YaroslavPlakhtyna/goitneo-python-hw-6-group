from datetime import datetime, timedelta
from collections import defaultdict

users = [{"name": "Bill Gates", "birthday": datetime(year=1955, month=10, day=28)},
         {"name": "Volodya", "birthday": datetime(1989, 12, 12)},
         {"name": "Dad", "birthday": datetime(1959, 12, 16)},
         {"name": "Mum", "birthday": datetime(1960, 12, 17)},
         {"name": "Vlad", "birthday": datetime(1991, 12, 14)},
         {"name": "Andrii", "birthday": datetime(1990, 12, 15)},
         {"name": "Oleh", "birthday": datetime(1999, 9, 12)}
         ]

def get_birthdays_per_week(users:list[dict]):
    contacts = defaultdict(list)
    today = datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            
        delta_days = (birthday_this_year - today).days
        if delta_days <= 7:
            birthday_weekday = (today + timedelta(days=delta_days)).strftime("%A")
            if birthday_weekday in ['Sunday','Saturday']:
                birthday_weekday = 'Next Monday'
            contacts[birthday_weekday].append(name)
    info = ''
    tail = ''
    for k, value in contacts.items():
        if k == 'Next Monday':
            tail += f"{k}: {', '.join(value)}"
            continue
        info += f"{k}: {', '.join(value)}\n"
    info += tail 
    print(info)


get_birthdays_per_week(users)
