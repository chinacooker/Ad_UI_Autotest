from selenium import webdriver
from time import sleep
import unittest
from xinlang.const import fm,db
import psycopg2


class fm_add(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_fm_add(self):
        driver = self.driver
        driver.get("%s" % fm.quick_login)
        driver.get("%s"%fm.main_page)
        sleep(2)
        print('打开主页')
        #driver.implicitly_wait(10)
        driver.maximize_window()
        sleep(2)
        print('设置浏览器全屏打开')
        driver.find_element_by_xpath('%s'%fm.add).click()
        sleep(2)
        print('新建推广计划')
        driver.find_element_by_xpath('%s'%fm.choose).click()
        sleep(2)
        driver.find_element_by_xpath('%s'%fm.choose_confirm).click()
        sleep(2)
        print('选择第一个帖子并确认选择')
        driver.find_element_by_xpath('%s'%fm.time_set).click()
        sleep(2)
        driver.find_element_by_xpath('%s'%fm.set_one).click()
        driver.find_element_by_xpath('%s'%fm.set_two).click()
        driver.find_element_by_xpath('%s'%fm.set_comfirm).click()
        sleep(2)
        print('点击设置投放时间并取消0点和2点且完成确认')
        driver.find_element_by_xpath('%s'%fm.idea).clear()
        driver.find_element_by_xpath('%s'%fm.text).clear()
        driver.find_element_by_xpath('%s'%fm.idea).send_keys('家电维修，专业服务18年')
        driver.find_element_by_xpath('%s'%fm.text).send_keys('我就在这里，欢迎你的到来')
        sleep(2)
        print('清空原创意和内容并填写新创意和内容')
        driver.find_element_by_xpath('%s'%fm.self_define).click()
        sleep(2)
        driver.find_element_by_xpath('%s'%fm.keyword_set).send_keys('专业维修')
        driver.find_element_by_xpath('%s'%fm.select).click()
        sleep(10)
        print('点击自定义关键词并填词搜索')
        driver.find_element_by_xpath('%s'%fm.price_one).clear()
        driver.find_element_by_xpath('%s'%fm.price_five).clear()
        driver.find_element_by_xpath('%s'%fm.price_one).send_keys('10')
        driver.find_element_by_xpath('%s'%fm.price_five).send_keys('20')
        driver.find_element_by_xpath('%s'%fm.keyword_one).click()
        driver.find_element_by_xpath('%s'%fm.keyword_five).click()
        sleep(2)
        print('设定第一和第五个词价格并选定')
        driver.find_element_by_xpath('%s'%fm.page_three).click()
        sleep(2)
        driver.find_element_by_xpath('%s'%fm.keyword_page3_20th).click()
        sleep(2)
        print('切到第3页并勾选第20个词')
        driver.find_element_by_xpath('%s'%fm.price_ratio).clear()
        driver.find_element_by_xpath('%s'%fm.price_ratio).send_keys('1.2')
        sleep(2)
        print('清空出价比例并重新设置')
        driver.find_element_by_xpath('%s'%fm.day_cost).clear()
        driver.find_element_by_xpath('%s'%fm.day_cost).send_keys('300')
        sleep(2)
        print('清空日预算并重新设置')
        driver.find_element_by_xpath('%s'%fm.create_confirm).click()
        sleep(10)
        driver.find_element_by_xpath('%s'%fm.repet_create_close).click()
        sleep(2)
        print('创建计划并且跳过投放其他渠道')
        plan_id_value=driver.find_element_by_xpath('%s'%fm.new_plan_id).text
        sleep(2)
        print('新创建的计划id是：%s'%plan_id_value)
        conn = psycopg2.connect(database=db.db_cfg['database'],
                                user=db.db_cfg['user'],
                                password=db.db_cfg['password'],
                                port=db.db_cfg['port'],
                                host=db.db_cfg['host'])
        sleep(2)
        print('打开数据库')
        cur=conn.cursor()
        cur.execute("select a.name,c.mobile_price_ratio from tb_campaign c,tb_sem_account a where c.sem_account_id = a.id and c.user_id=%s and c.id=%s",(fm.id,plan_id_value))
        sleep(10)
        print('按新建的计划搜索百度计划名')
        rows = cur.fetchall()
        for row in rows:
            print(rows)
            baidu_name=row[0]
            mobile_price_ratio=row[1]
            print('百度账号名：%s'%baidu_name)
            print('数据库出价比例:%s'%mobile_price_ratio)
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()