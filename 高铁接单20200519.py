# 指挥浏览器做爬虫，高铁，可以处理23条工单的,处理第2页第6条工单对不齐，采用刷新的方法关闭弹窗
from selenium import webdriver  #pip install selenium 
import os
import time



#引入chromedriver.exe
chromedriver = "C:\\Users\jiedan\\AppData\Local\\Google\\Chrome\\Application\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
#browser.maximize_window() #窗口最大化
url = "http://10.245.0.225/uf/login.jsp"  
browser.get(url)
time.sleep(2)


elementi= browser.find_element_by_css_selector('iframe')
browser.switch_to_frame(elementi)


browser.find_element_by_id("username").send_keys("lixn59")
browser.find_element_by_id("password").send_keys("czlt@2020")
browser.find_element_by_id("loginbtn").click()

time.sleep(2)
#browser.maximize_window() #窗口最大化

#time.sleep(10)
#time.sleep(2)
#browser.find_element_by_xpath('//*[@id="layui-layer1"]/span/a').click()#点击关闭按钮
#browser.refresh()    #刷新打开的页面

time.sleep(6)

#从应用收藏进入高铁派单
browser.find_element_by_id("AppFavorite").click()#应用收藏
time.sleep(2)
browser.find_element_by_id("appid_30353").click()#高铁派单

#browser.find_element_by_id("YYZX").click()#应用中心
#time.sleep(2)
#browser.find_element_by_id("TwoMenuYYZX").click()
#time.sleep(2)
#browser.find_element_by_id("sec_menu_1101").click()#电子运维
#time.sleep(2)
#browser.find_element_by_id("appid_30353").click()#高铁派单
#browser.find_element_by_id("appid_30313").click()#基站入网  测试滚动条
time.sleep(5)

browser.switch_to_frame('menu_show_for_regist_review_iframe')
browser.switch_to_frame('__menu_body')

time.sleep(2)

links_len_str  = browser.find_element_by_id("__total_count_valuetodoListContainer").text#工单数量
links_len = int(links_len_str)
print (time.strftime("%Y-%m-%d %H:%M:%S")) #输出时间
#print (links_len) #输出工单数量
print ('工单数',links_len,"条") #输出工单数量

for index in range(links_len):
    print('index=',index)
    if index == 23:#只处理23条工单，后面的工单不处理了
        break
        
    #if index >= 5 and index < 10:#处理 index 5,6,7,8,9
        #testindex = str(index)
        #        browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table['+testxpath+']/tbody/tr[1]/td[1]/a').click()
        #target = browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table['+testindex+']/tbody/tr[1]/td[1]/a')
        #browser.execute_script("arguments[0].scrollIntoView();", target)
        #time.sleep(2)
        
    if index >= 5 and index < 10:#处理 index 5,6,7,8,9
        testindex = str(index)
        #browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table['+testxpath+']/tbody/tr[1]/td[1]/a').click()
        #target = browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table['+testindex+']/tbody/tr[1]/td[2]/a') #测试滚动条
        #browser.execute_script("arguments[0].scrollIntoView();", target)
        #time.sleep(2)
        
        #定位到下一页
        target = browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table[5]/tbody/tr[1]/td[1]/a')
        browser.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(2)
        #向上移动
        target = browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table[4]/tbody/tr[1]/td[1]/a')
        browser.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(2)
        
        if index ==9:
            #向下移动
            target = browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table[5]/tbody/tr[1]/td[1]/a')
            browser.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(2)
        
    testxpath = str(index+1)
    browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table['+testxpath+']/tbody/tr[1]/td[1]/a').click()
    time.sleep(2)
    
    link_text =  browser.find_element_by_css_selector('#__link_bar > a:nth-child(1)').text
    #print(type(link_text),link_text)
    if link_text == '接单':
        browser.find_element_by_xpath('//*[@id="__link_bar"]/a[1]').click()#点击接单按钮
        time.sleep(2)
        browser.switch_to_frame('__myReceiveFormLink_dialog_body_iframe')
        browser.find_element_by_xpath('/html/body/div[2]/span[1]').click()#点击提交按钮
        time.sleep(2)

        time.sleep(10)
        browser.switch_to_frame('menu_show_for_regist_review_iframe')
        browser.switch_to_frame('__menu_body')
    else:
        browser.find_element_by_xpath('//*[@id="__link_bar"]/a[5]').click()#点击返回按钮
        #browser.find_element_by_xpath('//*[@id="__link_bar"]/a[3]').click()#点击返回按钮 测试滚动条
        time.sleep(2)
        
    if index>=9 and index<13:#处理 index 10，11,12,13
        testindex = str(index)
        #重新定位到 xpath = 10, index =9 
        target = browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table[10]/tbody/tr[1]/td[1]/a')
        browser.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(2)  

        #定位到下一页
        target = browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table[11]/tbody/tr[1]/td[1]/a')
        browser.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(2) 

        #向上移动
        target = browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table[10]/tbody/tr[1]/td[1]/a')
        browser.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(2) 

        #继续向上移动
        target = browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table[9]/tbody/tr[1]/td[1]/a')
        browser.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(2) 
    elif index >= 13 and index<15:#处理 index 14,15
        #重新定位到 xpath = 10, index =9
        target = browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table[10]/tbody/tr[1]/td[1]/a')
        browser.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(2)  
        #定位到下一页
        target = browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table[11]/tbody/tr[1]/td[1]/a')
        browser.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(2) 
    elif index>=15 and index<18:#处理 index 16,17,18
        #重新定位到 xpath = 10, index =9 
        target = browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table[10]/tbody/tr[1]/td[1]/a')
        browser.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(2)  
        #定位到下一页
        target = browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table[11]/tbody/tr[1]/td[1]/a')
        browser.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(2) 
        #定位到下一页
        target = browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table[14]/tbody/tr[1]/td[1]/a')
        browser.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(2) 
    elif index>=18:#处理 index 19,20,21,22,23
        #重新定位到 xpath = 10, index =9  第2页底部
        target = browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table[10]/tbody/tr[1]/td[1]/a')
        browser.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(2)  
        #定位到下一页  第3页第1条
        target = browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table[11]/tbody/tr[1]/td[1]/a')
        browser.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(2) 
        #第3页底部
        target = browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table[14]/tbody/tr[1]/td[1]/a')
        browser.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(2) 
        #定位该页的底部的条目
        target = browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table[18]/tbody/tr[1]/td[1]/a')
        browser.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(2) 
        #定位到下一页
        target = browser.find_element_by_xpath('//*[@id="todoListContainer"]/div[3]/table[19]/tbody/tr[1]/td[1]/a')
        browser.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(2) 
        #每一条工单处理完之后都会返回 index=0 第1条工单的位置
        
        
    
time.sleep(10)
browser.quit() #关闭并退出浏览器