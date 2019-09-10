# variable of named formatter that holds the value of 4 bracketes
formatter = "{} {} {} {}"

# print function printing out the formatter variable using the format function and four arguments
print(formatter.format(1, 2, 3, 4))

# print function printing out the formatter variable using the format function and four arguments
print(formatter.format("one", "two", "three", "four"))

# print function printing out the formatter variable using the format function and four booleans
print(formatter.format(True, False, False, True))

# print function printing out the formatter variable using the format function and using the formatter as an argument four times
print(formatter.format(formatter, formatter, formatter, formatter))

# print function printing out the formatter variable using the format function and passing  strings for the four curly brackets
print(formatter.format(
    " try your \n",
    "Own text here \n",
    "Maybe a poem \n",
    "Or a song about fear \n"
))