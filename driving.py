nationality = input('Your nationality: ')
age = input('Your age: ')
age = int(age)
if nationality == 'Taiwan':
	if age >= 18:
		print('You can drink and smoke')
	else:
		print('You are illegal to drink and smoke')
