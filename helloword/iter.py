# 创建要写入的文件
with open('E:/3.txt', 'a', encoding='UTF-8') as w:
    # 创建文件对象，r表示读取文件
    with open('E:/jianLi.sql', 'r') as f:
        # 使用迭代器读取文件
        iter_f = iter(f)
        # 记录行数
        lines = 0
        for line in iter_f:
            lines += 1
            print(lines)
            # print(line)
            if 'table' in line:
                w.write(line)
# w = open('E:/2.txt', 'w')
# # 读取文件，每次读取一行
# line = f.readline()
# print(line)
# 当读取内容不为空时执行写文件操作
# while line:
#     w.write(line)
#     print(line)
# w.flush()

# f.close()