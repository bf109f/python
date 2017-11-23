def cen_rig():
    """
    文本对齐
    """
    poem = [
        "登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"
    ]

    for pom in poem:
        # print("|%s|" % pom.center(10, " "))
        # print("|%s|" % pom.ljust(10, " "))
        print("|%s|" % pom.rjust(10, " "))


def trim():
    """
    去空格
    :return:
    """
    hello = " hello word "
    # 去除前后空格
    print(hello.strip())
    # 去除前面的空格
    print(hello.lstrip())
    # 去除后面的空格
    print(hello.rstrip())


def connect():
    """
    字符串拆分、连接
    :return:
    """
    hello = "hello word"
    # 拆分字符串
    pom_list = hello.split()
    # join连接字符串
    print("_".join(pom_list))


connect()