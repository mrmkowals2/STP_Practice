import os

fp1 = os.path.join("D:"
                  ,"Desktop"
                  ,"STP_Practice"
                  ,"Challenges"
                  ,"Chapter 09"
                  ,"user input.txt")

fp = os.path.join("D:",os.sep,fp1)

user_input = input("Provide text input: ")

with open(fp,'w+') as f:
    f.write(user_input)

print(user_input)
