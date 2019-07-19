from uitl.cmd import DosCmd
class Port():
    def port_is_use(self,port_num):
        self.dos=DosCmd()
        flag=None
        command='netstat -ano|findstr'+' '+str(port_num)
        result=self.dos.excute_cmd_result(command)
        if len(result)>0:
            flag=True
        else:
            flag=False
        return flag
    def create_port_list(self,start_port,devices_list):
        '''生成可用端口'''
        port_list=[]
        if devices_list != '请检查手机是否连接成功，目前没有检测到哦T_T!':
            while len(port_list)!=len(devices_list):
                if self.port_is_use(start_port)!=True:
                    port_list.append(start_port)
                start_port+=1
            return port_list
        else:
            return "手机没有连接成功哦T_T"




