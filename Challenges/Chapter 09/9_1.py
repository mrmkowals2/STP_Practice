import os

fp1 = os.path.join("D:"
                  ,"Desktop"
                  ,"STP_Practice"
                  ,"tstp"
                  ,"module1.py")

fp = os.path.join("D:",os.sep,fp1)

file_contents = []

with open(fp,'r') as f:
    file_contents.append(f.read())

print(file_contents)
