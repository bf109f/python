def change_position_1(num1, num2):
    """
    交换两个数字的位置（使用中间变量）
    :param 第一个数字
    :param 第二个数字
    :return: 交换后的数字
    """
    c = num1
    num1 = num2
    num2 = c
    return num1, num2


def change_position_2(num1, num2):
    """
    不使用中间变量
    :return:
    """
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    return num1, num2


def change_position_3(num1, num2):
    """
    python专有的解法
    :return:
    """
    # num1, num2 = (num2, num1)
    num1, num2 = num2, num1  # 多变量接收元组
    return num1, num2


def change_position_4(num1, num2):
    """

    :return:
    """
    return num2, num1


print(change_position_2(59, 108))