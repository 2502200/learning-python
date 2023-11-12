# ***Begginer Python Exercises***
## 1) print() function

1-a: 

print("Hello World")

1-b: 
```
my_text = "Hello World"
print(my_text)
```
           
1-c: 

print("Hi!", "How are you?")

## 2) variables

2-a: glass_of_water = 3

2-b: print(glass_of_water)

## 3) data types

3-a: 
```
  men_stepped_on_the_moon = 12
  print(man_stepped_on_the_moon)
```

3-b: 
```
my_reason_for_coding = "It's interesting and fun"
print(my_reason_for_coding)
```
3-c:
```
global_mean_sea_level_2018=21.36


print(global_mean_sea_level_2018)
```
3-d:
```
staying_alive= True
print(staying_alive)
```
## 4) type conversion exercises

4-a:
```
men_stepped_on_the_moon=12
answer_1=type(men_stepped_on_the_moon)
print(answer_1)
```
4-b:
```
my_reason_for_coding="intergalactic travel"
answer_2=type(my_reason_for_coding)
print (answer_2)
```
4-c:
```
global_mean_sea_level_delta_2018=21.36
answer_3=type(global_mean_sea_level_delta_2018)
print(answer_3)
```
4-d:
```
staying_alive=True
answer_4=type(staying_alive)
print(answer_4)
```
4-e:

#converting a string into an integer [ int() ]
```
my_grade="10"
answer_5=int(my_grade)
print(answer_5)
```
4-f:

#converting a float (decimal number) into integer (whole number); also [ int() ]
```
my_temp=97.70
answer_6=int(97.70)
print(answer_6)
```
4-g:

#converting a string into a float [ float() ]
```
shoe_price="69.99"
answer_7=float(shoe_price)
print(answer_7)
```
4-h:

#converting data into a string [ str() ]
```
gross_world_product=84.84
gwp_str=str(gross_world_product)
answer_8="In 2018 gross product of the world (GWP) was " + gwp_str + " in trillion US dollars."
print(answer_8)
```

## 6) list exercises

#assigning an element to the list [ lst[] ], first element on the list is 0

6-a:
```
lst=[11, 100, 99, 1000, 999]
answer_1=lst[0]
print(answer_1)
```
6-b:
```
lst=[11, 100, 99, 1000, 999]
print(lst[1])
```
6-c:
```
lst=[11, 100, 99, 1000, 999]
answer_1=lst[-1]
print(answer_1)
```
#[-1] is used when printing the last element on the list

6-d:

#adding elements on the list [ .append() ]
```
gift_list=['socks', '4K drone', 'wine', 'jam']
gift_list.append("pajamas")
print(gift_list)
```
6-e:

#[ .append()] can be used for appending another list in an existing list
```
gift_list=['socks', '4K drone', 'wine', 'jam']
gift_list.append(["socks","tshirt","pajamas"])
print(gift_list)
```
6-f:

#[ .insert() ] can be used to add a specific element into the list at a specified place
```
gift_list=['socks', '4K drone', 'wine', 'jam']
gift_list.insert(2,"slippers")
print(gift_list)
```
6-g:

#[ .index() ] shows index number of an element in the list
```
lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
answer_1=lst.index(8679)
print(answer_1)
```

6-h:

```
lst=["CRV", "Outback", "XC90", "GL", "Cherokee", "Escalade"]
lst.append(["Navigator","Suburban"])
print(lst)
```

6-i:

#[ .remove() ] is used to remove the last item on the list
```
lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
lst.remove(99)
print(lst)
```

6-j:

#[ .reverse() ] is used for reversing the list
```
lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
lst.reverse()
print(lst)
```
6-k:

#[ .count() ] to get the number of times that an element has appeared on the list
```
lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
answer_1=lst.count(6)
print(answer_1)
```
6-l:

#'.sum(lst)' to see the sum of all the numbers on the list
```
lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
answer_1=sum(lst)
print(answer_1)
```
6-m and 6-n:

#'min(lst)9 to get the lowest value in the list and 'max(lst)' to get the highest value in the list
```
lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
answer_1=min(lst)
print(answer_1)
```
```
answer_1=max(lst)
print(answer_1)
```
# 9) string exercises

#always inside quotation marks

9-a:
```
str="It's always darkest before dawn."
print(str)
```
9-b:

#creating a new string from, the existing one, using the 'str[]' and adding the index number of the element we want to use
```
str="It's always darkest before dawn."
ans_1=str[0]+str[1]+str[-1]
print(ans_1)
```
9-c:

#[ .replace() ] for replacing items in a string
```
str="It's always darkest before dawn."
str=str.replace(".","!")
print(str)
```
9-d and 9-e:

#[ .lower() ] for lowercase characters and [ .upper() ] for uppercase characters
```
str="EVERY Strike Brings Me Closer to the Next Home run."
str=str.lower()
print(str)
```
```
str="don't stop me now."
str=str.upper()
print(str)
```
9-f:

#to cappitalize the first letter [ -capitalize() ]
```
str="there are no traffic JamS Along The extra mile."
str=str.capitalize()
print(str)
```
9-i:

#to get the index of a character [ .index() ]
```
str="The best revenge is massive success.
ans_1=str.index('v')
print(ans_1)
```
9-j:

```
str="The best revenge is massive success."
ans_1=str.find('m')
print(ans_1)
```

## 11) sort exercises

11-a:

#to sort the list in ascending order [ .sort() ]
```
lst=[11, 100, 99, 1000, 999]
lst.sort()
print(lst)
```

## 8) [For loop exercises](https://holypython.com/intermediate-python-exercises/exercise-8-python-for-loop/)

8-a:
```

lst=["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
for animal in lst:
    print(animal)
```
8-b:
```
lst=["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
for name in lst:
    print("Hello!, " + name)
```
8-c:
```
str="Antarctica"
for letter in str:
    print(letter)
```
8-d:
```
