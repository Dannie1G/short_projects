#password generator
##generate a customized password

import random

lower_letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@_$%^&"

pass_len = int(input("The required password length is: "))
upper_len = int(input("The required number of upper case letters is: "))
symb_len = int(input("The required number of symbols is: "))
num_len = int(input("The required number of numbers is: "))

num_lower = pass_len - upper_len - symb_len - num_len

print("Number of lower case letters is then: ", num_lower)

pw_list = []

if num_lower < 0:
	print("Sorry, the numbers you entered don't match up! Please try again.")
	exit()
	
	
#insert lowercase letters
i = 0

while i < num_lower:
	pw_list.append(str(''.join(random.sample(lower_letters, 1))))
	i += 1

	
#insert uppercase 
j = 0
upper_inc = num_lower - 1

while j < upper_len:
	pw_list.insert(random.randint(0, upper_inc), str(''.join(random.sample(upper_letters, 1))))
	j += 1
	upper_inc += 1

	
#insert symbols 
k = 0
symbol_inc = num_lower + upper_len - 1

while k < symb_len:
	pw_list.insert(random.randint(0, symbol_inc), str(''.join(random.sample(symbols, 1))))
	k += 1
	symbol_inc += 1

	
#insert numbers 
l = 0
num_inc = num_lower + upper_len + symb_len - 1

while l < num_len:
	pw_list.insert(random.randint(0, num_inc), str(random.randint(0, 9)))
	l += 1
	symbol_inc += 1

	
#print password	
print("Your generated password is: " + str(''.join(pw_list)))
