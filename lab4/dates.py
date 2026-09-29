from datetime import datetime, timedelta

# 1
current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print("Current date:  ", current_date)
print("5 days ago:    ", five_days_ago)

# 2
today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:    ", today)
print("Tomorrow: ", tomorrow)

# 3
now = datetime.now()
print("With microseconds:   ", now)
print("Without microseconds:", now.replace(microsecond=0))

# 4
date1 = datetime(2026, 9, 1, 10, 0, 0)
date2 = datetime(2026, 9, 29, 12, 30, 0)
diff_seconds = (date2 - date1).total_seconds()
print("Difference in seconds:", diff_seconds)