"""
Fibonacci
Дано целое число 
N (> 1). Последовательность чисел Фибоначчи FK определяется следующим образом: 
F1 = 1, F2 = 1, FK = FK–2 + FK–1, K = 3, 4, … .
Проверить, является ли число N числом Фибоначчи.
Если является, то вывести True, если нет — вывести False.
"""
def trueFib(N):
    fib1 = 1
    fib2 = 1
    fibSum = 1
    while(fibSum != N and fibSum < N):
        fibSum = fib1 + fib2
        fib1 = fib2
        fib2 = fibSum
        if(fibSum == N or N == 1):
            return True
    return False


def main():
    N = 0
    while True:
        N = int(input("Введите целое число N = "))
        if(N > 1):
            break
        
    if(trueFib(N)):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()
            
