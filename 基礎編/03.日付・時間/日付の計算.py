import datetime
 
 
today = datetime.datetime.today()
 
print(today)
 
print(today + datetime.timedelta(days=1))
 
newyear = datetime.datetime(2010, 1, 1)
 
print(newyear + datetime.timedelta(days=7))

calc = today - newyear

print(calc.days)
