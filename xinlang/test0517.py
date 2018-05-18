from selenium import webdriver
from time import sleep
import unittest
from xinlang.const import mvp,db
import psycopg2


class mvp_add(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_mvp_add(self):
        driver = self.driver
        driver.get("%s" % mvp.quick_login)
        driver.get("%s"%mvp.main_page)
        sleep(2)
        print('打开主页')
        #driver.implicitly_wait(10)
        driver.maximize_window()
        sleep(2)
        print('设置浏览器全屏打开')
        driver.find_element_by_xpath('%s'%mvp.add).click()
        sleep(2)
        print('新建推广计划')
        driver.find_element_by_xpath('%s'%mvp.choose).click()
        sleep(2)
        driver.find_element_by_xpath('%s'%mvp.choose_confirm).click()
        sleep(2)
        print('选择第一个帖子并确认选择')
        driver.find_element_by_xpath('%s'%mvp.click_price).clear()
        driver.find_element_by_xpath('%s'%mvp.day_cost).clear()
        driver.find_element_by_xpath('%s'%mvp.click_price).send_keys('10')
        driver.find_element_by_xpath('%s'%mvp.day_cost).send_keys('300')
        sleep(2)
        print('清空点击单价和日预算并重新设置')
        driver.find_element_by_xpath('%s'%mvp.create_confirm).click()
        sleep(10)
        print('创建计划')
        driver.find_element_by_xpath('%s'%mvp.more_choose).click()
        sleep(5)
        driver.find_element_by_xpath('%s'%mvp.status_choose).click()
        sleep(5)
        driver.find_element_by_xpath('%s'%mvp.effect_status).click()
        sleep(5)
        plan_id_value=driver.find_element_by_xpath('%s'%mvp.new_plan_id).text
        sleep(5)
        print('新创建的计划id是：%s'%plan_id_value)
        #conn = psycopg2.connect(database=db.db_cfg['database'],user=db.db_cfg['user'],password=db.db_cfg['password'],port=db.db_cfg['port'],host=db.db_cfg['host'])
        #sleep(2)
        #print('打开数据库')
        #cur=conn.cursor()
        #cur.execute("select a.name,c.mobile_price_ratio from tb_campaign c,tb_sem_account a where c.sem_account_id = a.id and c.user_id=%s and c.id=%s",(fm.id,plan_id_value))
        #sleep(10)
        #print('按新建的计划搜索百度计划名')
        #rows = cur.fetchall()
        #for row in rows:
           # print(rows)
          #  baidu_name=row[0]
          #  mobile_price_ratio=row[1]
          #  print('百度账号名：%s'%baidu_name)
         #   print('数据库出价比例:%s'%mobile_price_ratio)
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()