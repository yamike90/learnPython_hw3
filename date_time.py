from datetime import datetime, date, timedelta

d_yesterday = date.today() - timedelta(1)
d_today = date.today()
d_month_ago = d_today - timedelta(30)


print(d_yesterday)
print(d_today)
print(d_month_ago)

datetime_str = "01/01/17 12:10:03.234567"
date_str_to_dt = datetime.strptime(datetime_str, '%d/%m/%y %H:%M:%S.%f')
print(date_str_to_dt)