"""
字符串
"""
name = "hello word"
# 索引
print(name[0])
# 长度
print(len(name))
# 出现次数
print(name.count("l"))
# 某个字符串(子字符串)在字符串中的位置 子字符串不存在会报错
print(name.index("l"))
# find方法 不存在返回-1
print(name.find("h"))
for info in name:
    print(info)
