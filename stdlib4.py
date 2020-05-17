from datetime import date,timedelta

now = date.today()
print(now)

otherd = date(2020,9,25)
print(otherd -now)
print(otherd+timedelta(days=2))

fdate = otherd.strftime('%m-%d-%y...... %d-%b-%Y...is a %A on th %d day of %B')
print(fdate)