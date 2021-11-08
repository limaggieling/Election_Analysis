#3.2.1 Creating a Python File
# VS Code lets you know if you have syntax errors, helps with bracket matching and indentation
# simply open a folder and add a .py file
# can connect GitHub account to track edits

# 3.2.2 Execute Python Files
print("Hello World!")
# this is the code we will run
# if there is a white dot next to the file tab, it means it has been edited but not saved
# save by hitting ctrl+s
# python is case sensitive, ex: Print("") is the incorrect syntax for the print command, it must be lowercase
# run command in terminal after saving by right clicking the file name in the explorer and selecting run in terminal
# the output will look like this
# C:/Users/tom/Python36/python.exe = command to run python
# c:/Users/tom/Desktop/Election_Analysis/Python_practice.py is the location of the file executed
# Hello World! is the result of the executed file
# terminal prompt appears waiting for the next command

# 3.2.3 Data types
# Integers =  whole neg or pos numbers 
# length of integer is dependent on computer RAM, ex: 8GB RAM has 8 billion bytes and the integer 10 quintillion (thats 20 digits) takes up only 36 bytes
# Whole numbers between –32,768 and 32,767 are stored in 16 bits, and whole numbers between –2,147,483,648 and 2,147,483,647 are stored in 32 bits

# type() function will tell you the data type of the thing you write between the () (could be a variable, number, string) do not use commas for your numbers

# Tuple = a data type that has 2 numbers ex: (1, 3), usually set equal to a variable and then the type(variable) funciton is used on the variable name
# Float = Floating-point decimal numbers, numbers that have decimals
# Str = strings and they are always between single or double quotes
# bool = boolean values aka true or false

# Variable Names
# declaring variables means setting it equal to something
# upper, lower case, numbers, underscores, thats it
# are case sensitive and they gotta be connected with underscores if you wanna space it out, aka Snake Case
# certain keywords are reserved and therefore variables cannot be named them
# You can also get this list if you type help("keywords") in the command line.

# 3.2.4 Perform Calculations using Python
# Arithmatic Operators: +,-,*,/(returns float),%,//(returns integer),** (exponential power)

# 3.2.5 Data Structures: Lists
# List = array that contains multiple data types
# Lists are mutable, dynamic, utilize indexing and slicing for data retrieval

mylist = list()
counties = ['arapahoe','denver','jefferson']

# An empty list can be declared with the following syntax: my_list = [ ]. Alternatively, you can use the built-in function list() to create an empty list: my_list = list().
# An index of a variable is its position in the array. Here are some general rules for indexing:
# Each item in a list has an index that specifies its position in the list.
# Indexing starts at 0. Therefore, the index of the first item is 0, the index of the second number is 1, and so on.
# Because indexing begins at 0, the index of the last item in a list is 1 less than the number of items in the list.
counties[0]
print(counties[2])
# negative indexes show location relative to the end of the list ex: last item would be print(counties[-1])
len(counties)
# gives the length of the list

# Slicing is used to get specific items from a list. The format for slicing a list is as follows: list[start : end].
# let's break down how slicing works.
#The start refers to the index of the first item in the slice.
#The end is the index marking the end of the slice.
#The expression list[start : end] returns a list containing a copy of the items in the list from the starting index value up to, but not including, the ending index value.
# >>> counties[0:2]
#['Arapahoe', 'Denver']
#>>> counties[0:1]
#['Arapahoe']
#>>> counties[:2]
#['Arapahoe', 'Denver']

# Add Items to list
# items added by append() command
# syntax is list.append(data you wanna add)
# ex: counties.append('el paso')
# will always add item to end of list
# to insert at a specific location use list.insert(index,obj) where index is the location you want the object to have in the list
#  >>> counties.insert(2, "El Paso")
#>>> counties
#['Arapahoe', 'Denver', 'El Paso', 'Jefferson', 'El Paso']
# remove items by using the .remove('obj') command or the .pop(index)
#counties.remove('el paso')
#counties.pop(3)

# Change an item in the list
# counties[2] = 'el paso'
# this declares the location to be changed and sets it to a new value 

# functions of python https://docs.python.org/3.7/library/functions.html

# 3.2.6 Data Structures: Tuples
# tuples similar to lists but cant be changed (no adding or removing) after created
# create empty tuple : my_tuple = () or my_tuple = tuple()
# counties_tuple[:2] is the same as counties_tuple[:-1]

# 3.2.7 Data Types: Dictionaries
# dictionary is an object that stores a collection of data
# A Python dictionary has a key and a value, or key-value pairs. Very similar to a dictionary that contains definitions, the words in the dictionary would be considered the keys, and the definitions of those words would be the values.
# syntax for dictionaries is: {key:value} and  {key1:value1, key2:value2}
# values can be any kinda data type
# keys must be immutable objects of any kind
# create a dictionary
# To initialize or create an empty dictionary, we use the following syntax: my_dictionary = {}. Or you can create a dictionary with the built-in Python dict() method, my_dictionary = dict().
# The standard format for creating a key in a dictionary is to place the key between single or double quotes and inside brackets.
#>>> counties_dict["Arapahoe"] = 422829 aka counties_dict["key"] = value 
# can also get len(counties_dict)
# get all keys and values by endering the dictionary name or use the .items() command
# would look like this: >>> counties_dict.items()
# view object is anything outputed in between the dict_XXX([''])
# get just keys with .keys()
# get just values with .values()
# items(), keys(), values() all return a view object on python
# Get a specific value with .get()
# can also use any of the following:
#counties_dict['Arapahoe'] 
#counties_dict.get("Arapahoe")  
#print(counties_dict['Arapahoe'])  
#print(counties_dict.get("Arapahoe"))
#key needs to be wrapped in '' or ""

# List of Dictionaries
# >>> voting_data = []
# >>> voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# >>> voting_data.append({"county":"Denver", "registered_voters": 463353})
# >>> voting_data.append({"county":"Jefferson", "registered_voters": 432438})
# output is >>> voting_data 
# [{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}
#Take a look at this code. This is a list of dictionaries because each element in the list is a dictionary. The keys are "county" and "registered_voters."
#The format of a CSV file is like a list of dictionaries, where the headers (column names) "county" and "registered_voters" are the keys, and the values are the data in the rows. If you added this data to a CSV file it would look like this.
# all list methods can be used on the list of dictionaries

# 3.2.8 Decision Statements
# aka Conditional statements, if statements, if else statements
# word if is followed by a condition that is evaluated as either true or false
# the following code is to be run after the evaluation must be indented, this is the only way for python to know where the code begins and ends
# == is the boolean comparison operator meaning "equal to"
# != "is not equal"
# Dual-alternative decision statment is the if-else statement
# a : must be used to end the condition
# Nested if-else statements
# Example
# # What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

# The length of the decision structure determines whether you use a nested if-else statement or the if-elif-else statement. If you have to scroll horizontally on your computer screen to see all the code in an if-else statement , then you should use an if-elif-else statement.

# 3.2.9 Membership and Logical Operators
# "in" is an operator that returns true if the sequence is found in the object, "not in" returns true if the sequence is not in the object
counties = ["Arapahoe","Denver","Jefferson"] 
if "Arapahoe" in counties: 
    print("True") 
else: 
    print("False")

if "El Paso" not in counties: 
    print("True") 
else: 
    print("False")

# logical operators
# "and" , "or" , and "not" connect multiple comparison expressions to create a compound expression

# 3.2.10 Repetition Statements
# loops in python
# condition-controlled loop aka While loop, as long as condition remains true, the loop will continue
# count-controlled loop aka For loop, a set number of repetitions is determined
x = 0
while x <= 5:
    print(x)
    x = x + 1
# as long as x is less than 5 the loop continues

# Iterate through list or tuple
for county in counties:
    print(county)

numbers = [0, 1,2,3,4]
for num in  numbers:
    print(num)

for num in range(5):
    print(num)

# all three options will result in the same output

# iterate through dictionary
# to get keys
# use the same syntax as lists or tuples

counties_dict = {"Arapahoe": 422829, "Denver" : 463353, "Jefferson" : 432438}

for county in counties_dict:
    print(county)

# another way is to use the keys() method
for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)
# gives keys and values

# just get keys aka the counties
for county_dict in voting_data:
    print(county_dict['county'])

# just get values aka the vote count
#   value() method
for voters in counties_dict.value():
    print(voters)
#   get() method
for county in counties_dict:
    print(counties_dict.get(county))

# get a key-value pair of a dictionary
for key, value in dictionary_name.items():
    print(key, value)

for county, voters in counties_dict.items():
    print(county, voters)

# item method gives both key and value
# first variable is always assigned to keys, second to values
# f string print helps format a numerical value into a string and performs a calculation

print(f"I received {myVotes/totalVotes*100}% of the total votes.")
# can also print multiple lines
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("what is the total number of votes in the election? "))

message_to_candidate = (
    f"you received {candidate_votes} number of votes."
    f"the total number of votes in the election was {total_votes}."
    f"you received {candidate_votes/total_votes*100}% of the total votes."
)
print (message_to_candidate)

f'{value:{width},.{precision}}'
# allows to format the output number
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
# skill drill
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for key, value in counties_dict.items():
    print(f"{key} county has {value:,} registered voters.")

# skill drill
voting_data = [
    {"county":"Arapahoe", "registered_voters": 422829}, 
    {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for key, value in voting_data:
    print(f"{value} county has {[value]} registered voters.")
 