import yaml

class WriteUserCommand:
    def read_data(self,filepath=None):
        '''加载yaml数据'''
        with open(r'G:\appium_python\config\userconfig.yaml', 'r') as f:
            data = yaml.load(f)
        return data
    def get_value(self,key,port):
        data=self.read_data()
        value=data[key][port]
        return value
    def write_data(self,data):
        '''写入数据'''
        with open(r'G:\appium_python\config\userconfig.yaml', 'a') as f:
            yaml.dump(data,f)
    def join_data(self,i,device,bp,port):
        '''拼接数据写入到yaml'''
        data={
            'user_info_'+str(i):{
                "deviceName":device,
                "bp":bp,
                "port":port
            }
        }
        return data
