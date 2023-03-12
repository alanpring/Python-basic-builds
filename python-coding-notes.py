# is a one line comment
"""
is a multiline
commment
"""
#print
#in python 3 this using parentheses, python 2 doesn't
#datatype is string
#
print("with double quotes")
print('with single quotes')
print "python 2"
print 'python 2'
# + to combine strings
print "Hello " + "AJ"
#
print total_cost
#
#print "Mismatched quotes will cause a SyntaxError'
#print Without quotes will cause a NameError
#EOL error means End of Line - string wasn't closed properly
#
#
#print string and variables. Must convert variable to string first
age = 13
print "I am " + str(age) + " years old!"
# 
#
#if doing arithmetic, need to convert string to numeric datatype
number1 = "100"
number2 = "10"
string_addition = number1 + number2 
# string_addition now has a value of "10010"
int_addition = int(number1) + int(number2)
# int_addition has a value of 110
#
string_num = "7.5"
print float(string_num)
#
#
float_1 = 0.25
float_2 = 40.0
product = float(float_1) * float_2
big_string = "The product was " + str(product)
#
#
#
#
#variables
#for data that may need to change over time
#use underscore to join words in var name e.g. hot_dog
todays_date = 20220904
#
#updating variabls
money_in_wallet = 40
sandwich_price = 7.50
sales_tax = .08 * sandwich_price
sandwich_price += sales_tax
money_in_wallet -= sandwich_price
#
#adding variables to existing variable
annual_rainfall += september_rainfall + october_rainfall + november_rainfall + december_rainfall
#
#variables with multiline strings
haiku = """The old pond,
A frog jumps in:
Plop!"""
#
#Arithmetic
#
mirthful_addition = 12381 + 91817
amazing_subtraction = 981 - 312
trippy_multiplication = 38 * 902
happy_division = 540 / 45
sassy_combinations = 129 * 1345 + 120 / 6 - 12
#modulo returns the remainder after division
is_this_number_odd = 15 % 2
is_this_number_divisible_by_seven = 133 % 7
#
#division will return an integer even if that's not the correct answer
#must use float numbers or float() method to get the correct result
quotient1 = 7./2
# the value of quotient1 is 3.5
quotient2 = 7/2.
# the value of quotient2 is 3.5
quotient3 = 7./2.
# the value of quotient3 is 3.5
quotient1 = float(7)/2 
# the value of quotient1 is 3.5
#
float_cucumbers_per_person = float(cucumbers) / num_people
#
#
#Numbers
#
#integer - a whole nuumber, no dedimal point
int1 = 1
int2 = 10
int3 = -5
#
#a number with a decimal point is a float
float1 = 1.0
float2 = 10.
float3 = -5.5
#
#you can also use scientific notation with 'e' indicating to the power of 10
# this evaluates to 150:
float4 = 1.5e2 
#
#
#
#Boolean
#True or False
#it's a special type of integer
#True = 1
#False = 0
#need to capitalise in order for these values to work
#
#
#
#strings
#A string can contain letters, numbers, and symbols.
#strins need escaping for special characters like '
'There's a snake in my boot!'
'There\'s a snake in my boot!'
#
"""
String methods let you perform specific tasks for strings.

We’ll focus on four string methods:

len() - gets the length (the number of characters) of a string
lower() - converts to lower case. Uses Dot Notation
upper() - converts to upper case. Uses Dot Notation
str() - turns data into string
"""
#
#
parrot = "Norwegian Blue"
print len(parrot)
print parrot.lower()
print parrot.upper()
#
#
pi = 3.14
print str(pi)
#
#
#Dot Notation only works with strings
#len() and str() can work on other data types.
#
#
#String Concatenation
# adding strings together
# + is the add operator
print "Spam " + "and " + "eggs"
#
#
#using str()
print "The value of pi is around " + str(3.14)
#
#
#
"""
The % operator after the string is used to combine a string with variables.
The % operator will replace the %s in the string with the string variable that comes after it.
"""
name = "Mike"
print "Hello %s" % (name)
#
#
#
"""
If you’d like to print a variable that is an integer, you can “pad” it with zeros using %02d.
The 0 means “pad with zeros”, the 2 means to pad to 2 characters wide, and the d means the number is a signed integer (can be positive or negative).
"""
day = 6
print "03 - %s - 2019" %  (day)
# 03 - 6 - 2019
print "03 - %02d - 2019" % (day)
# 03 - 06 - 2019
#
#
#
#
#datetime comes from a library
#this needs importing
from datetime import datetime
now = datetime.now()
print now
print now.year
print now.month
print now.day
#
#
"""
Remember that the standalone % operator after the string will fill the %02d and %04d placeholders in the string on the left with the numbers and strings in the parentheses on the right.
%02d pads the month and day numbers with zeros to two places
%04d pads the year to four places. This is one way dates are commonly displayed.
"""
#
#
#
from datetime import datetime
now = datetime.now()
print "%02d/%02d/%04d" % (now.month, now.day, now.year)
#
#
from datetime import datetime
now = datetime.now()
print '%s:%s:%s' % (now.hour, now.minute, now.second)
#
#
from datetime import datetime
now = datetime.now()
print '%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year,  now.hour, now.minute, now.second)
#
#
#
#Comparators
# == equal to
# != not equal to
# < less than
# <= less than or equal to
# > greater than
# >= greater than or equal to
#
# Operators
# *= multiply and assign
# += add and assign
# -= subtract and assign
#
#
#
#Boolean operators
#and - checks if both statements are true
#or - checks if at least one statement is true
#not - gives the opposite statement
#
#
"""
not is evaluated first;
and is evaluated next;
or is evaluated last.
"""
#
#
not 3 ** 4 < 4 ** 3
#
#
"""
True or not False and False. not gets evaluated first, so we have True or True and False.
and goes next, so we get True or False.
As we’ve seen, True or False is True, so the value finally returned is True!
"""
#
#
#
#
#Conditional Statement Syntax
#
#
"""
Pay attention to the indentation before the print statement. This space, called white space, is how Python knows we are entering a new block of code. Python accepts many different kinds of indentation to indicate blocks. In this lesson, we use four spaces but elsewhere you might encounter two-space indentation or tabs (which Python will see as different from spaces).

If the indentation from one line to the next is different and there is no command (like if) that indicates an incoming block then Python will raise an IndentationError. These errors could mean, for example, that one line had two spaces but the next one had three. Python tries to indicate where this error happened by printing the line of code it couldn’t parse and using a ^ to point to where the indentation was different from what it expected.
"""
#
#
if some_function():
  # block line one
  # block line two
  # et cetera
#
#
#
if 8 > 9:
  print "I don't get printed!"
else:
  print "I get printed!"
#
#
#
if 8 > 9:
  print "I don't get printed!"
elif 8 < 9:
  print "I get printed!"
else:
  print "I also don't get printed!"
#
#
#
#raw_input - accepts a string, prints it, waits for user response
name = raw_input("What's your name?")
print name
#
#
#You can use .isalpha() to check that a string doesn’t contain any non-letter characters! For example:
#
#
#Functions
#defined by three components
# header - includes def, function name and params
def hello_world(): # There are no parameters
#
#optional comment
"""Prints 'Hello World!' to the console."""
#
#body - what the function carries out. Must be indented
  print "Hello World!"
#
#
def hello_world():
  """Prints 'Hello World!' to the console."""
  print "Hello World!"
#
#
#Functions need to be called to run
#
def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print "%d squared is %d." % (n, squared)
  return squared
square(10)
#Here, the function square was called with the parameter n set to the argument 10.
#
#
#Functions can call functions
#
def one_good_turn(n):
  return n + 1
def deserves_another(n):
  return one_good_turn(n) + 2
#
#
#
def cube(number):
  return number * number * number
def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False
#
#
#
#Importing
"""
Pulling in just a single function from a module is called a function import, and it’s done with the from keyword:
"""
from module import function
#e.g.
from math import sqrt
#
#
#Universal import brings over all functions from module
from math import *
#
#
"""
it’s best to stick with either import module and type module.name or just import specific variables and functions from various modules as needed.
"""
#
#
#
#Functions
#
#max() - returns the largest argument. Best used on integers and floats
maximum = 13, 45, 56, 9
print max(maximum)
#
#
#min() - prints smallest
minimum = -54, 565, 3, 66
print min(minimum)
#
#
#abs() - absolute value. The number's distance from 0. Can only accept one number
#
absolute = -42
print abs(absolute)
#
#
#type() - returns the type of data
#
print type("dog")
print type(23)
print type(34.7)
#
"""
<type 'str'>
<type 'int'>
<type 'float'>
"""
#
#
#
#
def shut_down(s):
  if s == "yes":
    return "Shutting down"
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry"
  #
  #
  #
def distance_from_zero(i):
  if type(i) == int or type(i) == float:
    return abs(i)
  else:
    return "Nope"
#
#
#
def hotel_cost(days):
  return 140 * days
def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
  else:
    return "Sorry"
def rental_car_cost(days):
  daily = 40 * days
  if days >= 7:
    daily -= 50
  elif days >= 3:
    daily -=20
  return daily
def trip_cost(city, days, spending_money):
  return plane_ride_cost(city) + hotel_cost(days -1) + rental_car_cost(days) + spending_money
print trip_cost("Los Angeles",5,600)
#
#
#
#Lists
"""
Lists are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name. (Datatypes you’ve already learned about include strings, numbers, and booleans.)
"""
#
zoo_animals = ["pangolin", "cassowary", "sloth", ];
empty_list = []
#
#
"""
List indices begin with 0, not 1! You access the first item in a list like this: list_name[0]. The second item in a list is at index 1: list_name[1].
"""
#
numbers = [5, 6, 7, 8]
print numbers[1] + numbers[3]
#
#
#Append lists
#
#
suitcase = [] 
suitcase.append("sunglasses")
# Your code here!
suitcase.append('horse')
suitcase.append('flip flops')
suitcase.append('hat')
list_length = len(suitcase) # Set this to the length of suitcase
print "There are %d items in the suitcase." % (list_length)
print suitcase
#
#
#
#Slicing
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
# The first and second items (index zero and one)
first = suitcase[0:2]
# Third and fourth items (index two and three)
middle = suitcase[2:4]
# The last two items (index four and five)
last =  suitcase[4:6]
#
#
"""
In Python, when we specify a portion of a list in this manner, we include the element with the first index, 1, but we exclude the element with the second index, 3.
"""
#
#Slicing single values
#
animals = "catdogfrog"
# The first three characters of animals
cat = animals[:3]
# The fourth through sixth characters
dog = animals[3:6]
# From the seventh character to the end
frog = animals[6:]
#
#
#List - Search and insert
#
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")
# Your code here!
animals.insert(duck_index,"cobra")
print animals # Observe what prints after the insert operation
#
#
#
#For Loop
#
#
my_list = [1,9,3,8,5,7]
for number in my_list:
  print 2 * number
#
#
#
start_list = [5, 3, 1, 2, 4]
square_list = []
# Your code here!
for x in start_list:
  square_list.append(x ** 2)
square_list.sort()
print square_list
#
#
#
names = ["Adam","Alex","Mariah","Martine","Columbus"]
for i in names:
  print i
#
#
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}
# Add your code below!
for i in webster:
  print webster[i]
#
#
#
#print event numbers
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for x in a:
  if x % 2 == 0:
    print x
#
#
#
#count the number of 'fizz' in the list
def fizz_count(x):
  count = 0
  for i in x:
    if i == "fizz":
      count += 1
  return count

  fizz_count(["fizz","cat","fizz"])
#
#
#
#
#
#Adding list entries
#
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']
# Your code here: Add some dish-price pairs to menu!
menu['dog'] = 2.90
menu['cat'] = 345.00
menu['owl'] = 0.98
print "There are " + str(len(menu)) + " items on the menu."
print menu
#
#
#
#Overriding list entries - key pairs & deleting keys
#
# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines
# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']
# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin']='Meooooqw'
print zoo_animals
#
#
#
#Remove list items
#
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove("dagger")
#
#
#
#
inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf'],
  'pocket':['seashell', 'strange berry', 'lint']
}
# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
# Your code here
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold']+=50
#
#
#
#
prices = {
  "banana" : 4,
  "apple"  : 2,
  "orange" : 1.5,
  "pear"   : 3,
}
stock = {
  "banana" : 6,
  "apple"  : 0,
  "orange" : 32,
  "pear"   : 15,
}

for key in prices:
  print key
  print "price: %s" % prices[key]
  print "stock: %s" % stock[key]

total = 0
for sales in prices:
  print prices[sales] * stock[sales]
  total = total + prices[sales] * stock[sales]
print total
#
#
#
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}
# Add your function below!
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total/len(numbers)
def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return 0.1 * homework + 0.3 * quizzes + 0.6 * tests
def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >=80:
    return "B"
  elif score >=70:
    return "C"
  elif score >=60:
    return "D"
  else:
    return "F"
def get_class_average(class_list):
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)
students = [lloyd, alice, tyler]
avg = get_class_average(students)
print(avg)
print(get_letter_grade(avg))
#
#
#
#
"""
n.pop(index) will remove the item at index from the list and return it to you:
n.remove(item) will remove the actual item if it finds it:
del(n[1]) is like .pop in that it will remove the item at the given index, but it won’t return it:
"""
"""
Okay! Range time. The Python range() function is just a shortcut for generating a list, so you can use ranges in all the same places you can use lists.

range(6) # => [0, 1, 2, 3, 4, 5]
range(1, 6) # => [1, 2, 3, 4, 5]
range(1, 6, 3) # => [1, 4]

The range function has three different versions:

range(stop)
range(start, stop)
range(start, stop, step)
"""
#
#
def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x
print my_function(range(0,3)) # Add your range between the parentheses!
#
#
#
#
#
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
  results = []
  for numbers in lists:
    for i in numbers:
      results +=[i]
  return results
print flatten(n)
#
#
#
# keep python shell open
# this will keep the shell open until enter is hit
input('Press ENTER to exit')
#
#
#
"""

NESTED LISTS

To specify a single element in a 2-dimensional list, you need to give two indices. The syntax is: list_name[i][j], where i is an index in the outer list and j is an index in the inner list.

O O O O O
O O O O O
O O O O O
O O O O O
O O O O O

If we have nested lists, doing example[index] would give back another list. So then we can once again use another index to get the value from that list:
example[index][other_index]

The board is a multi-dimensional array. The list contains other list, each of these lists is a row on our board. Within these nested lists we have our columns.
So board[guess_row] would be returning a list like ['O', 'O', 'O', 'O', 'O',]. If you then reassign that to 'X', board[guess_row] = 'X' then you forget that list entirely and wind up with the issue you mention.
Using board[guess_row][guess_col] first returns that list, ['O', 'O', 'O', 'O', 'O',] (so the output of board[guess_row]) and then the [guess_col] index is used to get a specific element of that list. In this way you only change a single element of the list to 'X' (e.g. guess_col=1 resulting in ['O', 'X', 'O', 'O', 'O',]instead of replacing your entire list with that string.

board[guess_row][guess_col] = "X"

board – find the list. This is a nested list
row is first index as it was defined first
col is second as it was defined second

It’s a 2D list as we have horizontal and vertical


IF STATEMENTS

You can nest these

if - if
elif – else if
else – else


FOR LOOPS

use ‘break’ to break out of a for loop

"""

# WHILE LOOPS
# these are like if statements, but continue to execute whilst the condition is true, not just once like if
count = 0

if count < 5:
  print "Hello, I am an if statement and count is", count

#while the count is less than 10, executue this code
while count < 10:
  print "Hello, I am a while and count is", count
  count += 1
#
#
num = 1

while num < 11:  # Fill in the condition
  # Print num squared
  print num ** 2
  # Increment num (make sure to do this!)
  num += 1
#
#

choice = raw_input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
  choice = raw_input("Sorry, I didn't catch that. Enter again: ")

"""
you check if the user input does not equal y and n

if the user enters something invalid (like x), both condition are true, True and True is true, so the loop will run again. Which should happen, given we need to get new input

if the user enters valid input (for example y) one of the conditions is True while the other is False. True and False is false, so the loop stops (which it should, we have valid input)

on the other hand, using or will always result in true (True or True, True or False both evaluate to true), so the loop will keep running forever
"""

"""
While / else
while/else is similar to if/else, but there is a difference: the else block will execute anytime the loop condition is evaluated to False. 

This means that it will execute if the loop is never entered or if the loop exits normally. If the loop exits as the result of a break, the else will not be executed.
"""
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
  #input guess
  guess = int(raw_input("Your guess: "))
  #check if guess is correct
  if guess == random_number:
    print "You win!"
    break
  #if guess wasnt correct reduce gueses_left by 1
  guesses_left -= 1
else:
  print "You lose"
#
#
#
#This example means “for each number i in the range 0 - 19, print i“.
print "Counting..."

for i in range(20):
  print i
#
#
#
#
hobbies = []
#
# Add your code below!
for i in range(3):
  hobby = raw_input("Name a hobby of yours: ")
  hobbies.append(hobby)

print hobbies
#
#
#
"""
Question
Why do my hobbies have a ‘u’ before them when I print them?

Answer
This happens because raw_input() returns a unicode string, and that’s all the u means. If you’re seeing some output like this: [u'knitting', u'biking', u'coding'], that’s totally normal. Python is intentionally letting you know that the output is unicode.
To “fix” this, we can convert our hobbies to strings as we append them, like this: hobbies.append(str(hobby)).
"""
hobbies = []

# Add your code below!
for i in range(3):
  hobby = raw_input("Name a hobby of yours: ")
  hobbies.append(str(hobby))

print hobbies
#
#
#
#
#Using a for loop, you can print out each individual character in a string.
word = "eggs!"

# Your code here!
for i in word:
  print i
#
#
#
#
#replacing letters
#The , character after our print statement means that our next print statement keeps printing on the same line.
#
phrase = "A bird in the hand..."
# Add your for loop
for char in phrase:
  if char is "A" or char is "a":
    print "X",
  else:
    print char,
#Don't delete this print statement!
print
#
#
#
#
#print key and value from dictionary
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  # Your code here!
  print key, str(d[key])
#
#
#
#
#
#enumerate provides an index. as it starts at 0, add 1 so it looks more natural to the layperson
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
  print index + 1, item
#
#
#
#
#
#compare two lists and print the larger value
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  # Add your code here!
  print max(a,b)
#
#
##
#
#
#
#using for and else
#go through the list and give a response if it's a tomato, otherwise use the gneral response
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
  if f == 'tomato':
    print 'A tomato is not a fruit!' # (It actually is.)
  print 'A', f
else:
  print 'A fine selection of fruits!'
#
#
#
#
#
#
#
#check for eve numbers, return true if so
def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False
#
#
#
"""
Define a function is_int that takes a number x as an input.

Have it return True if the number is an integer (as defined above) and False otherwise.
"""
#
#potential error with this answer? how does it do with negative numbers?
from math import floor
def is_int(x):
  #if int or .0
  if floor(x) == x:
    return True
  else:
    return False
#
#
#
#
#
#
"""
Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number’s digits.
For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4. (Assume that the number you are given will always be positive.)
"""
def digit_sum(n):
  #create empty list
  answer = []
  for i in str(n):
    #use for to break n into single digits
    #add each value to list
    answer.append(int(i))
  #print the sum of all list values in answer
  print sum(answer)
  #return
  return sum(answer)
digit_sum(1234)
#
#a slightly cleaner way to do it is
def digit_sum(n):
  #create a var with value of 0
  answer = 0
  for i in str(n):
    #add each digit from n to answer
    answer += int(i)
  #print for visual confirmation
  print answer
  #return
  return answer
digit_sum(1234)
#
#
#
#
#
#
"""
FACTORIAL

To calculate the factorial of a non-negative integer x, just multiply all the integers from 1 through x. For example:

factorial(4) would equal 4 * 3 * 2 * 1, which is 24.
factorial(1) would equal 1.
factorial(3) would equal 3 * 2 * 1, which is 6.
"""
#
#https://www.youtube.com/watch?v=6xpwQn-TqAQ
def factorial(x):
  #define the factorial as 1, as we need to work from 1 not 0
  fact = 1
  #need to loop from 1 up to x
  for i in range(x):
    fact *= i+1
  print(fact)
  #return the factorial
  return fact
#trigger function  
factorial(4)
#
#
#CHECK FOR PRIME NUMBERS
#
#define function
def is_prime(x):
  #check if x is below 2 as prime numbers are 2 and up
  if x < 2:
    return False
  else:
    #start for range from 2
    for n in range(2, x-1):
      #test if x is evenly divisible by n
       if x % n == 0:
         return False
  #otherwise must be prime so return true
  return True
#
#
#
#
#this was a ball ache and kind of a cheat method to print the reverse text
#Create a function that reverses a string of text
def reverse(text):
  #define empty var to hold reversed text
  backwards = ""
  #get all the characters
  for i in text:
    #each character is added to the string using a prefix, ending up with the text 'reversed'
    backwards = i + backwards
  #print to check
  print backwards
  #return reversed text
  return backwards
#
#
#
#
#
#
#function to remove vowels from string
def anti_vowel(text):
  #make an empty variable to store the no vowel results
  result = ""
  #define the vowels to be checked against
  vowels = "aeiouAEIOU"
  #for the characters in the text input
  for char in text:
    #if the character doesn't match a vowel
    if char not in vowels:
      #append the result to the result list
      result += char
      #otherwise do nothing if it is in
  #return overall result - this is why it sits outside and after the loop
  return result
#print the anti vowel function with the "Hello Book" input processed through it
print anti_vowel("Hello Book")
#
#
#
#
#
#score list
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
#function to calculate scrabble score
def scrabble_score(word):
  #set all characters to lower case to match against the library
  word = word.lower()
  #empty var to hold points value. using 0 to have var hold int
  points = 0
  #loop through letters in word
  for x in word:
    #loop through letters in score library
    for y in score:
      #if the two letters match
      if x == y:
        #update the points total by summing points and score correspoonding int value
        points = points + score[y]
  #retur points
  return points
#input
print scrabble_score("Thorough")
#
#
#
#
#censorship!
def censor(text, word):
  #create an empty array to store censored version of text
  sentence = []
  #for the 'term' within the split text array
  for term in text.split():
    #if term matches word
    if term == word:
      #replace word with * number matching word length
      sentence.append("*" * len(word))
    else:
      #otherwise add unmodified term to sentence
      sentence.append(term)
  #return joined modified sentence
  return " ".join(sentence)
print censor("my favourite thing to eat is pizza and day old pizza", "pizza")
#
#
#
#
#
#count number of items in sequence
def count(sequence, item):
  #result var set at 0 to start
  result = 0
  #look through sequence
  for i in sequence:
    #if i matches item
    if i == item:
      #update count value by 1
      result += 1  
  #return result
  return result
print count([1, 2, 3, 4, 1], 1)
#
#
#
#
#filter odd numbers from list
def purify(x):
  #create empty even list
  evens = []
  #for each number in x
  for i in x:
    #check if even
    if i % 2 == 0:
      #and append to evens list
      evens.append(i)
      #otherwise do not
  #return
  print evens
  #return all evens values
  return evens
print purify([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#
#
#
#
#
#multiply
def product(n):
  #result var set as 1 as can't multiply by zero
  result = 1
  #for each number in n, multiply against result and add that outcome to result
  for i in n:
    result *= i
  return result
print product([4, 5, 6])
#
#
#
#
