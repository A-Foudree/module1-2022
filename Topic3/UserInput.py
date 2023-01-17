
#grabbing users age, assigning to a variable
user_age = input('Please enter an age: ')

#cast their age to an integer
age_in_25_years = int(user_age) + 25

#print their age in 25 years
print('In 25 years you will be age: ' + str(age_in_25_years))


#short hand
user_age = int(input('Please enter an age:'))
age_in_25_years = user_age + 25
print('In 25 years you will be age: ' + str(age_in_25_years))


#shorter hand
user_age = int(input('Please enter an age: ')) + 25
print('In 25 years you will be age: ' + str(age_in_25_years))

#one liner
print('In 25 years you will be age: ' + str(int(input('Please enter an age: ')) + 25))