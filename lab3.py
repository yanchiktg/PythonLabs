"""
6. Описать процедуру DigitCountSum(K, C, S), находящую кол-во C цифр
целого положительного числа K, а также сумму S(K - входной, C и S - выходные
параметры целшого типа). С помощью этой процедуры найти кол-во и сумму цифр для
каждого из пяти данных целых чисел.
"""
def DigitCountSum(K, C, S):
    C = len(str(K))
    print("C = ", C)

    while (K != 0):
        S = S + K % 10
        K = K // 10
    print("S = ", S)
    return C, S

def main():
    K = 0
    check = 0
    
    while (check < 5):
        while True:
            K = int(input("Введите целое положительное число K = "))
            if(K > 0):
                break
        S = 0
        C = 0
        C, S =  DigitCountSum(K, C, S)
        check = check + 1

if __name__ == "__main__":
    main()
