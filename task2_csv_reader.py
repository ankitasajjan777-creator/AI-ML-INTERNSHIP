name = input("Enter your name: ")
goal = input("Enter your Daily Goal: ")

with open("journal.txt", "a") as file:
    file.write(f"Name: {name}, Daily Goal: {goal}\n")
    import csv
with open (r"C:\Users\ankit\Downloads\Company_Data.csv", mode= "r") as file:
    csv_file = csv.reader(file)
    for lines in csv_file:
        print(lines)