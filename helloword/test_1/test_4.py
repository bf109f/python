
def print_stat_1():
    a = 1
    while a <= 5:
        print("*" * a)
        a += 1


def print_star_2():
    b = 1
    while b <= 5:
        c = 1
        while c <= b:
            print("*", end="")
            c += 1
        b += 1
        print()

# print不换行
# print("*", end="")
# print("*")


def multiple_table():
    """
    定义函数九九乘法表
    :return:
    """
    start = 1
    while start <= 9:
        row = 1
        while row <= start:
            # print(str(row) + " * " + str(start) + " = " + str(start*row), end="  ")
            # print("%d * %d = %.2d" % (row, start, (row * start)), end="  ")
            print("%d * %d = %d" % (row, start, (row * start)), end="\t")
            row += 1
        start += 1
        print()


# 调用函数
multiple_table()