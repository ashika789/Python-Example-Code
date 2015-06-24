# This program is designed to print 10 random integers greater than 10 and less than 50.
# Import the random module.
import random
 
# Define the main function

def main():
	randfind()

def randfind():
	for count in range(10):
        # Define number variable using random.randint
		number = random.randint(10,49)
        # Use print to display numbers
		print(number),
		print(' '),

main()