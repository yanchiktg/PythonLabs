import math

x = int(input("Input x = "))
y = int(input("Input y = "))
z = int(input("Input z = "))
print("You enter x, y, z: ", x, y, z)


chisl = int(abs(math.tan(z/2) + 2 - (math.pow(y,3))))
print("chisl =  ", chisl)

znam = int(math.pow(x,3) + 2 + math.tan(y/2))
if(znam <= 0):
  print("Error!")
print("znam =  ", znam)
chz = chisl/znam
test = math.log(abs(chz), 10)

test2 = (math.exp(x) + 1)
if(test2 <= 0):
  print("Error!")    
second = x/test2
print("second =  ", second)

test3 = (y + 3)
if(test3 <= 0):
  print("Error!") 
third = y/test3
print("third =  ", third)

b = (1/(math.sqrt(3)))* test * second + third
print("b =  ", b)
