# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with "From", then look for the third word and keep a running count of each of the days of the week. 
# At the end of the program print out the contents of your dictionary (order does not matter).

days = dict()
fh = open('../mbox-short.txt')
for line in fh :
    if line.startswith('From ') :
        day = line.split()[2]
        days[day] = days.get(day, 0) + 1
print(days)