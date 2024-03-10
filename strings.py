print("------------------String part - 1 ---------------------")

string1 = 'This is a string'
print(string1)
string2 = "This is also a string"
string3 = '#$%^&*()'
string4 = ''

print("------------------Accessing single character present in a string by index ---------------------")

ex_1 = 'Orange'
result = ex_1[4]
print(result)
print("Hello Shravani"[6])

print("------------------String slicing ---------------------")

ex_2 = 'Shravani'
print(ex_2[:3])
print(ex_2[2:4])
print(ex_2[2:])

print("------------------Concatenation---------------------")

print("Shr"+"ava"+"ni")

concatenated = "shr"+"ava"+"ni"
print(concatenated[4]) # v
print(concatenated[2:4]) # ra

# slicing a string or accessing a char from string, does not change string's original value
string = "forest road"
sliced_string = string[2:]
print(sliced_string)
print(string)

#excercise
str1 = "Just do it!"
print(str1[10])
print(str1[5:8])
print(str1[8:])
print(str1[:5])
print("Don't " + str1[5:])

# finding datatype of a variable using type()
var1 = 100
var2 = 100.00
var3 = False
print(type(var1))
print(type(var2))
print(type(var3))

# converting any datatype to a string using str()
  
# a is of type int 
a = 10
print("Type before : ", type(a)) 
  
# converting the type from int to str 
a1 = str(a) 
print("Type after : ", type(a1)) 

# Escape chars \t (tab), \n (new line), \', \", \\
print("My\tname\tis\tShravani")
print("What is your Name?\nMy name is Shravani")
print("My name is \'Shravani\'")
print("my name is \"Shravani\"")
print("my name is Shravani\\")

# coding challenge to print triangle
print("*******\n *****\n  ***\n   *")

# input() similiar to scanner in java 
# which ever data you pass in name by default its type will be string only
name = input("Please enter your name: ")
print("Your name is " + name + ".")
print(type(name))

fav_num = input("Enter your fav num : ")
print("Your fav num is : " + fav_num)
print(type(fav_num)) # even a number will treated as string

# Excercise

name = input("What is your name? ")
quest = input("What is your quest? ")
colour = input("What is your favorite color? ")
print("So your name is "+name+", your quest is "+quest+" and your favorite color is "+colour+"." )

# to make user input in int format then use int()
user_age = int(input("What is your age: "))
print(user_age)
print(type(user_age))

# to put string in a float use float()
Pi = float(input("What is the value of Pi is : "))
print(Pi)
print(type(Pi))

#int() excercise
value = int(input("Enter the value : "))
print(value+10)
print(type(value))

























