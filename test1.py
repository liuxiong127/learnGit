# -*- encoding=utf8 -*- 
'''
@Time:  2021/4/16-11:03
@User:  Administrator
@File:  test1.py
@Email：  liuxiong@fcbox.com
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random

import time
import win32gui
import win32con


driver = webdriver.Chrome()
driver.get("https://cns-sit4.fcbox.com/")
driver.implicitly_wait(20)
driver.maximize_window()

# 登录
WebDriverWait(driver, 30, 0.5).until(EC.visibility_of_element_located(("id","login")))
driver.find_element(By.ID,'account').send_keys("003398")
driver.find_element(By.ID,'password').send_keys('!@#ASDttt')
driver.find_element_by_id('verifyCode').send_keys('1111')
driver.find_element_by_id('login').click()

time.sleep(3)
driver.refresh()
time.sleep(5)

WebDriverWait(driver, 30, 0.5).until(EC.visibility_of_element_located(('xpath','//span[text()="选址管理"]/parent::div')))


# 选址信息选择
driver.find_element_by_xpath('//span[text()="选址管理"]/parent::div').click()
eles = driver.find_elements_by_css_selector('img.actionIcon___1NtR0.icon___3R3tu')
eles[4].click()

driver.find_element_by_xpath('//label[contains(text(),"流程归属")]/parent::div/following-sibling::div').click()
driver.find_element_by_xpath('//*[contains(text(), "地区开发人员-广深以外")]').click()
driver.find_element_by_xpath('//a[text()="打开高德地图"]').click()

time.sleep(3)
driver.find_element_by_id('pickerInput').send_keys("玉兰苑")
time.sleep(3)
driver.find_element_by_css_selector('li.sugg-item.sugg-no-id').click()
time.sleep(3)
driver.find_element_by_css_selector('li.poibox').click()

# 随机移动当前地图选中的位置
# positions = driver.find_elements_by_xpath('//div[@class="amap-icon"]/img')
loc1 = ('xpath','//div[@class="amap-marker-label"]/preceding-sibling::div')
WebDriverWait(driver, 30, 0.5).until(EC.visibility_of_element_located(loc1))



# positions = driver.find_elements('xpath','//div[@class="amap-marker-label"]/preceding-sibling::div')
positions = driver.find_element_by_xpath('//div[@class="amap-marker-label"]/preceding-sibling::div')
print(positions)

positions.click()
time.sleep(3)
x = random.randint(-576,576)
y = random.randint(-225,225)
print(x,y)
ActionChains(driver).drag_and_drop_by_offset(positions, x , y).perform()



time.sleep(3)
driver.find_element_by_xpath('//button[text()="确定"]').click()
time.sleep(1)



driver.find_element_by_xpath('//label[contains(text(),"选址人员")]/parent::div/following-sibling::div').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[contains(text(), "丰巢员工")]').click()
time.sleep(0.5)
driver.find_element_by_xpath('//span[text()="查 询"]/parent::button').click()
time.sleep(1)
driver.find_element_by_xpath('//td/img').click()
time.sleep(1)
driver.find_element_by_css_selector('div.handleActionButtons___1J6_n img').click()







# 社区信息选择
WebDriverWait(driver,30,0.5).until(EC.visibility_of_any_elements_located(('xpath', '//div[text()="社区信息"]')))

driver.find_element_by_xpath('//span[text()="关联社区"]/parent::button').click()
time.sleep(1.5)


# driver.find_element_by_css_selector('input#housingEstateName').send_keys("黎明社区东区")
driver.find_element_by_xpath('//div[@id="rcDialogTitle1"]/parent::div/following-sibling::div//input[@id="housingEstateName"]').send_keys("黎明社区东区")
# driver.find_element_by_id('housingEstateName').send_keys("黎明社区东区")
print('---------------------------------------------------------')
time.sleep(5)
driver.find_element_by_xpath('//span[text()="筛 选"]/parent::button').click()
time.sleep(3)

driver.find_element_by_xpath('//tr/td//input').click()

driver.find_element_by_xpath('//span[text()="选 择"]/parent::button').click()
time.sleep(1.5)

driver.find_element_by_xpath('//label[contains(text(),"位置属性")]/parent::div/following-sibling::div').click()
driver.find_element_by_xpath('//li[contains(text(), "主出入口")]').click()
time.sleep(1)

driver.find_element_by_id('boxLocaltion').send_keys('丰巢柜UI测试')
driver.find_element_by_xpath('//label[contains(text(),"行业日均派件量")]/parent::div/following-sibling::div').click()
driver.find_element_by_xpath('//*[contains(text(), "18-30")]').click()

driver.find_element_by_css_selector('div.handleActionButtons___1J6_n img').click()
time.sleep(2)

WebDriverWait(driver, 30 ,0.5).until(EC.visibility_of_element_located(('xpath', '//div[contains(text(), "3.竞品信息")]')))

driver.find_element_by_xpath('//div[@id="hasCompetitor"]//span[text()="否"]').click()
time.sleep(2)
driver.find_element_by_css_selector('div.handleActionButtons___1J6_n img').click()







# 场地数据,长宽高
driver.find_element_by_id('areaHeight').send_keys(5)
driver.find_element_by_id('areaWidth').send_keys(5)
driver.find_element_by_id('areaLength').send_keys(5)
# 其他数据

# 柜机类型
driver.find_element_by_xpath('//label[contains(text(),"柜机类型")]/parent::div/following-sibling::div').click()
time.sleep(0.5)
driver.find_element_by_xpath('//li[contains(text(), "室外机")]').click()
# 摆放造型
driver.find_element_by_xpath('//label[contains(text(),"摆放造型")]/parent::div/following-sibling::div').click()
time.sleep(0.5)
driver.find_element_by_xpath('//li[contains(text(), "标准柜")]').click()

# 是否隔断
driver.find_element_by_xpath('//label[contains(text(),"是否隔断")]/parent::div/following-sibling::div').click()
time.sleep(0.5)
driver.find_element_by_xpath('//li[text()="否"]').click()
# 柜机正面是否严重遮挡
driver.find_element_by_xpath('//label[contains(text(),"柜机正面是否严重遮挡")]/parent::div/following-sibling::div').click()
time.sleep(0.5)
driver.find_elements_by_xpath('//li[text()="否"]')[1].click()
# 地面情况
driver.find_element_by_xpath('//label[contains(text(),"地面情况")]/parent::div/following-sibling::div').click()
time.sleep(0.5)
driver.find_element_by_xpath('//li[text()="水泥地"]').click()
# 地面是否涉及工建
driver.find_element_by_xpath('//label[contains(text(),"地面是否涉及工建")]/parent::div/following-sibling::div').click()
time.sleep(0.5)
driver.find_elements_by_xpath('//li[text()="否"]')[2].click()
# 投放规格
driver.find_element_by_xpath('//label[contains(text(),"投放规格")]/parent::div/following-sibling::div').click()
time.sleep(0.5)
driver.find_element_by_xpath('//li[text()="一拖四"]').click()
# 是否涉及拉电
driver.find_element_by_xpath('//label[contains(text(),"是否涉及拉电")]/parent::div/following-sibling::div').click()
time.sleep(0.5)
driver.find_elements_by_xpath('//li[text()="否"]')[3].click()
# 电费
driver.find_element_by_xpath('//label[contains(text(),"电费")]/parent::div/following-sibling::div').click()
time.sleep(0.5)
driver.find_element_by_xpath('//li[text()="租金含电费"]').click()

# 电支付周期
driver.find_element_by_xpath('//label[contains(text(),"支付周期")]/parent::div/following-sibling::div').click()
time.sleep(0.5)
driver.find_element_by_xpath('//li[text()="季付"]').click()
# 租期（年）
driver.find_element_by_xpath('//label[contains(text(),"租期（年）")]/parent::div/following-sibling::div').click()
time.sleep(0.5)
driver.find_element_by_xpath('//li[text()="3"]').click()


# driver.find_element_by_id('powerLineLength').send_keys(12)
# 租金
a = driver.find_element_by_id('rentMoney')
a.clear()
a.send_keys(2500)

# 网络条件
driver.find_element_by_xpath('//label[contains(text(),"网络条件")]/parent::div/following-sibling::div').click()
time.sleep(0.5)
driver.find_element_by_xpath('//li[text()="宽带"]').click()

# 是否遮挡
driver.find_element_by_xpath('//label[contains(text(),"是否遮挡")]/parent::div/following-sibling::div').click()
time.sleep(0.5)
driver.find_elements_by_xpath('//li[text()="否"]')[4].click()

# 是否上刊
driver.find_element_by_xpath('//label[contains(text(),"是否上刊")]/parent::div/following-sibling::div').click()
time.sleep(0.5)
driver.find_elements_by_xpath('//li[text()="否"]')[5].click()





js = '''
document.querySelector("#boxType > div > div").innerText="室外柜";
document.querySelector("#boxModelType > div > div > div").innerText="标准柜";
document.querySelector("#whetherToSevered > div > div > div").innerText="否";
document.querySelector("#isBoxFaceKeep > div > div > div").innerText="否";
var a = document.querySelector("#floorCondition > div > div > div");
a.innerText="水泥地";
a.title = "水泥地";

document.querySelector("#floorIsConstruct > div > div > div").innerText="否";
document.querySelector("#putType > div > div > div").innerText="一拖四";
document.querySelector("#isPower > div > div > div").innerText="是";
document.querySelector("#powerCondition > div > div > div").innerText="自行拉电";
document.querySelector("#powerType > div > div > div").innerText="租金含电费";
document.querySelector("#rentPayPeriod > div > div > div").innerText="季付";
document.querySelector("#rentYear > div > div > div").innerText="3";
document.querySelector("#networkCondition > div > div > div").innerText="手机运营商";
document.querySelector("#mobileOperators > div > div > div").innerText="移动";
document.querySelector("#signalTest > div > div > div").innerText="优(大于-90dBm)";

document.querySelector("#whetherBlock > div > div > div").innerText="否";
document.querySelector("#whetherPublish > div > div > div").innerText="否";

'''

# time.sleep(10)
# driver.execute_script(js)

time.sleep(2)

driver.find_element_by_css_selector('div.handleActionButtons___1J6_n img').click()
time.sleep(2)


def upload(filepath,browser_type="chrome"):
    if browser_type == "chrome":
        title = "打开"
    else:
        title = ""

    # 找元素
    # 一级窗口 "#32770" , "打开"
    dialog = win32gui.FindWindow("#32770",title)

    ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)  #二级
    comboBox = win32gui.FindWindowEx(ComboBoxEx32,0,"ComboBox",None)       #三级

    # 编辑按钮
    edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)
    # 点击打开
    button = win32gui.FindWindowEx(dialog,0,'Button',"打开(&O)")

    # 输入文件路径
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)  # 发送文件路径
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  #点击打开

# 上传选址相关照片
eles = driver.find_elements_by_xpath('//div[@class="antUploadText___2ytRx"]')
for i in eles:
    i.click()
    time.sleep(5)
    upload(r'E:\testdata\picture\test11.jpg')

driver.find_element_by_id('remarkInfo').send_keys("选址UI自动化测试")

time.sleep(5)
driver.find_element_by_xpath('//span[text()="提 交"]/parent::button').click()


WebDriverWait(driver, 30, 0.5).until(EC.visibility_of_element_located(('xpath', '//span[text()="选址申请提交成功"]')))

print("选址申请成功")

driver.close()