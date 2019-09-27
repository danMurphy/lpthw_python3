# function named cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    '''cheese_and crackers function takes two arguments
    and then prints them out along with statments'''
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} cheeses!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# this a print statment
print("We can just give the function numbers directly:")
# cheese_and_crackers function being called with two interger number arguments
cheese_and_crackers(20, 30)


# another print statment here
print("OR, we can use variable from our script:")
# a variable holding the number 10 
amount_of_cheese = 10
# a variable holding the number 50
amount_of_crackers = 50

# cheese_and_crackers function being called using the two variables called amount_of_cheese and amount_of _crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Another print statment
print("We can even do math inside too:")
# calling the function and doing addition in the arguments spot before running the code
cheese_and_crackers(10 + 20, 5 + 6)

# another print statment here
print("And we can combine the two, variables and math:")
# calling the function again but now adding a variable by a number for both arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#====================================================================================

def fruits(apples, bananas, oranges):
    print(f"I need to by {apples} apples for the Grayson")
    print(f"{bananas} bananas for next week")
    print(f"And {oranges} oranges for the week after that")
    print("damn these kids get alot of fiber in his diet.\n")


print("Grayson is begging for more fruit!")
print("Grayson said he wants apples, bananas, and, oranges")
print("This is how many he said he wanted of each:")

fruits(5, 6, 8)

print("The next he even wants more then that")

fruits(5 * 8, 4 + 11, 25 * 100)

print("NOW...he said he wants alot more")
print("So now he wants 500 apples plus 7000 more")
print("450 bananas times 10")
print("300 oranges plus 2000")

apples = 500
bananas = 450
oranges = 300

fruits(apples + 7000, bananas * 10, oranges + 2000)
