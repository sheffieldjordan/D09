def fizzbuzz():
	for n in range(1,101):
		#msg = ''
		if n%3 == 0 and n%5 == 0: #
			print("FizzBuzz") #
		elif n % 3 == 0: 
			# msg += "Fizz" 
			print("Fizz")
		elif n%5 == 0:
			# msg += "Buzz" 
			print("Buzz")
		else: #
			# print(msg or n) ==> enables you to remove the first condition and remove the else:. 
			print(n)


def main():
	fizzbuzz()
if __name__ == '__main__':
    main()