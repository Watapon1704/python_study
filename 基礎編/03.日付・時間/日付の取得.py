import datetime
 
 
today = datetime.date.today()
todaydetail = datetime.datetime.today()
 
print('----------------------------------')
print(today)
print(todaydetail)
 
print('----------------------------------')
print(today.year)
print(today.month)
print(today.day)
print(todaydetail.year)
print(todaydetail.month)
print(todaydetail.day)
print(todaydetail.hour)
print(todaydetail.minute)
print(todaydetail.second)
print(todaydetail.microsecond)

print('----------------------------------')
print(today.isoformat())
print(todaydetail.strftime("%Y/%m/%d %H:%M:%S"))
