#guessing_game.py

def guess_number():
    x = 0 # x is the lowest number in range of possible numbers
    y = 50 # y is the middle number in range of possible numbers
    z = 100 # z is the maximum number in range of possible numbers

    counter = 1 # counter counts the number of guesses taken
    
    input("Please think of a number between 0 and 100, and then press enter.")

    condition = input("Is your number {} ? ('l' means number is too low, 'y' means yes, and 'h' means number is too high) ".format(round(y)))

    
    while condition != 'y':
    	counter += 1
    	if condition == 'l':
    		x = y + 1
    		y = (x + z) / 2
    		condition = input("Is your number {} ? ('l' means number is too low, 'y' means yes, and 'h' means number is too high) ".format(round(y)))
    	elif condition == 'h':
        	z = y - 1
        	y = (x + z) / 2
        	condition = input("Is your number {} ? ('l' means number is too low, 'y' means yes, and 'h' means number is too high) ".format(round(y)))

    
    if condition == 'y':
    	print("It took {} times to guess your number".format(counter))
    

guess_number()