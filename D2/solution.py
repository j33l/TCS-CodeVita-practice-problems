'''
Solution for "Television Sets" problem
'''

'''
static user input for testing
'''
# numberOfRooms = 20
# rateForTwoTypesOfRooms = [1500, 1000]
# targetedRevenue = 7227990

# User input
numberOfRooms = int(input('Enter number of rooms: '))
rateForTwoTypesOfRooms = [int(i) for i in input('Enter rate for with TV and without TV room(space seperated): ').split()]
targetedRevenue = int(input('Enter targeted revenue: '))

'''
A function to determine if a year is a leap year.
'''
def is_leap_year(year):
    # return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)
    return False # as per problem description, this is for non-leap year

'''
returns days in a given monthNumber based on a year is leap year or not
'''
def days_in_month(monthNumber, year = 0):
    if monthNumber == 9 or monthNumber == 4 or monthNumber == 6 or monthNumber == 11:
        return 30
    elif monthNumber == 1 or monthNumber == 3 or monthNumber == 5 or monthNumber== 7 or monthNumber == 8 or monthNumber == 10 or monthNumber == 12:
        return 31
    elif monthNumber == 2 and is_leap_year(year) == True:
        return 29
    elif monthNumber == 2 and is_leap_year(year) == False:
        return 28
    else:
        return 0

'''
stores number of patients on every day for a year as a [[monthlyList]]
'''
numberOfPatients = []
for month in range(1, 13): # 12 months/year
    # monthlyPatients = []
    for day in range(1, days_in_month(month) + 1):
        # monthlyPatients.append(int((6-month)**2 + ((day-15)**2)**(1/2)))
        numberOfPatients.append(int((6-month)**2 + ((day-15)**2)**(1/2)))
    # numberOfPatients.append(monthlyPatients)

currentRevenue = 0

'''
calculating revanue if all patient takes min rate room
'''
for dailyPatient in numberOfPatients:
    currentRevenue += dailyPatient * min(rateForTwoTypesOfRooms)

minNumberOfTV = 0

'''
increasing number of TVs if revenue is less then targeted
'''
while currentRevenue < targetedRevenue and minNumberOfTV <= numberOfRooms:
    currentRevenue += (max(rateForTwoTypesOfRooms) - min(rateForTwoTypesOfRooms))
    minNumberOfTV += 1

if(targetedRevenue > currentRevenue):
    print('Can\'t generate enough revenue, number of rooms: ', numberOfRooms)
else:
    print(f'minimum number of TVs:\t{minNumberOfTV}\nGenerated revenue:\t{currentRevenue}\nTargeted revenue:\t{targetedRevenue}.')
    # print(minNumberOfTV)

