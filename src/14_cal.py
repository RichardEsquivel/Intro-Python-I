"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# will be format 14_cal.py [month][year]

args = len(sys.argv)

print("Number of arguments given on command line", args)

# If user did not specify a month and year default to outputting the current month and date value
if args == 1:
    month = datetime.now().month
    year = datetime.now().year

# 2 if user only specified the month and not the year
elif args == 2:
    month = int(sys.argv[1])
    year = datetime.now().year

# 3 user specified both month and year
elif args == 3:
    month = int(sys.argv[1])
    year = int(sys.argv[2])

else:
    # User did not provide data in the format specified
    print("Error: Format needed is : 14_cal.py [month here] [year here]")
    exit(0)

tc = calendar.TextCalendar()

tc.prmonth(year, month)
