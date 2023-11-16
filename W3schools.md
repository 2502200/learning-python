## 1) [Python - string exercises](https://www.w3schools.com/python/exercise.asp?filename=exercise_strings1)
#using 'len()' to print the length of a string
```
x = "Hello World"
print(len(x)) 
```
#accessing elements of a string using '[ ]'  
#indexing in python starts from '0'
```
txt = "Hello World"
print(txt[0])
```
#using a slicing syntax to get certain characters from a string   
#start and end index need to be specified
```
txt = "Hello, World"
print(txt[2:5])
```
#this will return characters from position 2 to 5, exlucing the character on the position 5

#'.strip()' to get a string without whitespace
```
txt = " Hello World "
print(txt.strip())
```
#'.upper()' to get the string in uppercase (changes just the output)
```
txt = "Hello World"
print(txt.upper())
```
#'.lower()' to get the string in lowercase
```
txt = "Hello World"
print(txt.lower())
```
#'.replace( , )' to replace characters within a string
```
txt = "Hello World"
print(txt.replace("H", "J"))
```
#'.split()' to convert a string into a list
```
txt = "The quick brown fox jumps over the lazy dog"
print(txt.split())
```
#using the '+' operator can merge two strings together
```
a = "Hi!"
b = " How are you"
c = a + b
print(c)
```
#'.format( )' can be used to combine strings and numbers -> variables are places in a position where '{}' are in a string
```
a = 23
b = "I'm {} years old"
print(b.format(a))
```
#'.find( )' finds specified value and the position of it in a string
```
txt = "I'm 23 years old and a student"
a = txt.find("old")
print(a)
```
or 
```
txt = "I'm 23 years old and a student"
print(txt.find("old"))
```
#the same can be done with '.index( )'

## 2) [Python - lists exercises](https://www.w3schools.com/python/exercise.asp?filename=exercise_lists1)
#created using '[ ]' = square brackets; to store multiple items in a single variable 

#items in a list have a defined order but can be added, removed or changed

#lists are collection data types which allow duplicate members

#'len( )' shows the amount items in a list 
```
fruits = ["apples", "bananas", "cherries", "oranges", "kiwi", "mango"]
print(len(fruits))
```
#printing certain items from lists, e.g. printing 2nd item from fruits list
```
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
```
#changing items in a list 
```
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print(fruits)
```
#'.append( )' to add items to the end of the list
```
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
```
#'.insert( )' to insert items to the list at a specified place
```
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
print(fruits)
```
#'.remove( )' to remove specified items from the list
```
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)
```
#negative indexing can be used to print last item of the list
```
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
```
#range of indexes can be used to get specified values from the list, the items will be printed as a part of new list
```
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
```

## 3) [Python - If...Else exercises](https://www.w3schools.com/python/exercise.asp?filename=exercise_ifelse1)

```
a = 50
b = 10
if a > b:
    print('Hello world')
```
```
a = 50
b = 10
if a != b:
    print('Hello world')
```
#the '!=' stands for 'not equal to'
```
a = 50
b = 10
if a == b:
    print('yes')
else:
    print('No')
```
#'else' is used for anything which isn't defined with previous conditions

#'==' stands for 'equal to'
```
a = 50
b = 10
if a == b:
    print('1')
elif a > b:
    print('2')
else:
    print('3')
```
#'elif' is used when previous conditions weren't true so other coditions should be tried instead

#'and' is used to combine conditional statements
```
a = 2
b = 2
c = 2
if a == b and c == d:
  print("Hello")
```
#'or' is another logical operator used for the same reason as 'and'
```
if a == b or c == d:
  print("Hello")
```
#indentation/whitespace is important to define the scope in the code
```
if 5 > 2:
 print("Five is greater than two!")
```
#if they're short, the 'if' and 'else' statements can be put on the same line
```
print("Yes") if 5 > 2 else print("No")
```
#'if' statments can be inside 'if' statments => nested 'if' statments
```
x = 22
if x > 20:
 print(True)
 if x > 30:
  print('greater than 30')
 else:
    print('not greater than 30')
```
#'not' is also a logical operator used to reverse the results of conditional statments
```
x = 22
if x > 20:
 print(True)
 if not x > 30:
  print('not greater than 30')
```

## 4)[Python - For loops exercises](https://www.w3schools.com/python/exercise.asp?filename=exercise_for_loops1)

#'for loops' => used to iterate over a sequence (list, string, set...); a set of statments will be once for each item in a sequence
```
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
```
#'continue' is used to 'skip' over an item (to not print it)
```
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue 
  print(x)
```
#'range()' is used to loop through a set of a specified number of times; it always starts from 0 in increments of 1 and it ends at a specified number(doesn't print it out though)
```
for x in range(6):
  print(x)
```
#'break' is used to exit the loop before it has finished looping through all the items
```
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
```
#loops can be nested inside loops => 'nested loop' => so the inner loop will be executed one time for each iteration of the outer loop
```
adj = ['red', 'big', 'tasty', 'delicious']
furits = ['apples', 'bananas', 'cherry']
for word in adj:
    for fruit in fruits:
        print(word, fruit)
```
#'else' can also be used in loops; specifies a block of code to be executed when the loop is finished
```
for x in range(20):
    print(x)
else:
    print('yey finished')
```
#the starting value and the increment in the 'range()' function can also be defined
```
for numbers in range(1,30,3):
    if numbers == 10: break
    print(numbers)
else:
    print('finished it')
```
#the block of code won't be executed if the loop breaks

## 5) [Python - Booleans exercises](https://www.w3schools.com/python/exercise.asp?filename=exercise_booleans1)

#booleans represent either: True or False

#Python will return boolean answer when two values are compared
```
print(10 > 9)
```
#in this case, the boolean answer will be True since 10 is greater than 9
```
print(10 == 9)
print(10 < 9)
```
#here the boolean answer will be: False

#'bool()' function evaluates any value and gives a True or False answer in return

#any value is True if it has some content; any string and list is True except empty ones and any number is True except 0
```
bool("abc")
```
or
```
print(bool("abc"))
```
#this string will give the answer True
```
print(bool(0))
```
#the number 0 gives the answer False

#the value False and None, as well as empty values like (), [], {}, '', "" give the answer False

#functions can also return a boolean answer, and based on the boolean answer a code can be executed
```
def myFunction():
    return True
if myFunction():
    print('yes')
else:
    print('no')
```
#the executed code will be yes
```
def myFunction():
    return True
if not myFunction():
    print('no')
else:
    print('yes')
```
#here the executed code will be yes as well

#'isinstance()' can also be used to determine the data type of an object
```
x = 200
print(isinstance(x, int))
```
#this will return True, since 200 is an integer
```
x = 200
print(isinstance(x, float))
```
#this will return False since 200 is not a float

## 6)[Python - Dictionary Exercises](https://www.w3schools.com/python/python_dictionaries_exercises.asp)

#dictionaries store data values ina  form of a key:values pairs/items, they are changeable, ordered and don't allow duplicates, created using curly brackets '{}'

#to get a value of a certain 'key name' from a dictionary, '.get("")' method can be used
```
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(car.get("model"))
```
#to change a value of a key in a dictionary, e.g. changing a value of the year from 1964 to 2020:
```
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car["year"]= 2020
```
#to add a new key:value pair, the same method can be used:
```
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car["color"] = "red"
```
#or '.update({"":""})' can be used to add new items, or to update old ones:
```
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.update({"color": "black"})
```
#'.pop("")' is used to remove the item with specified key name, from the dictionary
```
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.pop("model")
```
#'del' can also be used to remove item from the dictionary, with specified key name:
```
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
del car["model"]
```
#'.popiem()' removes last inserted item

#'.clear()' empties the dictionary
```
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.clear()
```
#'.copy()' is used to make a copy of a dictionary
```
car2 = car.copy()
```

