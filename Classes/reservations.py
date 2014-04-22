"""
**Airline / Hotel Reservation System** - Create a reservation system which books airline seats or hotel rooms. It charges various rates for particular sections of the plane or hotel. Example, first class is going to cost more than coach.
 Hotel rooms have penthouse suites which cost more. Keep track of when rooms will be available and can be scheduled.
"""
import datetime
from calendar import monthrange

month_names = {1:'January', 2:'February', 3:'March', 4:'April', 
          5:'May', 6:'June', 7:'July', 8:'August',
          9:'September', 10:'October', 11:'November', 12:'December'}

current_year, current_month = datetime.date.today().year, datetime.date.today().month


class Calendar(object):
    
    def __init__(self):
        self.reservations = []
        
    def update(self, update):

        self.reservations.append(update)
                
    def printCalendar(self, year=current_year, month=current_month):

        days_taken = [day.date.day for day in self.reservations if day.date.month==month]
        # days_taken is a list of days that are
        first_day = monthrange(year, month)[0]
        last_day = monthrange(year, month)[1]+1
        
        print 'Month of %s' % month_names[month]
        for i in range(first_day, last_day):
            print "%d:\t %s" % (i, 'Not available' if i in days_taken else 'Available')
            

class Reservation(object):
    
    def __init__(self, name, date, upgrade=False):
        self.name = name
        self.date = date
        self.upgrade = upgrade
        self.price = 99.99 if self.upgrade else 79.99
        
paul = Reservation('Paul', datetime.date.today())
calendar = Calendar()
calendar.update(paul)
