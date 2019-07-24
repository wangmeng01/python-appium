from uitl.cmd import DosCmd
from uitl.port import Port
from uitl.write_user_command import WriteUserCommand
import threading
class Server():
    def __init__(self):
        self.dos = DosCmd()
        self.devices_list=self.get_devices()
    def get_devices(self):
        '''获取设备信息'''

        devices_list=[]
        result_list=self.dos.excute_cmd_result('adb devices')
        if len(result_list)>=2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info=i.split('\t')
                devices_list.append(devices_info[0])
            return devices_list
        else:
            return ("请检查手机是否连接成功，目前没有检测到哦T_T!")
    def create_port_list(self,start_port):
        '''创建可用端口'''
        port=Port()
        port_list=port.create_port_list(start_port,self.get_devices())
        return port_list
    def create_command_list(self,i):
        #appium -p 4700 -bp 4701 -U 127.0.0.1
        write_user_command = WriteUserCommand()
        command_list=[]
        appium_port_list=self.create_port_list(4700)
        bootstrap_port_list=self.create_port_list(4800)
        devices_list=self.get_devices()
        if len(devices_list) > 0 and appium_port_list != '手机没有连接成功哦T_T' and bootstrap_port_list != '手机没有连接成功哦T_T':
            command = 'appium -p ' + str(appium_port_list[i]) + ' -bp ' + str(bootstrap_port_list[i]) + ' -U ' + devices_list[i] + " --no-reset --session-override"
            command_list.append(command)
            data = write_user_command.join_data(i, str(bootstrap_port_list[i]), devices_list[i],str(appium_port_list[i]))
            write_user_command.write_data(data)
            return command_list
        else:
            return "手机没有连接成功哦T_T"
    def start_server(self,i):
        self.kill_server()
        start_list=self.create_command_list(i)
        self.dos.excute_cmd(start_list[0])
    def kill_server(self):
        server_list=self.dos.excute_cmd_result('tasklist | find "node.exe"')
        if len(server_list)>0:
            self.dos.excute_cmd('taskkill -F -PID node.exe')
    def main(self):
        for i in range(len(self.devices_list)):
            appium_start=threading.Thread(target=self.start_server,args=(i,))
            appium_start.start()
        else:
            return "手机没有连接成功哦T_T,服务启动失败!!!!!"
if __name__ == '__main__':
    a=Server()
    b=a.main()