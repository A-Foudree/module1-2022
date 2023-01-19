"""
Program: cast_to_integer.py
Author: Ashley Fry
Last date modified: 01/18/2023

The purpose of this program is to accept any input,
convert to a integer type and output the integer.
"""
#Test your code by observing the results and adding comments at the bottom of your .py file
#Your code goes below here

user_input = input()
int(user_input)
print(user_input)


#and above here, use as many lines as you need; reference code at the top of this Topic for Hints



#Modify these comments with your inputs you tested; it is fine if your expected output isn't your actual output
# Input   Expected Output  Actual Output
#11           11                 11
#12.5         12                 12
#'Number'     Number             Number




#The input of 11 gave the expected output of 11.


#The input of 12.5 did not have the output of 12 as expected.
#When ran a ValueError: invalid literal for int() with base 10:'12.5'
#This happened because I am trying to convert a non-integer (a number with a decimal) variable into an integer.
#To solve this problem, I can use the float() method to convert a floating-point number in a string to an integer.


#The input 'Number' with expected output of Number, did not work.
#When ran a ValueError: invalid literal for int() with the base 10: 'Number'
#This happened because I tried to convert a string value that is not formatted as an integer, sting needs to be a number.
#This can be fixed by converting the input into a integer or float.