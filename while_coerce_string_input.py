import sys




def main():
    check_is_digit()
    keep_going()

def check_is_digit():
    a = input("Enter text: ")
    while a.isdigit():
        a = input("Error. Do not enter an integer")
        break
    if not a.isdigit():
        print("Your input is:", str(a)," and ",type(a))

def keep_going():
    while True:
        k = input("To try again select YES or NO: ").lower()
        if k == "yes":
            check_is_digit()
        else:
            sys.exit()


if __name__=="__main__":
    main()
