from uitl.read_ini import ReadInt
import os
import time
class GetByLocal():
    '''封装定位方式'''
    def __init__(self,driver):
        self.driver=driver
    def get_element_value(self,key):
        readini=ReadInt()
        local=readini.get_value(key)
        type=local.split('>')[0]
        local_by=local.split('>')[1]
        try:
            if type == "xpath":
                return self.driver.find_element_by_xpath(local_by)
            elif type == "class_name":
                return self.driver.find_element_by_class_name(local_by)
            elif type == "id":
                return self.driver.find_element_by_id(local_by)
            elif type == "name":
                return self.driver.find_element_by_name(local_by)
            elif type == "link_text":
                return self.driver.find_element_by_link_text(local_by)
            elif type == "partial_link_text":
                return self.driver.find_element_by_partial_link_text(local_by)
        except:
            return None
    def Click(self, key):
        element=self.get_element_value(key)
        try:
            element.click()
        except:
            return None
    # 输入内容方法
    def Input(self,key,inputvalue):
        element=self.get_element_value(key)
        try:
            element.send_keys(inputvalue)
        except:
            return None
    #清空输入内容
    def Clear(self,key):
        element=self.get_element_value(key)
        try:
            element.clear()
        except:
            return None
    #截图封装
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
        except NameError as e:
            self.get_windows_img()

