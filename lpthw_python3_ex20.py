# importing argv from sys module
from sys import argv

# adding to variables to argv
script, input_file = argv

# function named print_all. This will print all the file contents
def print_all(f):
    print(f.read())

# function named rewind. This will rewind the pointer to position zero in the file
def rewind(f):
    f.seek(0)

# function named print_a_line. This argument takes two numbers. One is a number. The other prints out one line from the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# variable current_file holding the open() function to open the info_file.txt
current_file = open(input_file)

# printhing separator
print('===================================')
# printing statment
print("First let's print the whole file:\n")

# function call printing out all the contents from info_file.txt
print_all(current_file)
# printing out separator
print('===================================')

# printing out separator
print('===================================')
# printing statment
print("now let's rewind, kind of like a video tape.")

# calling function rewind() to rewind pointer to line zero in info_file.txt
rewind(current_file)
# printing out separator
print('===================================')


# printing out separator
print('===================================')
#printing out separator
print('===================================')
# printing out a statment
print("Let's print three lines:\n")

# variable current_line equal to 1
current_line = 1
# function call with passing two arguments. One argument is an interger number of one. Thee other is passing the info_file.txt 
print_a_line(current_line, current_file)

# variable current_line and adding 1 to get 2
current_line = current_line + 1
# function call with passing two arguments. One argument is an interger of two. The other is getting line 2 from info_file.txt
print_a_line(current_line, current_file)

# variable current_line and adding 2 to get 3
current_line = current_line + 1
# function call with passing two arguments. One argument is an interger of three. The other is getting line 3 from info_file.txt
print_a_line(current_line, current_file)
#printing out separator
print('===================================')