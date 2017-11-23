import sys
import importlib
import os
import os.path
import time
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
importlib.reload(sys)

'''
 解析pdf 文本，保存到txt文件中
'''

allFileNum = 0

def parse(path):
    fp = open(path, 'rb')
    # 以二进制读模式打开
    # 用文件对象来创建一个pdf文档分析器
    praser = PDFParser(fp)
    # 创建一个PDF文档
    doc = PDFDocument()
    # 连接分析器 与文档对象
    praser.set_document(doc)
    doc.set_parser(praser)

    # 提供初始化密码
    # 如果没有密码 就创建一个空的字符串
    doc.initialize()

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDf 资源管理器 来管理共享资源
        rsrcmgr = PDFResourceManager()
        # 创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        count = 0

        try:
            sp = open('E:/pdf1/pdf.txt', 'a+', encoding='utf-8')
            # 两文件之间的分隔符
            sp.write('===============================================================================' + '\n')
            sp.write('文件名：' + os.path.splitext(path)[0] + '.pdf\n')
            sp.write('===============================================================================' + '\n')
        finally:
            sp.close()

        # 循环遍历列表，每次处理一个page的内容
        for page in doc.get_pages():
            # doc.get_pages() 获取page列表
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
            # 想要获取文本就获得对象的text属性，
            print("count=" + str(count))
            if count == 1:
                break
            for x in layout:
                try:
                    if isinstance(x, LTTextBoxHorizontal):
                        results = x.get_text()
                        # print(results)
                        # filename = os.path.splitext(path)
                        # print(path)
                        # with open(filename[0] + '.txt', 'a+', encoding='utf-8') as f:
                        if 'Introduction' in results:
                            count = 1
                            return count
                        # with语句来自动帮我们调用close()
                        with open('E:/pdf1/pdf.txt', 'a+', encoding='utf-8') as f:
                            f.write(results + '\n')
                except Exception as e:
                    print(e)
                # print('执行完成')
                finally:
                    f.close()

    fp.close()


def printPath(level, path):
    global allFileNum
    ''''' 
    打印一个目录下的所有文件夹和文件 
    '''
    # 所有文件夹，第一个字段是次目录的级别
    dirList = []
    # 所有文件
    fileList = []
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    files = os.listdir(path)
    # 先添加目录级别
    dirList.append(str(level))
    for f in files:
        if os.path.isdir(path + '/' + f):
            # 排除隐藏文件夹。因为隐藏文件夹过多(Linux系统)
            if f[0] == '.':
                pass
            else:
                # 添加非隐藏文件夹
                dirList.append(f)
        if os.path.isfile(path + '/' + f):
            # 添加文件
            fileList.append(f)
            # 当一个标志使用，文件夹列表第一个级别不打印
    i_dl = 0
    for dl in dirList:
        if i_dl == 0:
            i_dl = i_dl + 1
        else:
            # 打印至控制台，不是第一个的目录
            print('-' * (int(dirList[0])), dl)

            # 打印目录下的所有文件夹和文件，目录级别+1
            printPath((int(dirList[0]) + 1), path + '/' + dl)
    for fl in fileList:
        # 打印文件
        print('-' * (int(dirList[0])), fl)
        parse(path + '\\' + fl)
        # 随便计算一下有多少个文件
        allFileNum = allFileNum + 1


if __name__ == '__main__':
    time1 = time.time()
    printPath(1, 'E:\\pdf')
    time2 = time.time()
    print('总文件数 =', allFileNum)
    print(u'ok,解析pdf结束!')
    print(u'总共耗时：' + str(time2 - time1) + 's')

    # path = r'E:/offer.pdf'
    # parse(path)