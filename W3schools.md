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
