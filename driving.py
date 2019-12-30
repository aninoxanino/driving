nationality = input('Your nationality: ')
age = input('Your age: ')
age = int(age)
if nationality == 'Taiwan':
	if age >= 18:
		print('You can drink and smoke')
	else:
		print('You are illegal to drink and smoke')
elif nationality == 'America' or nationality == 'USA' or nationality == 'US':
	if age >= 21:
		print('You can drink and smoke')
	elif age >= 18 and age < 21:
		print('You can drink but cannot smoke')
	else:
		print('You cannot smoke and drink')


