my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
<<<<<<< HEAD
my_cent = 74 * 2.54 # converting inches to centimeters
my_kg = 180 / 0.45359237# converting pounds to kg
=======
my_cent = 74 * 2.54 # inches
my_weight = 180 # lbs
>>>>>>> 2d8debd409286179a0b3420dac0425964945662c
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}")
print(f"He's {my_cent} centimeters tall.")
<<<<<<< HEAD
print(f"He's {my_kg} pounds heavy.")
=======
print(f"He's {my_weight} pounds heavy.")
>>>>>>> 2d8debd409286179a0b3420dac0425964945662c
print(f"Actually that's not too heavy.")
print(f"He's got {my_eyes}eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_kg + my_kg
print(f"if I add {my_age}, {my_kg}, and {my_kg} I get {total}.")