from datetime import datetime, timedelta



dt_now = datetime.now()
dt_now.strftime('%Y-%m-%d')
delta = timedelta(days=1)
dt_yest = dt_now - delta
dt_yest.strftime('%Y-%m-%d')
dt_tom = dt_now + delta
dt_yest.strftime('%Y-%m-%d')
print('Сегодня: '+str(dt_now))
print('Вчера: '+str(dt_yest))
print('Завтра: '+str(dt_tom))


date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print('Дата из строки: '+str(date_dt))