def factorial_recrisive(n):
    if (n > 0):
        result = n +factorial_recrisive(n - 1)
        print(result)
    else: 
        result = 0
    return result

factorial_recrisive(6)


def recursion(k):
    if (k > 0):
        answer = k + recursion(k - 1)
        print(answer)
    else:
        answer = 0
    return answer

recursion(5)