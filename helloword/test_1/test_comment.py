"""
公共的方法：内置函数
"""
print("abc" < "abd")
# *号
print("a" * 5)
print([1, 2] * 5)
print((1, 2) * 5)
# +号
print("a" + "b")
print([1, 2] + [3, 4])
print((1, 2) + (3, 4))
# in/not in  字符串、列表、元组、字典（key）
print(1 in [1, 2])
print(3 not in [1, 2])

"""
完整的for循环（for...else） 如果循环体内部使用了break推出了循环，else中的代码不会被执行
应用场景：
    
"""
for num in [1, 2, 3]:
    if num == 2:
        break
else:
    print("程序执行结束")