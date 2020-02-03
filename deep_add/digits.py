""" 3. We can determine how many digits a positive integer has by repeatedly dividing by 10
(without keeping the remainder) until the number is less than 10, consisting of only 1 digit.
 We add 1 to this value for each time we divided by 10. Here is the recursive algorithm: 1.
 If n < 10 return 1.2. Otherwise, return 1 + the number of digits in n/10 (ignoring the fractional part)."""

def digits(number):
    if number < 10:
        return 1
    else:
        return 1 + digits(number // 10)
