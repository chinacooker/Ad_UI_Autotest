"""新建凤鸣计划时需要用到的常量，网页结构修改时需要修改对应的常量"""

id='252'
quick_login='http://192.168.8.201/bax/user/login/local?user_id=%s'% id             #骇客登录，账号13127811381
main_page='http://192.168.8.201/main'                                                  #bax主页
add='/html/body/content/div[1]/main/ul/li[4]/ul/li[1]/p'                           #新建推广计划页面
choose='/html/body/content/div[2]/main/section[1]/div[2]/span/' \
       'div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[1]/div/div/label'          #选择第一个帖子
choose_confirm='/html/body/content/div[2]/main/section[1]/div[2]/' \
               'span/div[2]/div/footer/span[2]/button[2]'                            #选择后确认
time_set='/html/body/content/div[2]/main/section[1]/div[4]/span/' \
         'button/span'                                                                    #时段设置
set_one='/html/body/content/div[2]/div[2]/div/div[2]/main/content/' \
        'section[1]/aside[2]/div[1]/div/label/span/span'                            #取消0点
set_two='/html/body/content/div[2]/div[2]/div/div[2]/main/content/' \
        'section[1]/aside[2]/div[3]/div/label/span/span'                            #取消2点
set_comfirm='/html/body/content/div[2]/div[2]/div/div[3]/footer/button[2]'        #设置完成确认
idea='/html/body/content/div[2]/main/section[2]/div[1]/span/div/div/input'       #创意
text='/html/body/content/div[2]/main/section[2]/div[2]/span/div/div/textarea'   #内容
self_define='/html/body/content/div[2]/main/section[3]/h3/a'                        #自定义关键词
keyword_set='/html/body/content/div[2]/main/section[3]/div[2]/span/div/input'    #填写自定义词
select='/html/body/content/div[2]/main/section[3]/div[2]/button'                  #搜索关键词
price_one='/html/body/content/div[2]/main/section[3]/div[3]/div/div[3]/' \
          'table/tbody/tr[1]/td[4]/div/span/div/input'                               #第一个词出价
price_five='/html/body/content/div[2]/main/section[3]/div[3]/div/div[3]/' \
          'table/tbody/tr[5]/td[4]/div/span/div/input'                               #第五个词出价
keyword_one='/html/body/content/div[2]/main/section[3]/div[3]/div/div[3]/' \
            'table/tbody/tr[1]/td[1]/div/label/span'                                  #第一个词选择
keyword_five='/html/body/content/div[2]/main/section[3]/div[3]/div/div[3]/' \
            'table/tbody/tr[5]/td[1]/div/label/span'                                  #第五个词选择
page_three='/html/body/content/div[2]/main/section[3]/div[3]/footer/' \
           'footer/div/ul/li[3]'                                                         #第3页
keyword_page3_20th='/html/body/content/div[2]/main/section[3]/div[3]/div/' \
                   'div[3]/table/tbody/tr[20]/td[1]/div/label/span'                  #第3页第二十个词选择
price_ratio='/html/body/content/div[2]/main/section[3]/div[4]/section[2]/' \
            'span[1]/div/input'                                                           #出价比例
day_cost='/html/body/content/div[2]/main/section[4]/div[2]/span[1]/div/input'     #日预算
create_confirm='/html/body/content/div[2]/main/section[4]/div[3]/button'            #确认创建
repet_create_close='/html/body/content/div[2]/div[3]/div/div[1]/button'              #复制投放关闭
new_plan_id='/html/body/content/div[2]/div/main/div/div[3]/table/tbody/' \
            'tr[1]/td[3]/div'                                                              #新建计划id