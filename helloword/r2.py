# # 创建文件对象，r表示读取文件
# f = open('E:/info.txt', 'r')
# # w = open('E:/2.txt', 'w')
# # 读取文件，每次读取一行
# line = f.readline()
# # 当读取内容不为空时执行写文件操作
# while line:
#     # w.write(line)
#     print(line)
# # w.flush()
#
# # f.close()
f = open('E:/pdf1/pdf.txt', 'r', encoding='utf-8')
# 创建输出文件，指定编码格式
w = open('E:/2.txt', 'w', encoding='utf-8')
result = ''
for line in open('E:/pdf1/pdf.txt', encoding='utf-8'):
    line = f.readline()
    print(line)
    # 判断该行是否包含该字符串，如果包含则写入文件
    result = result + line
    if 'Introduction' in line:
        # result = result+line
        break

print(result)
w.write(result)
w.flush()
f.close()