# def factorial_iter(n):
#    result = 1
#    for i in range(2, n + 1):
#       result *= i
#  return result


def factorial_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_rec(n - 1)


# print("Iterativ:", factorial_iter(5))  
print("Rekursiv:", factorial_rec(5))    