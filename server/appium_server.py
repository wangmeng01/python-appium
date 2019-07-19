from appium import webdriver
class Start_Server():
    def start_server(self):
        capabilities={
            'platformName':'Android',
            'deviceName':'127.0.0.1:6555',
            'app':'C:\\Users\\microlanguage\\Desktop\\lxt_test_v2.14.apk'
        }
        driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',capabilities)
        return driver
