"""新建MVP计划时需要用到的常量，网页结构修改时需要修改对应的常量"""

id='252'
quick_login='http://192.168.8.201/bax/user/login/local?user_id=%s'% id             #骇客登录，账号13127811381
main_page='http://192.168.8.201/main'                                                  #bax主页
add='/html/body/content/div[1]/main/ul/li[3]/ul/li[1]/p'                           #新建推广计划页面
choose='/html/body/content/div[2]/main/section[1]/main/div[2]/' \
       'section[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[1]/div/div/label'      #选择第一个帖子
choose_confirm='/html/body/content/div[2]/main/section[1]/main/div[2]/' \
               'section[2]/div/footer/span[2]/button[2]'                             #选择后确认
click_price='/html/body/content/div[2]/main/section[2]/main/div[1]/div/div/' \
            'input'                                                                        #点击单价
day_cost='/html/body/content/div[2]/main/section[2]/main/div[2]/div/div/input'   #日预算
create_confirm='/html/body/content/div[2]/main/section[2]/footer/button'           #确认创建
more_choose='/html/body/content/div[2]/header[2]/div/span[1]/button'               #更多筛选
status_choose='/html/body/content/div[2]/header[2]/div[2]/section/span[1]/' \
              'div/div[1]/input'                                                          #投放状态选择
effect_status='/html/body/div[3]/div[1]/div[1]/ul/li[3]'                              #有效状态
new_plan_id='/html/body/content/div[2]/div/main/div/div[3]/table/tbody/' \
            'tr[1]/td[3]/div'                                                             #新建计划id