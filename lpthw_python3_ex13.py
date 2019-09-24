from sys import argv

#read the WYSS section for how to run this

script, second, third, fourth = argv

first_input = input("type something here thanks")
second_input = input("type something here again")
third_input = input("type something here again for the third time")
fourth_input = input("type something here again for the fourth time")

print(f"The script is called : {first_input}", script) 
print(f"Your first variable is :{second_input}", second)
print(f"Your second variable is :{third_input}", third)
print(f"Your third variable is: {fourth_input}", fourth)