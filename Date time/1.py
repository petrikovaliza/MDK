import datetime

now = datetime.datetime.now()

formatted_date_1 = now.strftime("%d.%m.%Y")
print(formatted_date_1)

formatted_date_2 = now.strftime("%d.%m.%y")
print(formatted_date_2)

formatted_date_3 = now.strftime("%d %b %Y")
print(formatted_date_3)

full_date = now.strftime("%d.%m.%Y")
day_of_year = now.strftime("%j")
week = now.strftime("%U")
day_of_week = now.strftime("%A")
exact_time = now.strftime("%X")
exact_time_ampm = now.strftime("%p %X")
print(full_date, '- день в году:', day_of_year, ', неделя:', week, ', день недели:', day_of_week)
print('Точное время: ', exact_time)
print('Точное время: ', exact_time_ampm)