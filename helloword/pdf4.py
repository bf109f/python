import os


# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        # .decode('gbk')是解决中文显示乱码问题
        print(child)


# 读取文件内容并打印
def readFile(filename):
    # r 代表read
    fopen = open(filename, 'r')
    for eachLine in fopen:
        print("读取到得内容如下：", eachLine)

    fopen.close()


# 输入多行文字，写入指定文件并保存到指定文件夹
# def writeFile(filename):
#     fopen = open(filename, 'w')
#     print("\r请任意输入多行文字", " ( 输入 .号回车保存)")
#
#     while True:
#         aLine = raw_input()
#         if aLine != ".":
#             fopen.write('%s%s' % (aLine, os.linesep))
#         else:
#             print
#             "文件已保存!"
#             break
#     fopen.close()


if __name__ == '__main__':
    filePath = "E:\codeStyle\\CodeFormatter.xml"
    # filePathI = "D:\\FileDemo\\Python\\pt.py"
    filePathC = "E:/"
    # eachFile(filePathC)
    readFile(filePath)
    # writeFile(filePathI)