"""Complete the following Python program to compute
the sum 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 recursively: """

def suma(x):
    if x == 1:
        return 1
    else:
        return x + suma(x-1)


suma(5)
"""sum(5) == 5 + sum(4)
          == 5 + 4 + sum(3)
          == 5 + 4 = 3 + sum(2)
          == 5 + 4 + 3 + 2 sum(1)
          == 5 + 4 + 3 + 2 + 1"""