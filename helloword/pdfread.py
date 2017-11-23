from PyPDF2.pdf import PdfFileReader
import pymysql
import os
import os.path
from time import strftime, strptime


def sqlupdate(sql):
    conn = pymysql.connect(host="xxx.xxx.xx.xxx", port=3306, user="***", password="***", database="db_name")
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()


def getDataUsingPyPdf2(filename):
    pdf = PdfFileReader(open(filename, "rb"))
    content = ""
    for i in range(0, pdf.getNumPages()):
        extractedText = pdf.getPage(i).extractText()
        content += extractedText + "\n"
        # return content.encode("ascii", "ignore")
    return content


def removeBlankFromList(list_old):
    list_new = []
    for i in list_old:
        if i != '':
            list_new.append(i)
    return list_new


if __name__ == '__main__':
    rootdir = '/root/'
    for dirpath, dirnames, filenames in os.walk(rootdir):
        filedir = dirpath.split('/')[-1]
        for filename in filenames:
            filename = filename
            filename_long = dirpath + '/' + filename
            outputString = getDataUsingPyPdf2(filename_long)
            # outputString = getDataUsingPyPdf2("/root/a.pdf")
            outputString = outputString.split('\n')
            outputString_new = removeBlankFromList(outputString)
            outputString = outputString_new
            try:
                rectime = strftime('%Y-%m-%d %H:%M:%S', strptime(outputString[1].rstrip(' '), "%a %b %d %Y %H:%M:%S"))
            except:
                rectime = strftime('%Y-%m-%d %H:%M:%S', strptime(outputString[-1].rstrip(' '), "%a %b %d %Y %H:%M:%S"))
            pn = outputString[0].split()
            if len(pn) > 1:
                sn = pn[1]
            else:
                sn = ''
            pn = pn[0].strip()
            # print('[%s],[%s],[%s]' % (pn,topbut,rectime))
            sql = "insert into tb_1(pn,sn,rectime,dir,filename) values ('%s','%s','%s','%s','%s')" % (
            pn, sn, rectime, filedir, filename)
            print('sql=[%s]' % sql)
            sqlupdate(sql)
            print('done')
            # print(getDataUsingPyPdf2("/root/a.pdf"))