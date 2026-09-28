from datetime import datetime,date,timedelta

now = datetime.now()
today = date.today()

print(f"Сейчас: {now}")
print(f"Сегодня: {today}")

moon_landing = datetime(1969, 7, 20, 20, 17)
print(f"Высадка на Луну: {moon_landing}")

from datetime import datetime

dt = datetime(2026, 9, 28, 14, 30)

# --- strftime: Форматируем объект в строку ---
# %Y - год (4 цифры), %m - месяц (01-12), %d - день, %H - часы (24ч), %M - минуты
formatted_str = dt.strftime("%d.%m.%Y в %H:%M")
print(formatted_str)  # Вывод: 28.09.2026 в 14:30

# --- strptime: Парсим строку обратно в объект ---
api_response = "2026-12-31 23:59:59"
# Мы должны указать питону шаблон, в котором записана строка
parsed_dt = datetime.strptime(api_response, "%Y-%m-%d %H:%M:%S")
print(type(parsed_dt)) # Вывод: <class 'datetime.datetime'>

#------------------------------------------------------------
new_year = datetime(2027,1,1)

time_left = new_year - now
print(f"До Нового года осталось: {time_left.days} дней")

# Прибавляем время (например, рассчитываем дату подписки на 30 дней)
subscription_duration = timedelta(days=30, hours=12)
expiry_date = now + subscription_duration
print(f"Подписка истекает: {expiry_date.strftime('%d.%m.%Y')}")