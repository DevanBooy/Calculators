# Compulsory Task 1

# While loop to display user menu
while True:
	menu = input('''\nWelcome to your simple calculator application.
			c - To access calculator
			v - View previous answers 
			e - Exit program
			: ''').casefold()

	# Perform calculation
	if menu == 'c':
		try:
			# input number 1
			num1 = float(input('Enter number one - '))

			# input math operation
			operation = input('Enter an operation (e.g. +, -, x, / ): ')

			list_of_operations = ['+', '-', 'x', '/']

			if operation not in list_of_operations:
				raise Exception('Error - please enter the available math operations.')

			# input number 2
			num2 = float(input('Enter number two - '))

			# Conditional logic
			if operation == '+':
				x = num1 + num2

			elif operation == '-':
				x = num1 - num2

			elif operation == 'x':
				x = num1 * num2

			elif operation == '/':
				x = num1 / num2

			# Assign answer to out_contents variable and print answer
			out_contents = f'\n{num1} {operation} {num2} = {x}'
			print(out_contents)

			# Open text file
			file = None
			try:
				# Prompt user to select filename
				file_name = input('\nPlease enter filename to append answers to (e.g. answers.txt) \n - ')
				# Append answers to text file
				file = open(file_name, 'a+')
				file.write(out_contents)
				print(f'\nAnswers written to - {file_name}')

			except Exception:
				print(f'\nYour chosen file name is invalid\n')

			finally:
				if file is not None:
					file.close()

		except ZeroDivisionError as e:
			print('\nError! - You are not allowed to divide by zero.')
		except ValueError as e:
			print('\nError! - could not convert string to float - please enter a valid number.')
		# else:
		# 	print('\nError! - You have entered an incorrect number or operation.')

	# View text file
	elif menu == 'v':
		try:
			# Prompt user to select which file to open
			chosen_file = input('Which file would you like to view (e.g. answers.txt) \n - ')
			contents = ""
			# Read text file
			f = open(chosen_file, 'r')

			# Print contents for text file
			for line in f:
				contents += line
			print(f'\nAll answers from {chosen_file}:\n')
			print(contents)

		except FileNotFoundError as error:
			print('\nThe file that you are trying to open does not exist')
			print(error)

	# Exit program
	elif menu == 'e':
		print('Goodbye!')
		exit()

	else:
		print('Error! You have made a wrong choice, Please Try again.')