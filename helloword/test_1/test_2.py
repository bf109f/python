x = input("第一个数字")
y = input("请输入第二个数字")
z = input("请输入运算符")
if z == "+":
    c = int(x) + int(y)  # int(x)将字符串转换为int
elif z == "-":
    c = int(x) - int(y)
elif z == "*":
    c = int(x) * int(y)
elif z == "/":
    c = int(x) / int(y)
else:
    c = "运算符错误"
print(c)
