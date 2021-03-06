#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
from selenium import webdriver

import time
import sys
import re
import math
import numpy  
import pandas as pd 
import os
import random

print("-" *80)
print("=" *80)
print("\n")

query_txt = input('영화 제목을 입력하세요: ')
query_url = 'https://movie.naver.com'

cnt = int(input('리뷰 건수를 입력하세요: '))
page_cnt = math.ceil(cnt / 10)

f_dir = input("폴더명을 입력하세요(예:c:\\temp\\):")
print("-" *80)

now = time.localtime()
s = '%04d-%02d-%02d-%02d-%02d-%02d' % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
os.makedirs(f_dir+s+'-'+query_txt)
os.chdir(f_dir+s+'-'+query_txt)

ff_name=f_dir+s+'-'+query_txt+'\\'+s+'-'+query_txt+'.txt'
fc_name=f_dir+s+'-'+query_txt+'\\'+s+'-'+query_txt+'.csv'
fx_name=f_dir+s+'-'+query_txt+'\\'+s+'-'+query_txt+'.xls'

s_time = time.time( )

path = "E:/temp/chromedriver_240/chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get(query_url)
time.sleep(2)

element = driver.find_element_by_id("ipt_tx_srch")
element.send_keys(query_txt)
driver.find_element_by_xpath("""//*[@id="jSearchArea"]/div/button""").click()
driver.find_element_by_xpath("""//*[@id="old_content"]/ul[2]/li/dl/dt/a""").click()
        
driver.find_element_by_link_text("평점").click()


driver.switch_to.frame('pointAfterListIframe')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

result= soup.find('div', class_='score_total').find('strong','total').find_all('em')
result2 = result[0].get_text()

print("=" *80)
result3 = result2.replace(",","")
result4 = re.search("\d+",result3)
search_cnt = int(result4.group())

if cnt > search_cnt :
    cnt = search_cnt

print("전체 검색 결과:",search_cnt,"건")
print("실제 검색 결과:",cnt, "건")

print("\n")
page_cnt = math.ceil(cnt / 10)
print("총 페이지: ",page_cnt)
print("=" *80)


score2=[]
review2=[]
writer2=[]
wdate2=[]
gogam2=[]
g_gogam2=[]
b_gogam2=[]
dwlist2=[]

count = 0         
click_count = 1   

while ( click_count <= page_cnt )  :
            
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            
            score_result = soup.select('div.score_result')[0]
            slist = score_result.find_all('li')

            for li in slist:

                count += 1
                
                f = open(ff_name, 'a',encoding='UTF-8')
            
                print("\n")
                print("총 %s 건 중 %s 번째 리뷰 데이터를 수집합니다..." %(cnt,count))
                score = li.find('div', class_='star_score').find('em').get_text()
                print("1.별점:", score , "점")
                score2.append(score)
                f.write("\n")
                f.write("총 %s 건 중 %s 번째 리뷰 데이터를 수집합니다..." %(cnt,count) + "\n")
                f.write("1.별점:"+score + "\n")
            
                review = li.find('div', class_='score_reple').find('p').get_text().strip()
                print("2.리뷰내용:",review)
                f.write("2.리뷰내용:" + review + "\n")
                review2.append(review)
         
                dwlist = li.find('div',class_='score_reple').find_all('em')
                writer = dwlist[0].find('span').get_text()
                print("3.작성자:",writer)
                f.write("3.작성자:" + writer + "\n")
                writer2.append(writer)
                
                wdate = dwlist[1].text
                print('4.작성일자:',wdate)
                f.write("4.작성일자:" + wdate + "\n")
                wdate2.append(wdate)
            
                gogam = li.find('div', class_='btn_area').find_all('strong')
                g_gogam = gogam[0].text
                print('5.공감:',g_gogam)
                f.write("5.공감:" + g_gogam + "\n")
                g_gogam2.append(g_gogam)
                
                b_gogam = gogam[1].text
                print('6.비공감:', b_gogam)
                f.write("6.비공감:" + b_gogam + "\n")
                b_gogam2.append(b_gogam)
                print("\n")

                

                if count == cnt :
                    break
            
            time.sleep(random.randrange(1,2))  

            click_count += 1
            
            if click_count > page_cnt :
                break
            else :
                driver.find_element_by_link_text("%s" %click_count).click()

            time.sleep(random.randrange(1,2))  


naver_movie = pd.DataFrame()
naver_movie['별점(평점)']=score2
naver_movie['리뷰내용']=review2
naver_movie['작성자']=writer2
naver_movie['작성일자']=wdate2
naver_movie['공감횟수']=g_gogam2
naver_movie['비공감횟수']=b_gogam2

naver_movie.to_csv(fc_name,encoding="utf-8-sig",index=True)

naver_movie.to_excel(fx_name ,index=True)

e_time = time.time( )
t_time = e_time - s_time


print("\n") 
print("=" *80)
print("1.%s 건 리뷰 중 실제 검색 건수: %s 건" %(cnt,count))
print("2.총 소요시간: %s 초 입니다 " %round(t_time,1))
print("3.파일 저장 완료: txt 파일명 : %s " %ff_name)
print("4.파일 저장 완료: csv 파일명 : %s " %fc_name)
print("5.파일 저장 완료: xls 파일명 : %s " %fx_name)
print("=" *80)

driver.close( )


# In[ ]:




