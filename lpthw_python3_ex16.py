# importing argv from sys module
from sys import argv

# unpacking script and filename variable from argv
script, filename = argv

# printing out the file name 
print(f"We're going to erase {filename}.")
# printng a statment to tell the user hit CRTL-C to cancell if they want to
print("If you don't want that, hit CTRL-C (^C).")
# printing a statment to tell the user hit the RETURN button to continue
print("If you do want that, hit RETURN")

# receiving there input of CRTL-C or return
input("?")

# printing out a statment letting the user know we are now opening the file
print("Open the file...")
# opening the file wit the write open and storing in a variable named target
target = open(filename, 'w')

# printing out statement letting user know we are deleting everything here
# print("Truncating the file....GOODBYE")
# using the truncate() function to delete all the data from the .txt file
# target.truncate()

# asking the user for 3 statments here
print("Now I am going to ask you for three lines")

# getting statment 1 from the user
line1 = input("line1: ")
# getting statment 2 from the user
line2 = input("line2: ")
# getting statment 3 from the user
line3 = input("line3: ")

# printing a statment letting the user know that the program is going to write to the file
print("I'm going to write these to the file now")


# writing statment 1 to file
target.write(line1 + "\n" + line2 + "\n" + line3)
# new line
# target.write("\n")
# writing statment 2 to file
# target.write(line2)
# new line 
# target.write("\n")
# writing statment 3 to file
# target.write(line3)
# new line
# target.write("\n")

# printing out statment letting the user know we are closing the file
print("And finally we close the file")

# closing the file
target.close()