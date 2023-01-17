"""
Program: main.py
Author: Ashley Fry
Last date modified: 01/16/2023

The purpose of this program is convert age in years to months.
The input is an integer representing the age in years.
The output an integer representing the age in months.
"""

#This is a comment
print("Hello World")

#I am going to set a name variable
users_name = 'Joe'

#Print out Hello to the user's name
print('Hello' + ' ' + users_name + '. How are you?')
#Print out the type of the name
print("The 'users_name' variable, is type: " + str(type (users_name)))

#print("The 'users_name' variable, is type: " + str(type ( Users_name)))
#print("the 'users_name' variable, is type: " + str(<class 'str'>))
#print("the 'users_name' variable, is type: " + "<class 'str' >")
#print("the 'users_name' variable, is type: <class 'str' >")
#The 'users_name' variable, is type: <class 'str'>

type_of_users_name = type(users_name)
str_of_type_of_users_name = str(type_of_users_name)
final_string = "The 'users_name' variable is type: " + str_of_type_of_users_name
print(final_string)

