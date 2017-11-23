"""
列表 for循环
"""
list_name = ["张三", "李四", "王五"]
"""
迭代：顺序的从列表中获取数据，每一次循环过程中数据都会保存在name这个变量中
"""
for name in list_name:
    print(name)
# list_name.remove()
# print(list_name)


def demo(num_list):
    """
    列表的 += 操作  相当于 num_list.extend()
    :param num_list:
    :return:
    """
    num_list += num_list


gl_list = [1, 2, 3]
demo(gl_list)
print(gl_list)
