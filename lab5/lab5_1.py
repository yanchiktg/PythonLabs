import math

def func(x, y, z):
    chisl = int(abs(math.tan(z/2) + 2 - (math.pow(y,3))))
    #print("chisl =  ", chisl)

    znam = int(math.pow(x,3) + 2 + math.tan(y/2))
    if znam <= 0:
        raise ArithmeticError("Знаменатель не может быть равен нулю!")
    #print("znam =  ", znam)
    chz = chisl/znam
    test = math.log(abs(chz), 10)

    
    test2 = (math.exp(x) + 1)
    if (test2 <= 0):
      raise ArithmeticError("Error!")    
    second = x/test2
    #print("second =  ", second)

    test3 = (y + 3)
    if test3 <= 0:
        raise ArithmeticError("Знаменатель не может быть равен нулю!") 
    third = y/test3
    #print("third =  ", third)

    b = (1/(math.sqrt(3)))* test * second + third
    print("b =  ", b)

try:
    x = int(input("Введите число x = "))
    y = int(input("Введите число y = "))
    z = int(input("Введите число z = "))
    print("Вы ввели x, y, z: ", x, y, z)
    func(x, y, z)
except ValueError as e:
    print("Вы должны ввести число!\n", e)
except ArithmeticError as e:
    print("Ошибка: ", e)
finally:
    print(":)")
