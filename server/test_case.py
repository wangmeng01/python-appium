from server.appium_server import Start_Server
from uitl.get_by_local import GetByLocal
class Test():
    def __init__(self):
        self.driver=Start_Server().start_server()
        self.get_by_local=GetByLocal(self.driver)

    def start(self):
        self.get_by_local.Input('username','13261869728')
        self.get_by_local.Input('password','123qwe')
        self.get_by_local.Click('login')



if __name__ == '__main__':
    a=Test()
    a.start()