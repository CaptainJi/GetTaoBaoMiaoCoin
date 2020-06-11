from server.checkPort import *
from time import sleep, ctime
import multiprocessing
import subprocess
import logging


# 查找device
def find_device():
    cmd_device = 'adb devices |findstr /e device'
    logging.info('查找设备')
    result = os.popen(cmd_device).read()
    # print(result)
    logging.info(cmd_device)
    if 'device' in result:
        i = result.index('device')
        # print(i)
        start = 0
        end = result.index('\t')
        device = result[start:end]
        logging.info('已找到设备：{d}'.format(d=device))
        # print('设备ID：{d}'.format(d=device))
        return device
    else:
        logging.info('查找设备失败，请将手机连接PC或检查环境配置')
        # print('查找设备失败，请将手机连接PC或检查环境配置')



# 检查端口
def check_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))
        s.shutdown(2)
    except OSError as msg:
        # logging.info('端口：%s 可用' % port)
        # logging.info(msg)
        return True
    else:
        # logging.info('端口：%s 已被占用' % port)
        return False


# 释放端口
def release_port(host, port):
    if check_port(host, port):
        logging.info('%s端口可用 Appium服务已关闭' % port)
    else:
        cmd_find = 'netstat -ano |findstr %s' % port
        logging.info(cmd_find)

        result = os.popen(cmd_find).read()
        logging.info(result)
        if str(port) and 'LISTENING' in result:
            i = result.index('LISTENING')
            start = i + len('LISTENING') + 7
            end = result.index('\n')
            pid = result[start:end]
            cmd_kill = 'taskkill -f -pid %s' % pid
            logging.info('执行 %s 命令关闭Appium服务' % cmd_kill)
            os.popen(cmd_kill)
            logging.info('Appium服务已关闭')
        else:
            logging.info('Appium服务未开启')


# Appium服务启动
def start_appium_action(host, port):
    if check_port(host, port):
        bootstrap_port = str(port + 1)
        logging.info('开始启动Appium服务: Host: %s  Port: %s  BootStrap Port: %s' % (host, port, bootstrap_port))
        cmd = 'start /b appium -a' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)
        logging.info('执行 %s 命令开启Appium服务' % cmd)
        subprocess.Popen(cmd, shell=True, stdout=open('./logs/' + str(port) + '.log', 'a'), stderr=subprocess.STDOUT)
        return True
    else:
        bootstrap_port = str(port + 1)
        logging.info('Appium服务已启动  Host: %s  Port: %s  BootStrap Port: %s' % (host, port, bootstrap_port))
        return False


# # 设备启动
# def start_devices_action(udid, port):
#     if start_appium_action(host, port):
#         appium_desired()
#     else:
#         release_port(port)


def appium_start_sync(devicesList, port):
    logging.info('====================Appium多进程启动====================')
    appium_process_list = []
    # 加载appium进程组
    for i in range(devicesList):
        host = '127.0.0.1'
        port = port + 2 * i
        appium = multiprocessing.Process(target=start_appium_action, args=(host, port))
        appium_process_list.append(appium)

    for appium in appium_process_list:
        appium.start()
    for appium in appium_process_list:
        appium.join()
    sleep(5)


# def devices_start_sync(devicesList, port):
#     logging.info('====================设备多进程启动====================')
#     desired_process = []
#     # 多进程启动测试
#     for i in range(devicesList):
#         port = port + 2 * i
#         desired = multiprocessing.Process(target=start_devices_action, args=(i, port))
#         desired_process.append(desired)
#
#     for desired in desired_process:
#         desired.start()
#     for desired in desired_process:
#         desired.join()


if __name__ == '__main__':
    # check_port(host, port)
    # release_port(port)
    find_device()

