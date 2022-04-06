# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/2-17:46
@User:  Administrator
@File:  basepage.py.py
@Email：  liuxiong@fcbox.com
'''

import logging
import datetime
import time
from Common import project_path
from Common import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def wait_element_visible(self, locator, timeout, frequency,img_desc):
        """
                :param locator: 元素定位，元组形式。example:（xpath，//div[@id="dddd"]）
                :param timeout: 超时时间
                :param frequency: 轮询周期
                :param filename: 截图保存名称
                :return: None
                """
        # 开始等待时间
        start = datetime.datetime.now()
        try:
            # 等待元素可见
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(locator))
        except:
            # 日志输出
            logging.exception("等待元素 {} 可见失败！！！".format(locator))  # exception相比error可以在控制台中展示一模一样的报错日志
            # 截图
            self.save_screenshots(img_desc)
            raise
        else:
            # 结束等待时间
            end = datetime.datetime.now()
            logging.info("等待元素 {} 可见成功，等待时间 {}".format(locator, end - start))

        # 失败截图
    def save_screenshots(self, img_desc):
        """
        操作失败后，进行截图操作
        :param img_desc:图片名称的描述，可以为这样的形式：模块名_页面名称_操作名称_年-月-日_时分秒.png
        :return:
        """

        # 获取截图时间并转换成字符串格式---如：2018_12_28_14_01_39
        time_str = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

        # 设置图片保存路径
        file_name = project_path.screenshots_path + '\\' + img_desc + time_str + '.png'
        # 保存截图
        self.driver.save_screenshot(file_name)
        logging.info("获取网页截图成功，文件保存路径为：{}".format(file_name))