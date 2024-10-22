## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
import sys
def main() :
	# Nested function to calculate if the number is anti-prime
	def antiprimecalc(num):
		divnum = 0  # Count of divisors of the given number
		divi = 0  # Count of divisors for numbers smaller than num
        
          # Count the divisors of num
		for i in range(1, num + 1):
			if num % i == 0:
				divnum += 1

        # Compare divisors of all numbers smaller than num
		for i in range(1, num):
			divi = 0
			for j in range(1, i + 1):
				if i % j == 0:
					divi += 1
            # If any smaller number has more or equal divisors, return "not anti-prime"
			if divi >= divnum:
				return "not anti-prime"
        
		return "anti-prime"

    # Ensure we have exactly one command-line argument and it's a valid integer
	if len(sys.argv) != 2:
		return f"error: {sys.argv[0]} <number>"

	if not sys.argv[1].isdigit() or int(sys.argv[1]) <= 0:
		return "Please provide a positive integer greater than 0."

	num = int(sys.argv[1])
	result = antiprimecalc(num)
	return result

# Main logic to run the program
if __name__ == "__main__":
	print(main())

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
