'''''
msg ="hello, world "
print(msg.strip()) 
print(msg.upper())
print(msg.replace("world ", "python"))''''''
'''

''''
label ="data Science "
print(label[0])
print(label[5:12])''

''''''''
text = "python programming"
print(text[::-1])
print(text[:6])
print(text[7:])
print(text[0:3])
print(text[-3:-1])
'''

'''text = "pythonprogramming is a high level language "
print (text.split("+"))
'''



'''
//topic called stack and methods// 

stack = [10, 20, 30, 40, 50]
print("Initial stack:", stack)
stack.append(60)
print("After append:", stack)

popped = stack.pop(1)
print("Popped element:", popped)
print("After pop:", stack)

stack.insert(2, 99)                                         # Insert 99 at index 2
print("After insert:", stack)

del stack[1]                                          # Deletes element at index 1
print("After delete:", stack)

stack.remove(99)                                        # Removes first occurrence of 99
print("After remove:", stack)

stack.extend([70, 80, 90])
print("After extend:", stack)

stack.clear()
print("After clear:", stack)

stack = [10, 40, 20, 10, 50, 10]
print("New Stack:", stack)

stack.sort()
print("After sort:", stack)

stack.reverse()
print("After reverse:", stack)

print("Index of 20:", stack.index(20))


print("Count of 60:", stack.count(10))'''



'''a = [10, 20, 30, 40, 50]
print("Initial stack:", a)

a.append(60)
print("After append:", a)

popped = a.pop(1)             
print("Popped element:", popped)
print("After pop:", a)

a.insert(2, 99)                 
print("After insert:", a)

del a[1]                       
print("After delete:", a)

a.remove(99)                   
print("After remove:", a)

a.extend([70, 80, 90])
print("After extend:", a)

a.clear()
print("After clear:", a)

a = [10, 40, 20, 10, 50, 10]
print("New Stack:", a)

a.sort()
print("After sort:", a)

a.reverse()
print("After reverse:", a)

print("Index of 20:", a.index(20))

print("Count of 10:", a.count(10))'''



'''
//topic called tuple// 

t = (10, 20, 30, 20, 40, 20)

print(t.count(20))

print(t.index(30))'''

'''
//topic called lambda function// 
f = lambda x : x * 4
print(f(5))'''




'''
topic map function  
values = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(map(lambda x: x + 2, values))
print(result)'''

'''
filter function topic 
values = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(filter(lambda x: x % 2 == 0, values))

print(result)'''

'''from functools import reduce

values = [1, 2, 3, 4, 5, 6, 7, 8]

result = reduce(lambda x, y: x + y, values)
print(result) '''


'''
day3/task1
inventory = ["Apples", "Bananas", "Carrots", "Dates"]
print("Current Inventory:", inventory)
inventory.append("Eggs")
inventory.remove("Bananas")
inventory.sort()
print("Final Updated Inventory:", inventory)'''

'''
task2 //day3
temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print("First Reading:", temperatures[0])
print("Last Reading:", temperatures[-1])
afternoon_peak = temperatures[3:6]
print("Afternoon Peak Readings:", afternoon_peak)
last_three_hours = temperatures[-3:]
print("Last 3 Hours:", last_three_hours)'''

screen_res =(1920, 1080)
print("Current Resolution: 1920x1080")
print("Tuples cannot be modified!")

















