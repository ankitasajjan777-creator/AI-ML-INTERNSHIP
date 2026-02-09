
'''
file = open("example.txt","r")
print(file.readlines())
'''
'''file = open("example2.txt","a")
file.write("data science and AI/ML")
file.close()'''


'''with open(r"C:\Users\ankit\OneDrive\Desktop\day6 vs\image.png", "rb") as f:
    image = f.read()
    print(image)
'''
try:
    file =open ("sample.txt","r")
    print(file.read)
except Exception as e:
    print("file not found, pls open existing file ")
finally:
    file.close1
