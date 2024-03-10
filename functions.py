# functions are used for code reusability
# function definition:
# a function will not be called by itself but programmer should call it ---- calling a function

def function_name1():
    print(2+2)   


function_name1()

# function parameters and passing arguments

def function_name2(parameter):
    print(parameter+2) #by default it is int

function_name2(10.0999)

# function with multiple parameters
first_string = "The Number "

def function_name3(p1, p2, p3):
    print(p1+str(p2)+p3) #by default is string

function_name3(first_string, 20, " is a integer.")

# default function

def default_example(num1=2, num2=4):
    print(num1 * num2)

default_example()
default_example(9) # 9*4=36
default_example(6,8) #6*8=48

# return

def ex(num1=2, num2=3):
    return num1 * num2

print(ex(3,1) + 10)

# excercise 1
def hello_world_printer():
    print("hello world")

hello_world_printer()

# excercise 2

name = input("Enter your name : ")

def name_printer(name):
    return name

name_printer(name)

# exercise 3 finding volume of rectangular prism v=l * b * h

# def volume(length, breadth, height):
#     print(length*breadth*height)

# volume(2,5,6)

length = int(input("Enter length : "))
breadth = int(input("Enter breadth : "))
height = int(input("Enter height : "))

def v1(l, b, w):
    return l * b * w


print("Volume of the rectangular prism is :" + str(v1(length, breadth, height)) + " tin cubic feet")















