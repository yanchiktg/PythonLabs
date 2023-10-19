"""
Дано целое число 
N (> 0). Используя один цикл, найти сумму 
1! + 2! + 3! + … + N!
"""
import math

def main():
    N = 0
    while True:
        N = int(input("Введите целое число N = "))
        if(N > 0):
            break
    sum = 0
    for i in range(1, N+1):
        sum += math.factorial(i)
    print("Сумма = ", sum)

if __name__ == "__main__":
    main()
