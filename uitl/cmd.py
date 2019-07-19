import os

class DosCmd:
    def excute_cmd_result(self,cmd):
        result=os.popen(cmd).readlines()
        result_list=[]
        for i in result:
            if i=='\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list
    def excute_cmd(self,cmd):
        os.system(cmd)
if __name__ == '__main__':
    a=DosCmd()
    b=a.excute_cmd_result('adb devices')
    print(b)