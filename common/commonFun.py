import csv
import logging
import os
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from common.desiredCaps import appium_desired
from base.baseView import BaseView


# 封装公共类


class Common(BaseView):
    # 定义公共元素
    sv_search_view = (By.ID, 'com.taobao.taobao:id/sv_search_view')
    cancelBtn = (By.XPATH, '//*[@content-desc=\'我的淘宝\']')  # 取消按钮
    okBtn = (By.XPATH, '//*[@text=\'同意\']')  # 同意按钮
    wemedia_cacel = (By.ID, 'com.tal.kaoyan:id/view_wemedia_cacel')  # 跳过广告

    getmiaocoin = (By.XPATH, '//*[@text=\'做任务，领喵币\']')
    join_in = (By.XPATH, '//*[@text=\'去参与\']')
    browse = (By.XPATH, '//*[@text=\'去浏览\']')
    finish = (By.XPATH, '//*[@text=\'去完成\']')
    singin = (By.XPATH, '//*[@text=\'签到\']')
    watch = (By.XPATH, '//*[@text=\'去观看\']')
    stroll = (By.XPATH, '//*[@text=\'去逛逛\']')
    exit_message = (By.XPATH, '//*[@text=\'再按一次返回键退出手机淘宝\']')

    def get_miaocoin(self):
        a = True
        b = True
        c = True
        d = True
        e = True
        f = True

        self.active_page()
        while d:
            try:
                time.sleep(1)
                browseBtn = self.driver.find_element(*self.browse)
                logging.info('领取去浏览的喵币')
            except NoSuchElementException:
                logging.info('已无去浏览可领取的喵币')
                d = False
            else:
                browseBtn.click()
                time.sleep(23)
                self.driver.press_keycode(4)
                time.sleep(1)
        while a:
            try:
                time.sleep(1)
                join_inBtn = self.driver.find_element(*self.join_in)
                logging.info('领取去参与的喵币')
            except NoSuchElementException:
                logging.info('已无去参与可领取的喵币')
                a = False
            else:
                join_inBtn.click()
                time.sleep(23)
                self.driver.press_keycode(4)
                time.sleep(1)
        while b:
            try:
                time.sleep(1)
                singinBtn = self.driver.find_element(*self.singin)
                logging.info('签到')
            except NoSuchElementException:
                b = False
            else:
                singinBtn.click()
                logging.info('已签到')
                # time.sleep(1)
                self.driver.press_keycode(4)
        while c:
            try:
                time.sleep(1)
                finishBtn = self.driver.find_element(*self.finish)
                logging.info('领取去完成的喵币')
            except NoSuchElementException:
                logging.info('已无去完成可领取的喵币')
                c = False
            else:
                finishBtn.click()
                time.sleep(23)
                self.driver.press_keycode(4)
                time.sleep(1)
        while e:
            try:
                time.sleep(1)
                watchBtn = self.driver.find_element(*self.watch)
                logging.info('领取去观看的喵币')
            except NoSuchElementException:
                logging.info('已无去观看可领取的喵币')
                e = False
            else:
                watchBtn.click()
                time.sleep(23)
                self.driver.press_keycode(4)
                time.sleep(1)
        while f:
            try:
                time.sleep(1)
                strollBtn = self.driver.find_element(*self.stroll)
                logging.info('领取去逛逛的喵币')
            except NoSuchElementException:
                logging.info('已无去逛逛可领取的喵币')
                f = False
            else:
                strollBtn.click()
                time.sleep(23)
                self.driver.press_keycode(4)
                time.sleep(1)

        if a == False and b == False and c == False and d == False and e == False and f == False:
            logging.info('退出活动页面')
            i = True
            while i:
                try:
                    self.driver.find_element(*self.exit_message)
                except NoSuchElementException:
                    self.swipeDown()
                    self.driver.press_keycode(4)
                    time.sleep(1)
                else:
                    logging.info('已回到手机淘宝首页')
                    i = False
            return 1
        else:
            logging.info('退出活动页面')
            i = True
            while i:
                try:
                    self.driver.find_element(*self.exit_message)
                except NoSuchElementException:
                    self.swipeDown()
                    self.driver.press_keycode(4)
                    time.sleep(1)
                else:
                    logging.info('已回到手机淘宝首页')
                    i = False

            return 0
            time.sleep(1)

    def check_cancel_btn(self):
        logging.info('检查弹窗')
        try:
            cancelBtn = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('没有找到弹窗')
        else:
            logging.info('关闭弹窗')
            cancelBtn.click()

    def check_skipBtn(self):
        logging.info('检查温馨提示')
        try:
            skipBtn = self.driver.find_element(*self.okBtn)
        except NoSuchElementException:
            logging.info('没有找到温馨提示')
        else:
            logging.info('同意')
            skipBtn.click()

    # 获取屏幕尺寸

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 向左滑动屏幕

    def swipeLeft(self):
        logging.info('向左滑动')
        swipe = self.get_size()
        x1 = int(swipe[0] * 0.9)
        y1 = int(swipe[1] * 0.5)
        x2 = int(swipe[0] * 0.1)
        self.swipe(x1, y1, x2, y1, 500)

    # 向右滑动屏幕

    def swipeRight(self):
        logging.info('向右滑动')
        swipe = self.get_size()
        x1 = int(swipe[0] * 0.1)
        y1 = int(swipe[1] * 0.5)
        x2 = int(swipe[0] * 0.9)
        self.swipe(x1, y1, x2, y1, 500)

    # 向上滑动屏幕

    def swipeUp(self):
        logging.info('向上滑动')
        swipe = self.get_size()
        x1 = int(swipe[0] * 0.5)
        y1 = int(swipe[1] * 0.9)
        y2 = int(swipe[0] * 0.1)
        self.swipe(x1, y1, x1, y2, 500)

    # 向下滑动屏幕

    def swipeDown(self):
        logging.info('向下滑动')
        swipe = self.get_size()
        x1 = int(swipe[0] * 0.5)
        y1 = int(swipe[1] * 0.1)
        y2 = int(swipe[0] * 0.9)
        self.swipe(x1, y1, x1, y2, 500)

    def active_page(self):
        logging.info('进入618列车活动')
        time.sleep(2)
        self.driver.tap([(547, 1192), (1028, 1437)])
        self.driver.implicitly_wait(5)

        # size = self.get_size()
        # x = int(size[0] * (780 / 1080))
        # y = int(size[1] * (1300 / 1920))
        # # print(x, y)
        # self.driver.implicitly_wait(3)
        # self.driver.swipe(x, y, x, y)
        # self.driver.implicitly_wait(5)

        try:

            self.driver.find_element(*self.getmiaocoin).click()
            logging.info('做任务，领喵币')
            self.driver.implicitly_wait(3)
            logging.info('向上滑动')
            time.sleep(1)
            swipe = self.get_size()
            x1 = int(swipe[0] * 0.5)
            y1 = int(swipe[1] * 0.7)
            y2 = int(swipe[0] * 0.1)
            self.swipe(x1, y1, x1, y2, 500)
        except NoSuchElementException:
            logging.info('没有找到入口')

    # 获取当前时间
    def getTime(self):
        # windows文件名禁止使用“:”所以时间格式要避免类似“14:30:25”
        self.now_time = time.strftime('%Y{y}%m{m}%d{d}%H{h}%M{M}').format(y='年', m='月', d='日', h='时', M='分')
        return self.now_time

    # 获取截图
    def getScreenShot(self, module):
        now_time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s %s.png' % (module, now_time)
        logging.info('获取“%s”屏幕截图' % module)
        print('截图:' + '%s %s.png' % (module, now_time), end='')
        self.driver.get_screenshot_as_file(image_file)

    def check_market_ad(self):
        logging.info('检查广告弹窗')
        try:
            element = self.driver.find_element(*self.wemedia_cacel)
        except NoSuchElementException:
            pass
        else:
            logging.info('关闭广告弹窗')
            element.click()

    # 读取csv数据模块

    def get_csv_data(self, csv_file, line):
        logging.info('获取csv数据')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row


if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
    i = True
    # com.active_page()
    # com.miaocoin()
    while i:
        i = com.get_miaocoin()
        print(i)

    # com.check_skipBtn()
    # com.check_cancel_btn()
    #
    # print(com.getTime())
    # com.swipeLeft()
    # com.getScreenShot('测试截图')

    # csv_file = '../data/account.csv'
    # data = get_csv_data(csv_file, 2)
    # print(data)
