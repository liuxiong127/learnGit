# -*- encoding=utf8 -*- 
'''
@Time:  2019/10/23-17:58
@User:  Administrator
@File:  basepage.py
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

    def __init__(self,driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self,locator,img_desc, timeout=30,frequency=0.5):
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
            #等待元素可见
            WebDriverWait(self.driver,timeout,frequency).until(EC.visibility_of_element_located(locator))
        except:
            # 日志输出
            logging.exception("等待元素 {} 可见失败！！！".format(locator)) #exception相比error可以在控制台中展示一模一样的报错日志
            #截图
            self.save_screenshots(img_desc)
            raise
        else:
            # 结束等待时间
            end = datetime.datetime.now()
            logging.info("等待元素 {} 可见成功，等待时间 {}".format(locator, end-start))

    # 等待元素不可见
    def wait_eleInvisible(self,locator,img_desc, timeout=30, frequency=0.5):
        """
        :param locator: 元素定位，元组形式。example:（xpath，//div[@id="dddd"]）
        :param timeout: 超时时间
        :param frequency: 轮询周期
        :param filename: 截图保存名称
        :return: None
        """
        start = datetime.datetime.now()
        try:
            #等待元素不可见
            WebDriverWait(self.driver,timeout, frequency).until(EC.invisibility_of_element_located(locator))
        except:
            # 日志输出
            logging.exception("等待元素 {} 不可见失败！！！".format(locator))
            # 截图
            self.save_screenshots(img_desc)
            raise
        else:
            # 结束等待时间
            end = datetime.datetime.now()
            logging.info("等待元素 {} 可见成功，等待时间 {}".format(locator, end-start))

    # 等待元素存在
    def wait_elePresence(self,locator,img_desc, timeout=30, frequency=0.5):
        """
        :param locator: 元素定位，元组形式。（元素定位方法，元素定位表达式）
        :param timeout: 超时时间
        :param frequency: 轮询周期
        :param filename: 截图保存名称
        :return: None
        """
        # 开始等待时间
        start = datetime.datetime.now()
        try:
            #等待元素存在
            WebDriverWait(self.driver,timeout,frequency).until(EC.presence_of_element_located(locator))
        except:
            logging.exception("等待元素 {} 存在失败！！！".format(locator))
            #截图
            self.save_screenshots(img_desc)
            raise
        else:
            # 结束等待元素存在的时间
            end = datetime.datetime.now()
            logging.info("等待元素结束，等待时长为：{}".format(end - start))

    # 查找单个元素
    def get_element(self,locator,img_desc):
        """
        查找元素
        :param locator:
        :param img_desc:
        :return:返回查找到的元素
        """
        try:
            ele =  self.driver.find_element(*locator)
        except:
            # 日志
            logging.exception("查找 {} 元素 {} 失败！！！".format(img_desc, locator))
            # 截图
            self.save_screenshots(img_desc)
            raise
        else:
            logging.info("查找 {} 元素 {} 成功！！！".format(img_desc, locator))
            return ele

    # 查找多个元素
    def get_elements(self,locator,img_desc):
        try:
            ele = self.driver.find_elements(*locator)
        except:
            logging.exception("查找 {} 元素 {} 失败！！！".format(img_desc, locator))
            # 截图
            self.save_screenshots(img_desc)
            raise
        else:
            logging.info("查找 {} 元素 {} 成功！！！".format(img_desc, locator))
            return ele

    # 点击操作
    def click_element(self,locator,img_desc,timeout=30,frequency=0.5):
        # 等待元素可见
        self.wait_eleVisible(locator,img_desc,timeout, frequency)
        # 查找元素
        ele = self.get_element(locator,img_desc)
        # 操作元素
        try:
            ele.click()
            logging.info("点击  {} 元素 {} 成功！".format(img_desc, locator))
        except:
            logging.exception("元素点击操作失败！！！")
            # 截图
            self.save_screenshots(img_desc)
            raise

    # 输入文本操作
    def input_text(self,locator,img_desc,text):
        # 等待元素可见
        self.wait_eleVisible(locator,img_desc)
        # 查找元素
        ele = self.get_element(locator,img_desc)
        # 操作元素

        try:
            ele.send_keys(text)
            logging.info("{} 元素 {} 输入文本{} 成功".format(img_desc, locator, text))
        except:
            logging.exception(" {} 元素 {} 输入文本失败！！！")
            # 截图
            self.save_screenshots(img_desc)
            raise

    # 获取元素的文本内容
    def get_text(self,locator, img_desc,timeout=30,frequency=0.5):
        # 等待元素可见
        self.wait_elePresence(locator, img_desc,timeout, frequency)
        # 查找元素
        ele = self.get_element(locator, img_desc)
        # 获取文本内容
        logging.info("获取元素 {} 文本内容".format(locator))
        try:
            logging.info("获取{}元素 {} 文本内容 {} 成功".format(img_desc, locator, ele.text))
            return ele.text
        except:
            logging.exception("获取{} 元素{} 的文本内容失败！！！".format(img_desc, locator))
            # 截图
            self.save_screenshots(img_desc)
            raise

    # 获取元素的属性值
    def get_element_attribute(self,locator,img_desc,attr):
        # 等待元素存在
        self.wait_elePresence(locator, img_desc)
        # 查找元素
        ele = self.get_element(locator, img_desc)
        # 获取元素的属性值
        try:
            logging.info("获取{} 元素 {} 的{}的属性值成功".format(img_desc,locator, attr))
            return ele.get_attribute(attr)
        except:
            logging.exception("获取元素的属性值失败！！！")
            # 截图
            self.save_screenshots(img_desc)
            raise

    # alert弹窗处理
    def alert_action(self,img_desc,text="", timeout=30,frequency=0.5,action="accept"):
        """
        alert弹窗的处理
        :param img_desc: 操作描述
        :param text:    弹窗的文本框输入值
        :param timeout:
        :param frequency:
        :param action:  对弹窗的操作 accept》确认 dismiss》取消  fill_with》输入文本值
        :return: None
        """
        # 等待弹窗出现
        WebDriverWait(self.driver,timeout,frequency).until(EC.alert_is_present())
        # alert切换
        try:
            logging.info("{}页面，alert弹窗切换成功".format(img_desc))
            alert = self.driver.switch_to.alert
            time.sleep(0.5)
        except:
            logging.exception("alert弹窗切换失败！！！")
            # 截图
            self.save_screenshots(img_desc)
            raise
        else:
            #alert窗口切换成功后进行后续操作
            #点击"确定"按钮
            if action == "accept":
                alert.accept()
            # 点击"取消"按钮
            elif action == "dismiss":
                alert.dismiss()
            # 输入文本内容
            elif action == "fill_with":
                alert.send_keys(text)

    # iframe切换
    def switch_iframe(self,iframe_reference,img_desc,timeout=30,frequency=0.5):
        #使用WebDriverWait进行iframe切换
        try:
            logging.info("{} iframe切换".format(iframe_reference))
            WebDriverWait(self.driver,timeout,frequency).until(EC.frame_to_be_available_and_switch_to_it(iframe_reference))
            time.sleep(0.5)
        except:
            logging.exception("iframe切换失败！！！")
            # 截图
            self.save_screenshots(img_desc)
            raise

    # windows窗口切换
    def switch_window(self,handles,index,img_desc,timeout=30,frequency=0.5):
        # 使用WebDriverWait进行window切换

        try:
            # 等待新窗口出现
            WebDriverWait(self.driver,timeout,frequency).until(EC.new_window_is_opened(handles))
            # 新窗口打开后，重新获取句柄
            handles = self.driver.window_handles
            # 切换窗口
            self.driver.switch_to.window(handles[index])
            logging.info("window窗口切换成功")
            time.sleep(0.5)
        except:
            logging.exception("windows窗口切换失败！！！")
            # 截图
            self.save_screenshots(img_desc)
            raise

    # 获取窗口title
    def get_current_window_title(self):
        try:
            title = self.driver.title()
            logging.info("获取当前窗口的标题{}成功！".format(title))
            return title
        except:
            logging.exception("获取当前窗口的标题失败")
            raise

    # 获取当前窗口的URL
    def get_current_window_url(self):
        try :
            url = self.driver.current_url()
            logging.info("获取当前窗口的URL {} 成功！".format(url))
            return url
        except:
            logging.exception("获取当前窗口的URL失败！！")
            raise




    # 上传操作
    # def upload_file(self,filepath,doc=""):
    #     logging.info("{} 文件上传操作".format(doc))
    #     try:
    #         # 一级窗口
    #         dialog = win32gui.FindWindow("#32770", "打开")
    #         # 二级窗口
    #         ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
    #         # 三级窗口
    #         ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
    #         # 文本输入框--四级窗口
    #         edit = win32gui.FindWindowEx(ComboBox, 0, "Edit", None)
    #         # 打开按钮--二级窗口
    #         button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&O)")
    #
    #         # 输入文件地址
    #         win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)
    #         # 点击“打开”按钮--提交文件
    #         win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
    #     except:
    #         logging.exception("文件上传失败！！！")
    #         # 截图
    #         self.save_screenshots(doc)
    #         raise

    # 键盘输入
    def input_from_keyboard(self,locator,args,img_desc):
        # 等待元素可见
        self.wait_eleVisible(locator, img_desc)
        #查找元素
        ele = self.get_element(locator,img_desc)
        #输入操作

        try:
            ele.send_keys(*(args))
            logging.info("{}元素输入操作成功".format(locator))
        except:
            logging.exception("元素输入操作失败！！！")
            # 截图
            self.save_screenshots(img_desc)
            raise

    # 鼠标悬浮
    def move_mouse_to_element(self,locator,img_desc):
        # 等待元素可见
        self.wait_eleVisible(locator, img_desc)
        # 查找元素
        ele = self.get_element(locator, img_desc)

        try:
            logging.info("移动鼠标到{} 元素操作".format(img_desc))
            ActionChains(self.driver).move_to_element(ele).perform()
        except:
            logging.exception("鼠标移动到'{}'元素{}操作失败！！！".format(img_desc, locator))
            # 截图
            self.save_screenshots(img_desc)
            raise


    # 下拉列表
    # js处理----滚动条
    # js处理----日历控件
    # select操作

    # 失败截图
    def save_screenshots(self,img_desc):
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


    def drag_and_drop_element(self, locator, x , y ,img_desc):
        '''
        以当前位置为中心，移动鼠标
        :param x:
        :param y:
        :param img_desc:
        :return:
        '''

        self.positions = self.get_element(locator, img_desc)
        ActionChains(self).drag_and_drop_by_offset(self.positions, x, y).perform()




