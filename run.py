from common.desiredCaps import appium_desired
from common.commonFun import Common

driver = appium_desired()
com = Common(driver)
i = True
n = com.get_miaocoin()
while i:
    # 加入计数器当没有可领取的喵币时再运行一次，防止有遗漏的喵币没有领取
    if n == 0:
        n = com.get_miaocoin()
    elif n == 1:
        n = com.get_miaocoin()
        n += n
    else:
        i = False


