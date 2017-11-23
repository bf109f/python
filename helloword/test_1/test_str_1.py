"""
判断类型的方法
"""
str_hello = "hello word"
# 判断只是空白字符 空格 \t、\r、\n
print(str_hello.isspace())
# 判断字符串中只包含数字
num_str = "一千零一"
print(num_str)
"""
判断数字的三个方法：
    1、这三个方法都不能判断小数
    2、unicode字符串 \u00b2 (1)
    3、中文数字 “一千零一”
"""
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())