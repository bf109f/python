"""
切片，截取
"""
string_num = "0123456789"
# 2为步长
print(string_num[2:9:2])
print(string_num[2:])
print(string_num[::2])
print(string_num[-1::-1])
# 步长-1表示从右向左切
print(string_num[::-1])