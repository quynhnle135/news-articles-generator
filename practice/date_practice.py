from datetime import date, timedelta, datetime


today = date.today()
week = date.isoweekday(today)
print(today)
print(week)

monday_date = datetime.strptime("2023-12-11", "%Y-%m-%d").date()
print(monday_date)
print(type(monday_date))
print(date.isoweekday(monday_date))

start_date = today - timedelta(days=today.weekday())
end_date = start_date + timedelta(days=6)
print(start_date)
print(today.weekday())
print(end_date)

another_start_date = datetime.strptime("2023-12-12", "%Y-%m-%d")
print(another_start_date)
print(another_start_date.weekday())
another_start_date = another_start_date - timedelta(days=another_start_date.weekday())
print(another_start_date)