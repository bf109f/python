class Time:
    """
    表示一天的时间，属性hour、minute、second
    """


def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))


def is_after(t1, t2):
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)


def increment(time, seconds):
    time.second += seconds
    if time.second >= 60:
        time.second -= 60
        time.minute += 1
    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1
    return time


start = Time()
start.hour = 8
start.minute = 35
start.second = 22

end = Time()
end.hour = 8
end.minute = 34
end.second = 33
print(is_after(start, end))
print_time(start)
print_time(increment(start, 40))