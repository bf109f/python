"""
内存引用
"""


def test(num):
    print("函数内部的内存地址 %d" % id(num))
    result = "hello"
    print("result 的内存地址%d " % id(result))
    return result


def meause():
    # 温度
    temp = 30
    # 湿度
    wetness = 50
    # 返回的是元组  （）可以省略
    return temp, wetness


a = 10
# id()查看内存地址
print("a的内存地址 %d" % id(a))
print(id(test(a)))
result = meause()
# 取数据
print("温度 %d" % result[0])
print("湿度 %d" % result[1])
gl_temp, gl_wetness = result
print(gl_temp)
print(gl_wetness)