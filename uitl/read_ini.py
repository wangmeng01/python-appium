import configparser
class ReadInt:
    '''封装读取ini的方法'''
    def __init__(self,filepath=None):
        if filepath == None:
            self.filepath=r'G:\appium_python\config\localElement.ini'
        else:
            self.filepath=filepath
        self.read=self.read_ini()
    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.filepath)
        return read_ini
    def get_value(self,element_key,group_key=None,):
        try:
            if group_key ==None:
                value=self.read.get('login_element', element_key)
            else:
                value=self.read.get(group_key, element_key)
            return value
        except:
            return None
