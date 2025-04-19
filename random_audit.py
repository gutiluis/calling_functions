from random import randrange
from datetime import datetime
from datetime import timedelta

def random_date(start, end):
    """
    Function to return a random date within a time frame.
    still missing. random objects. auditing system.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds = random_second)


d1 = datetime.strptime("1/1/2008 1:30 PM", "%m/%d/%Y %I:%M %p")
d2 = datetime.strptime("1/1/2009 4:50 AM", "%m/%d/%Y %I:%M %p")

print(random_date(d1, d2))
