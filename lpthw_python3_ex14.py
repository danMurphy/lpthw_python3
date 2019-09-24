from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to know ask you a few questions.")
print(f"Do you like me {user_name}")
like_me = input(prompt)

print(f"where do live {user_name}")
live = input(prompt)

print(f"What kind of computer do you have {user_name}?")
computer = input(prompt)

print(f"""
Alright, so you said {like_me} about liking me.
You live in {live}. Not sure where that is.
And you have a {computer} computer. Nice.
""")