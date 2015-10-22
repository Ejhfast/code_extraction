# How to turn users input into a list in Python?
user_choice_port = "23, 80, 44"
print map(int, user_choice_port.split(","))
print [int(n) for n in user_choice_port.split(",")]
