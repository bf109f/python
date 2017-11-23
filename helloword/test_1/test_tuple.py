"""
元组：多个元素组成的序列，用“,”分割，用“()”定义，数据从0开始，一旦定义不能修改（增、删、改）
应用场景：
    1、保存不同类型的数据
    2、函数的参数和返回值
    3、格式化字符串，格式化字符串后面的()本质上就是一个元组 print("%s 年龄是 %d 身高是 %.2f" % ("小明", 18, 175.02))
    4、让列表可以不被修改
列表转元组：tuple(列表)
元组转列表：list(元组)
"""
info_tuple = ("张三", 18, 1.75)
for tup in info_tuple:
    print(tup)
print(info_tuple.index(18))
print(type(info_tuple))
print(info_tuple[0])
print(len(info_tuple))
print(type(list(info_tuple)))
print("%s 年龄是 %d 身高是 %.2f" % ("小明", 18, 175.02))