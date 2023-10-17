import os

#print(f"OS: {os.name}")
#print("___Here___")
#print(os.getcwd())
#print("___Here___")
#print(os.listdir(path="."))
#the_path = os.getcwd()
#print(os.listdir(the_path))
#print(os.path.isdir(the_path))
f = open("text.txt", "w+")
f.write("Does this work?")
with open("text.txt", "r") as reader:
    line = reader.readline()
    while line != " ":
        print(line, end=" ")
        line = reader.readline()