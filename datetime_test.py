from datetime import MINYEAR
import dis # use dis to check if a function has to be assigned to a variable or not within another function.


def import_datetime():
    import datetime
    # see import dis. to verify if it returns or not
    # when returned something it needs to be assigned to a variable
    return datetime # need to return the datetime module

def print_today():
    import datetime
    return datetime.date.today()


def datetime_now_m():
    n = import_datetime()
    c = n.datetime.datetime.now()
    print(c)

# datetime_now_m()


def show_date_not_time_m():
    o = import_datetime()
    n = o.datetime.now()
    k = n.strftime("%d-%m-%Y")
    print(k)

# show_date_not_time_m()

def print_y_m_d_today():
    datetime = import_datetime() # call the method import_datetime()
    n = datetime.date.today()
    print(n)

# print_y_m_d_today()

def show_universal_time():
    #from datetime import * # * wildcard not allowed
    from dateutil import tz
    n = datetime.now(tzutc())
    print(n)

#show_universal_time()

def dat():
    n = datetime.MINYEAR
    MINYEAR_constant_ex = datetime.datetime(MINYEAR, 1, 1) # fixed importing from module
    k = datetime.MAXYEAR
    print(f"Minimum year: {n}")
    print(f"{MINYEAR_constant_ex}")
    print(f"Maximum Year: {k}")

# dat()

# if it says return_const none it needs to be returned
# example of dis to check if something returns a value and needs to be assigned inside a local scope of another function
def check_return():
    import_datetime()

dis.dis(check_return) # load constant states (NONE)
print("-" * 50)
def check_Return():
    print("this")

dis.dis(check_Return)
print("-" * 50)
def checker():
    import datetime
    return datetime
dis.dis(checker)