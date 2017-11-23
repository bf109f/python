"""
名片管理系统
"""
# 导入工具包
from cardmanage import card_tools

while True:
    # TODO 显示功能菜单
    card_tools.show_menu()
    action_str = input("请选择需要执行的操作：")
    print("您选择的操作是%s" % action_str)
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            card_tools.new_card()
            pass
        elif action_str == "2":
            card_tools.show_all()
        else:
            card_tools.search_card()
        pass
    elif action_str == "0":
        print("欢迎再次使用")
        break
        # pass占位
        pass
    else:
        print("输入错误")