new_file = open('new_file.txt', 'x')
new_file.close()
#check if a file exists or not
import os
print("Checking if my_file exists or not....")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")
os.rmdir('fortnite')
os.mkdir('fork knife')