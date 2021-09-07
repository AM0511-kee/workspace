import datetime



today_date=datetime.date.today()
print(today_date)
print(today_date.year)
print(today_date.month)
print(today_date.isoweekday())
delta=datetime.timedelta(days=10)
ten_days_later=today_date+delta
print(ten_days_later)
b_days=datetime.date(2021,11,5)
till_b_day=b_days-today_date
print(till_b_day)
print(till_b_day.total_seconds())
print(datetime.datetime.today())
after_14hrs=datetime.timedelta(hours=14)
print(after_14hrs)
