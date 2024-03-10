var1 = 10
var2 = 19
print(var1%var2)
# print("gfhdfdsuf")

#Mathematical operators in Python

print("------------------Mathematical operator---------------------")


sum = 4+5  # 9
print(sum)

diff = 4-5
print(diff)

prod=4*5
print(prod)

div=5/2
print(div)

exponentiation = 4**2 # 2*2*2*2
print(exponentiation)

floor_division = 16//5 # 16/5 = 3.2 and it gets rounded off to 3
print(floor_division)

modulo = 7%3 # it gives the remainder
print(modulo) 

#Assignment operator

print("------------------Assignment operator---------------------")

add_assign = 5
add_assign += 5 #adding 5+5 = 10
print(add_assign)

sub_assign = 5
sub_assign -= 5 #sub 5-5 = 0
print(sub_assign)

prod_assign = 5
prod_assign *= 5 #prod 5*5 = 25
print(prod_assign)

div_assign = 5
div_assign /= 5 #div 5/5 = 1.0
print(div_assign)

exponentiation_assign = 5
exponentiation_assign **= 2 #expo 5*5 = 32
print(exponentiation_assign)

floor_division_assign = 5
floor_division_assign //= 2 #floor_division_assign 5/2 = 2.5 roundoff it becomes 2
print(floor_division_assign)

modulo_assign = 5
modulo_assign %= 2 #modulo_assign 5%2 = 1 
print(modulo_assign)

print("------------------Operator presedence example---------------------")

exp = (9-7)* 2 ** 3 + 10 % 6 // -1 * 2 - 1
print(exp)

print("------------------Rounding---------------------")

var = (1.23+2.80)
print(var) 
print(round(var,2))

var = 16.68+6.98+16.78+15.26+3.00+4.39
print(16.68+6.98+16.78+15.26+3.00+4.39)
print(round(var,2))

  
# a is of type int 
a = 10
print("Type before : ", type(a)) 
  
# converting the type from int to str 
a1 = str(a) 
print("Type after : ", type(a1))







