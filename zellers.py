# first and last names
first_name = raw_input('Enter your first name: ')
last_name = raw_input('Enter your last name: ')
# date of birth
print 'Enter your date of birth: '
day = input('Day? ')
month = input('Month? (Mar: 1,..., Jan: 11, Feb: 12) ')
year = input('Year? (If born in Jan or Feb, enter previous year)')
#Century And Year
century = year/100
year = year % 100
#Apply zeller's algorithm
W = (13 * month - 1) / 5
X = year / 4
Y = century / 4
Z = W + X + Y + day + year - 2 * century
R = Z % 7
#Result
print first_name, last_name, 'was born on day', R, 'of the week'
print "(0 means Sunday, 1 means Monday, ..., 6 means Saturday)"
