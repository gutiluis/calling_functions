import csv


the_file_name = input("Enter the name of the csvfile: ")


# newline="" from bestpractice. official documentation
with open(the_file_name, newline="") as csvfile:
    reader = csv.reader(csvfile) # return a reader object
    for row in reader:
        print(row)

# from official documentation
with open("birthdays.csv", newline="") as csvfile:
    new_object = csv.reader(csvfile, delimiter=" ", quotechar="|")
    for row in new_object:
        print(", ".join(row))
