def parse_ranges(list):
    matrix = []
    ranges = list.split(',')
    for i in ranges:
        matrix.append(i.split("-"))
    parsed_ranges_values = []
    for item in matrix:
        start = int(item[0])
        stop = int(item[1]) + 1
        parsed_ranges_values += range(start, stop)
    return parsed_ranges_values









parse_ranges('0-0, 4-8, 20-20, 43-45')
parse_ranges('1-2,4-4,8-10')