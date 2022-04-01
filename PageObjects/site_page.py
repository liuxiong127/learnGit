# -*- encoding=utf8 -*- 
'''
@Time:  2021/4/15-18:35
@User:  Administrator
@File:  site_page.py
@Email：  liuxiong@fcbox.com
'''

from Common.basepage import BasePage
from PageLocator.site_apply_loc import SiteApplyLocator as sal
import time
import random

class SitePage(BasePage):

    def add_site_apply(self):
        self.click_element(sal.site_apply_button, '点击选址申请按钮')
        self.click_element(sal.flowBelong, '点击流程归属下拉框')
        self.click_element(sal.select_flow, '选择流程')

        self.click_element(sal.gaode_map, '点击打开高德地图')
        time.sleep(3)
        self.input_text(sal.search_input, '输入地址搜索', '玉兰苑')
        time.sleep(2)
        self.click_element(sal.select_address, '选择一个地址')
        time.sleep(2)
        self.click_element(sal.select_poi, '选择一个点')

        # 随机移动当前选中的点位
        loc1 = ('xpath', '//div[@class="amap-marker-label"]/preceding-sibling::div')

        x = random.randint(-576, 576)
        y = random.randint(-225, 225)
        self.drag_and_drop_element(loc1,x,y, '拖动元素')

        self.click_element(sal.address_assure, '确认点位')

