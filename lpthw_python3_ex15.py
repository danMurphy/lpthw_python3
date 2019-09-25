# import argv from sys module
from sys import argv

# unpacking script variable and filename variable 
script, filename = argv

# variable named txt using the open function to open passed argument of filename
txt = open(filename)

#printing out the filename
print(f"Here is file : {filename}")
#printing out the file contents here
print(txt.read())

# printing out type the filename again 
print("Type the filename again : ")
#getting the input of the filename again
file_again = input('> ')

#variable here using the open function to open file
txt_again = open(file_again)

#printing the contents again of the filei
print(txt_again.read())

print(txt_again.close())