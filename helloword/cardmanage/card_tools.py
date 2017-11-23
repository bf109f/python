# 记录所有的名片字典
card_list = []


def show_menu():
    """
    显示菜单
    :return:
    """
    print("*" * 50)
    print("欢迎使用【名片管理系统】")
    print()
    print("1、新增名片")
    print("2、显示名片")
    print("3、搜索名片")
    # print("4、修改名片")
    print()
    print("0、退出程序")
    print("*" * 50)


def new_card():
    """
    新增名片
    :return:
    """
    # 1、提示用户输入名片的详细信息
    name = input("请输入姓名")
    phone = input("请输入电话")
    qq = input("请输入qq")
    email = input("请输入邮箱")
    card_dict = {
        "name": name,
        "phone": phone,
        "qq": qq,
        "email": email
    }
    card_list.append(card_dict)


def show_all():
    """
    显示所有名片
    :return:
    """
    if len(card_list) != 0:
        # 打印表头
        for name in ["姓名", "电话", "qq", "邮箱"]:
            print(name, end="\t\t")
        print()
        print("-" * 50)
        # 遍历名片列表
        for card_dict in card_list:
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))
    else:
        print("列表为空")


def search_card():
    """
    搜索名片
    :return:
    """
    find_name = input("请输入要搜索的姓名")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tqq\t\t邮箱")
            print("-" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))
            deal_card(card_dict)
            break
    else:
        print("抱歉，未找到%s" % find_name)


def deal_card(find_dict):
    print(find_dict)
    action_str = input("请输入要执行的操作：1、修改 2、删除 0、返回上一级")
    if action_str == "1":
        print("修改名片")
        find_dict["name"] = input_card_info(find_dict["name"], "姓名")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话")
        find_dict["qq"] = input_card_info(find_dict["qq"], "qq")
        find_dict["email"] = input_card_info(find_dict["email"], "email")
    elif action_str == "2":
        # 删除名片
        card_list.remove(find_dict)
    elif action_str == "0":
        print("返回上一级")
    else:
        print("输入错误")


def input_card_info(dict_name, tip_message):
    """
    输入名片信息
    :param dict_name:字典中原有的值
    :param tip_message: 输入的提示文字
    :return: 如果用户输入内容则返回内容，否则返回原有的值
    """
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_name