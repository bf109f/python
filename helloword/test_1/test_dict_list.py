"""
字典与列表结合，将字典保存到列表中
"""
card_list = []
dict_1 = {
    "name": "小明",
    "age": 18
}
dict_2 = {
    "name": "特朗普",
    "age": 60
}
# dict_3 = {}
card_list.append(dict_1)
card_list.append(dict_2)
# card_list.append(dict_3)
print(card_list)
find_name = "奥巴马"
"""
for...else
"""
for info in card_list:
    if info['name'] == find_name:
        print("找到了 %s" % info["name"])
        break
else:
    print("未找到 %s" % find_name)