#Input/Output Homework #8
import os

directory = os.listdir(".")
def check_user_file():
    user_file = input("What file would you like to edit?\n")
    
    if user_file in directory:
        answer = input("Would you like to:\nA) Read the file\nB) Delete the file and start over\nC) Append the file\nEnter A,B or C\n")
        if answer.lower() == "a":
            new_file = open(user_file,"r")
            for line in new_file:
                print(line)
            new_file.close()
        elif answer.lower() == "b":
            new_file = open(user_file,"w")
            print("The file data has been deleted")
            data = input("Enter the text you would like to write to the file\n")
            new_file.write(data)
            new_file.close()
        elif answer.lower() == "c":
            with open(user_file,"a") as new_file:
                new_file.write(input("Enter the text you would like to append to the end of the file\n"))
                new_file.write("\n")
        else:
            print("That was not a valid input")
    else:
        new_file = open(user_file,"w")
        new_file.write(input("Enter the text you would like to write to this file\n"))
        new_file.close()

check_user_file()

