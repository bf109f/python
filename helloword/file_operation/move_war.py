import os
import shutil
import time


def find_web_apps(file_path):
    """
    查找tomcat目录中的webapps目录
    :param file_path 给出的webapps所在目录或父目录
    :return: webapps的全路径
    """
    for root, dirs, files in os.walk(file_path):
        # 判断是否是tomcat目录下的webapps目录
        if root.find("apache-tomcat") != -1 and root.endswith("webapps"):
            return root
        # for dir_names in dirs:
        #     dir_str = os.path.join(root, dir_names)
        #     print(dir_str)
        #     # 判断是否是tomcat目录下的webapps目录
        #     if dir_str.find("apache-tomcat") != -1 and dir_str.endswith("webapps"):
        #         return dir_str
    else:
        print("未找到webapps目录，请给出正确的目录")
        return None


def copy_war(old_file, web_path):
    """
    将war包拷贝到tomcat下
    :param old_file: target目录下的war包路径
    :param web_path:webapps的路径
    :return:war_name war包名称
    """
    war_name = ""
    if old_file.endswith(".war") and os.path.exists(old_file):
        # basename获取文件名  dirname 获取文件夹名
        war_name = os.path.basename(old_file)
        new_file = web_path + "\\" + war_name
        if os.path.exists(new_file + "_bak"):
            os.remove(new_file + "_bak")
        if os.path.exists(new_file):
            os.rename(new_file, new_file + "_bak")
        shutil.copyfile(old_file, new_file)
    return war_name


def del_file(web_app_path, pro_name):
    """
    删除原项目
    :param web_app_path webapps的路径
    :param pro_name 项目名称
    :return:
    """
    pro_name = pro_name.replace(".war", "")
    dir_path = web_app_path + "\\" + pro_name
    if os.path.exists(dir_path):
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                print(file_path)
                os.remove(file_path)
        # 删除所有空目录
        shutil.rmtree(dir_path)


start_time = time.time()
# tomcat路径
path = find_web_apps("E:\\test\\apache-tomcat-9.0.0.M22\\webapps")
# war包路径
war_path = "F:\\girl\\bills\\jsnu\\target\\fendou-jsnu.war"
gl_war_name = copy_war(war_path, path)
del_file(path, gl_war_name)
end_time = time.time()
print("耗时 %f" % (end_time - start_time) + "秒")