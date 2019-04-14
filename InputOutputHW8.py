#Input/Output Homework #8
import os

directory = os.listdir(".")
def check_user_file():
    user_file = input("What file would you like to edit?\n")
    
    if user_file in directory:
        answer = input("Would you like to:\nA) Read the file\nB) Delete the file and start over\nC) Append the file\nD) Replace a single line\nEnter A,B,C or D\n")
        if answer.lower() == "a":
            new_file = open(user_file,"r")
            for line in new_file.readlines():
                print(line)
            new_file.close()
        elif answer.lower() == "b":
            new_file = open(user_file,"w")
            print("The file data has been deleted")
            data = input("Enter the text you would like to write to the file: ")
            new_file.write(data + "\n")
            new_file.close()
        elif answer.lower() == "c":
            with open(user_file,"a") as new_file:
                new_file.write(input("Enter the text you would like to append to the end of the file: ") + "\n")
        elif answer.lower() == "d":
            line_number = int(input("What line number would you like to replace?\n"))
            replace_text = input("Enter the new text for the line: ")
            temp_file = []
            with open(user_file,"r") as new_file:
                counter = 1
                for line in new_file:
                    temp_file.append(line)
                    counter += 1
            temp_file[line_number-1] = replace_text + "\n"
            with open(user_file, "w") as new_file:
                for line in temp_file:
                    new_file.write(line)


        else:
            print("That was not a valid input")
    else:
        new_file = open(user_file,"w")
        new_file.write(input("Enter the text you would like to write to this file: "))
        new_file.close()

check_user_file()

