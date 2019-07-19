
class Swipe_On():
    def __init__(self,driver,direction):
        self.direction=direction
        self.driver=driver
    def swipe_on(self):
        if self.direction =='up':
            self.swipe_up()
        elif self.direction == 'down':
            self.swipe_down()
        elif self.direction == 'left':
            self.swipe_left()
        else:
            self.swipe_right()
    def get_window_size(self):
        size=self.driver.get_window_size()
        widgh = size['width']
        height = size['height']
        return widgh,height

    #向左滑动
    def swipe_left(self):
        x1=self.get_window_size()[0]/10*9
        y1=self.get_window_size()[1]/10
        x=self.get_window_size()[0]/10
        self.driver.swipe(x1,y1,x,y1)

    #向右滑动
    def swipe_right(self):
        x1=self.get_window_size()[0]/10
        y1=self.get_window_size()[1]/10
        x=self.get_window_size()[0]/10*9
        self.driver.swipe(x1,y1,x,y1)

    #向上滑动
    def swipe_up(self):
        x=self.get_window_size()[0]/10
        y=self.get_window_size()[1]/10
        y1=self.get_window_size()[0]/10*9
        self.driver.swipe(x,y1,x,y)
    #向上滑动
    def swipe_down(self):
        x=self.get_window_size()[0]/10
        y=self.get_window_size()[1]/10
        y1=self.get_window_size()[0]/10*9
        self.driver.swipe(x,y,x,y1)
