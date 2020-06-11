# 封装基础类，如：获取元素、获取屏幕尺寸等
class BaseView(object):
    def __init__(self, driver):
        self.driver = driver

    # 获取元素
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    # 获取元素集
    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    # 获取屏幕尺寸
    def get_windows_size(self):
        return self.get_windows_size()

    # 滑动动作
    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

