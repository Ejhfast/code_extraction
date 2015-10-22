# User input integer list
user_input = raw_input("Please enter five numbers separated by a single space only: ")
input_numbers = [int(i) for i in user_input.split(' ') if i.isdigit()]
