# Author: DA (amdg) 10/29/20

import calendar
# question 1- Shows the calendar for the year 2020, with months and days of the week
calendar.TextCalendar().pryear(2020)

# question 2- change the number since they correspond with what day of the week the calandar will use 0=monday
calendar.TextCalendar(6).pryear(2020)

# question 3
print(calendar.month(2020, 3))

# question 4
calendar.LocaleTextCalendar(6, "SPANISH").pryear(2020)
calendar.LocaleTextCalendar(6, "FRENCH").pryear(2020)
calendar.LocaleTextCalendar(6, "PORTUGUESE").pryear(2020)
calendar.LocaleTextCalendar(6, "RUSSIAN").pryear(2020)

# question 5- returns wether the year inputted is a leap year or not with true or false
print(calendar.isleap(2020)) 