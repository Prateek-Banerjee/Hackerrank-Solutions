# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
from datetime import date

month,day,year = input().split()

print((calendar.day_name[date(int(year),int(month),int(day)).weekday()]).upper())