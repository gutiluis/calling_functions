import sys




def main():
    check_is_digit()
    keep_going()

def check_is_digit():
    a = input("Enter text: ")
    while a.isdigit():
        a = input("Error. Do not enter an integer")
        break
    if a.isdigit():
        print("Your input is:", str(a))

def keep_going():
    while True:
        k = input("To try again select YES or NO: ").lower()
        if k == "no":
            sys.exit()
        else:
            k == "yes"
            check_is_digit()


if __name__=="__main__":
    main()
