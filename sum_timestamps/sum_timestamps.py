def sum_timestamps(hours):
    if len(hours) == 1:
        return hours
    hour1 = hours[0].split(":")
    hour2 = hours[1].split(":")
    newhour = int(hour1[0]) + int(hour2[0])
    newminute = int(hour1[1]) + int(hour2[1])
    if int(newminute) > 59:
        newhour = int(newhour) + 1
        newminute = int(newminute) - 60

    if newhour > 23:
        newhour= int(newhour) - 24
    print( f"{newhour}:{newminute}")
    return f"{newhour}:{newminute}"


sum_timestamps(['5:32', '4:48'])
sum_timestamps(['03:10', '01:00'])
sum_timestamps(['2:10', '1:59'])