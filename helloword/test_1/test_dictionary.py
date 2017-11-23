"""
列表是有序的对象集合
字典是无序的对象集合
字典用{}定义相当于json数据
    key是唯一的、且只能是数字、字符串、元组
"""
xiao_ming = {"name": "小明",
             "age": 18,
             "gender": True,
             "height": 175.0,
             "weight": 66}
temp_dict = {"birthday": "1995-12-13",
             "age": 20}
# k 是每次循环中字典的key
for k in xiao_ming:
    print("%s - %s" % (k, xiao_ming[k]))
# 字典的合并
xiao_ming.update(temp_dict)
# 字典的长度
print(len(xiao_ming))
# 取值
print(xiao_ming["name"])
# 新增
xiao_ming["class"] = "1班"
# 修改
xiao_ming["name"] = "普京"
# 删除
xiao_ming.pop("gender")
# 获取key
print(xiao_ming.keys())
# 清空
xiao_ming.clear()
print(xiao_ming)