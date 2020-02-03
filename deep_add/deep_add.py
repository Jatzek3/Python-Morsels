def deep_add(numbers):
    sum = 0
    if isinstance(numbers, (int or float)):
        return sum + numbers
    elif numbers == []:
        return sum
    elif type(numbers) == list:
        for i in numbers:
            sum += deep_add(i)
        return sum
    else:
        pass

