"""
**Airline / Hotel Reservation System** - Create a reservation system which books airline seats or hotel rooms. It charges various rates for particular sections of the plane or hotel. Example, first class is going to cost more than coach.
 Hotel rooms have penthouse suites which cost more. Keep track of when rooms will be available and can be scheduled.
"""
import datetime
from calendar import monthrange
current_year_month = (datetime.date.today().year, datetime.date.today().month)

class Calendar(object):
    
    def __init__(self):
        self.reservations = []
        
    def update(self, update):

        self.reservations.append(update)
                
    def printCalendar(self, month_year=current_year_month):
        for i in range(monthrange(month_year)[0], monthrange(month_year)[1]):
            print i
            

class Reservation(object):
    
    def __init__(self, name, date, upgrade=False):
        self.name = name
        self.date = date
        self.upgrade = upgrade
        self.price = 99.99 if self.upgrade else 79.99
        
paul = Reservation('Paul', datetime.date.today())
calendar = Calendar()
calendar.update(paul)
print calendar.printCalendar()