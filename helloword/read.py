# 读取文件返回一个文件对象,r表示读文件
f = open('E:/jianLi.sql', 'r')
line = f.read()
print(line)
# 创建文件对象，w写完文件
m = open('E:/1.txt', 'w')
m.write(line)
m.flush()
f.close()

