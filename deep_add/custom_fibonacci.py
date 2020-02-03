
def custom_fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return custom_fibonacci(n-1) + custom_fibonacci(n-2)




"""custom fibonnaci(5) = (1+1) + custom_custom_fibonacci(4)
                       = 2 + 1 + custom fibonacci(3)
                       = 3 + 2 + custom fibonnaci(2)
                       = 5 + 3 + custom fibonacci(1)
                       = 8 + 5"""




