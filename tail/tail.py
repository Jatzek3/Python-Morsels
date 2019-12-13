def tail(iterable, end):
    if 0 > end:
        return []
    elif end > len(iterable):
        return list(iterable)
    else:
        list1 = list(iterable)
        print(list1[(len(iterable) - end):])
        return list1[(len(iterable) - end):]





tail("12367123672", 3)
