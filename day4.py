'''
student = {"name": "ankita", "age": 21, "course": "AI"}
print(student)

student = {"name": "ankita", "age": 21}
print(student["name"])
print(student["age"])

student = {"name": "ankita", "age": 21}
student["city"] = "bengalore"
print(student)

student = {"name": "ankita", "age": 21}
student["age"] = 22
print(student)

student = {"name": "ankita", "age": 21}
student.pop("age")
print(student)


student = {"name": "ankita", "age": 21}

for key, value in student.items():
    print(key, ":", value)

    student = {"name": "ankita", "age": 21}

if "name" in student:
    print("Name is present")

student = {"name": "ankita", "age": 21}
print(len(student))

students = {
    1: {"name": "bhagya", "age": 21},
    2: {"name": "ankita", "age": 22}
}

print(students[2]["name"])
'''

'''
#DICTIONARY TOPIC
day4 task1 submission

contacts = {
    "Ankita": "9876543210",
    "Riya": "9123456780",
    "Karan": "9988776655"
}
contacts["Megha"] = "9001122334"
contacts["Riya"] = "7000000001"

found = contacts.get("Ankita", "Contact not found")
not_found = contacts.get("Rahul", "Contact not found")
print ("safe LookupResults: ")
print("Ankita's number:", found)
print("Rahul's number:", not_found)

print("\nAll Contacts:")
for name, phone in contacts.items():
    print("Contact:", name, "| Phone:", phone)'''


'''
#SETS FUNCTIONS TOPIC #

fruits = {"apple", "banana", "mango"}
print("Original Set:", fruits)

fruits.add("orange")
print("\nAfter add('orange'):", fruits)

fruits.remove("banana")
print("\nAfter remove('banana'):", fruits)

fruits.discard("grapes")  
print("\nAfter discard('grapes'):", fruits)

removed_item = fruits.pop()
print("\nAfter pop():", fruits)
print("Removed item:", removed_item)'''




'''#SET OPERATION TOPIC
set1 = {1, 2, 3, 4, 5, 7, 8, 9, 0, 4}
set2 = {3, 4, 5, 4, 8, 5, 9, 6, 5, 7}

print("Union:", set1.union(set2))

print("Intersection:", set1.intersection(set2))

print("Difference:", set1.difference(set2))'''



'''
day3 task2 submission 

raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

unique_users = set(raw_logs)

check_id = "ID05" in unique_users
print("Is ID05 in unique users?:", check_id)

print("Original list count:", len(raw_logs))
print("Unique users count:", len(unique_users))

print("Unique user IDs:", unique_users)'''

friend_a = {"python", "cooking", "hiking", "movies"}
friend_b = {"hiking", "gaming", "photography", "python"}
shared_interests = friend_a & friend_b
all_shared_interests = friend_a | friend_b
unique_intersects_a = friend_a - friend_b

 













