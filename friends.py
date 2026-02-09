

friends = []
for i in range(3):
    name = input(f"Enter friend name {i+1}: ")
    friends.append(name)

with open("friends.txt", "w") as f:
    for friend in friends:
        f.write(friend + "\n")

marks = input("Enter marks to append: ")
with open("friends.txt", "a") as f:
    f.write("Marks: " + marks + "\n")

student = input("Enter student name: ")
student_marks = input("Enter marks for the student: ")



with open("marks.txt", "a") as f:
    f.write(student + "-" + student_marks + "\n")



with open("marks.txt", "r") as f:
    lines = f.readlines()
    print("How many students are listed?", len(lines))
    search_name = input("Enter a name to search in friends.txt: ")

with open("friends.txt", "r") as f:
    content = f.read().splitlines()

if search_name in content:
    print("Found!")
else:
    print("Not found!")