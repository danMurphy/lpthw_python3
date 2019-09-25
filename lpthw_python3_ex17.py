# importing argv function from sys module
from sys import argv
# importing exists function from os.path
from os.path import exists

# variable names for argv..expecting 3 variables
script, from_file, to_file = argv

# printing out from_file variable to to_file variable
print(f"Copying from {from_file} to {to_file}")

# in_file variable using the open() function to open the file
in_file = open(from_file)
# indata variable using the in_file variable data to read the file
indata = in_file.read()

# printing out the length of indata
print(f"The input file is {len(indata)} bytes long")

# printing if the file already exists 
print(f"Does the output file exist? {exists(to_file)}")
# printing out to see if you want to continue or abort at this point
print("Ready , hit RETURN to continue, or CRTL-C to abort")
input()

# out_file variable opening and write mode 
out_file = open(to_file, 'w')
# out_file wrtiting the data  
out_file.write(indata)

# printing done here
print("Alright, ..all done here.")

# saving the file
out_file.close()
# closing out the file
in_file.close()