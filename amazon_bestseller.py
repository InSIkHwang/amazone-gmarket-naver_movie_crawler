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
import xlwt 
import random
import os

import urllib.request
import urllib

print("=" *80)
print("아마존 닷컴의 분야별 Best Seller 상품 정보 추출하기")
print("=" *80)

query_txt='아마존닷컴'
query_url='https://www.amazon.com/bestsellers?ld=NSGoogle'

sec = input('''
    1.Amazon Devices & Accessories     2.Amazon Launchpad            3.Appliances
    4.Apps & Games                     5.Arts, Crafts & Sewing       6.Audible Books & Originals
    7.Automotive                       8.Baby                        9.Beauty & Personal Care      
    10.Books                           11.CDs & Vinyl                12.Camera & Photo             
    13.Cell Phones & Accessories       14.Clothing, Shoes & Jewelry  15.Collectible Currencies       
    16.Computers & Accessories         17.Digital Music              18.Electronics                
    19.Entertainment Collectibles      20.Gift Cards                 21.Grocery & Gourmet Food     
    22.Handmade Products               23.Health & Household         24.Home & Kitchen             
    25.Industrial & Scientific         26.Kindle Store               27.Kitchen & Dining           
    28.Magazine Subscriptions          29.Movies & TV                30.Musical Instruments        
    31.Office Products                 32.Patio, Lawn & Garden       33.Pet Supplies               
    34.Prime Pantry                    35.Smart Home                 36.Software                   
    37.Sports & Outdoors               38.Sports Collectibles        39.Tools & Home Improvement   
    40.Toys & Games                    41.Video Games

    1.분야의 번호를  선택하세요: ''')

cnt = int(input('2.건수를 입력하세요(1~100): '))

f_dir = input("3.폴더명을 입력하세요(예:c:\\temp\\):")
print("\n")

if sec == '1' :
      sec_name='Amazon Devices and Accessories'
elif sec =='2' :
      sec_name='Amazon Launchpad'
elif sec =='3' :
      sec_name='Appliances'
elif sec =='4' :
      sec_name='Apps and Games'
elif sec =='5' :
      sec_name='Arts and Crafts and Sewing'
elif sec =='6' :
      sec_name='Audible Books and Originals'        
elif sec =='7' :
      sec_name='Automotive'        
elif sec =='8' :
      sec_name='Baby'
elif sec =='9' :
      sec_name='Beauty and Personal Care'
elif sec =='10' :
      sec_name='Books'
elif sec =='11' :
      sec_name='CDs and Vinyl'
elif sec =='12' :
      sec_name='Camera and Photo'
elif sec =='13' :
      sec_name='Cell Phones and Accessories'
elif sec =='14' :
      sec_name='Clothing and Shoes and Jewelry'
elif sec =='15' :
      sec_name='Collectible Currencies'
elif sec =='16' :
      sec_name='Computers and Accessories'
elif sec =='17' :
      sec_name='Digital Music'
elif sec =='18' :
      sec_name='Electronics'
elif sec =='19' :
      sec_name='Entertainment Collectibles'
elif sec =='20' :
      sec_name='Gift Cards'
elif sec =='21' :
      sec_name='Grocery and Gourmet Food'
elif sec =='22' :
      sec_name='Handmade Products'
elif sec =='23' :
      sec_name='Health and Household'
elif sec =='24' :
      sec_name='Home and Kitchen'
elif sec =='25' :
      sec_name='Industrial and Scientific'
elif sec =='26' :
      sec_name='Kindle Store'
elif sec =='27' :
      sec_name='Kitchen and Dining'
elif sec =='28' :
      sec_name='Magazine Subscriptions'
elif sec =='29' :
      sec_name='Movies and TV'
elif sec =='30' :
      sec_name='Musical Instruments'
elif sec =='31' :
      sec_name='Office Products'
elif sec =='32' :
      sec_name='Patio and Lawn and Garden'
elif sec =='33' :
      sec_name='Pet Supplies'
elif sec =='34' :
      sec_name='Prime Pantry'
elif sec =='35' :
      sec_name='Smart Home'
elif sec =='36' :
      sec_name='Software'
elif sec =='37' :
      sec_name='Sports and Outdoors'
elif sec =='38' :
      sec_name='Sports Collectibles'
elif sec =='39' :
      sec_name='Tools and Home Improvemen'
elif sec =='40' :
      sec_name='Toys and Games'
elif sec =='41' :
      sec_name='Video Games'

print("*" *80)
print("데이터 수집중...")
print("*" *80)
      

now = time.localtime()
s = '%04d-%02d-%02d-%02d-%02d-%02d' % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

os.makedirs(f_dir+s+'-'+query_txt+'-'+sec_name)
os.chdir(f_dir+s+'-'+query_txt+'-'+sec_name)

ff_dir=f_dir+s+'-'+query_txt+'-'+sec_name
ff_name=f_dir+s+'-'+query_txt+'-'+sec_name+'\\'+s+'-'+query_txt+'-'+sec_name+'.txt'
fc_name=f_dir+s+'-'+query_txt+'-'+sec_name+'\\'+s+'-'+query_txt+'-'+sec_name+'.csv'
fx_name=f_dir+s+'-'+query_txt+'-'+sec_name+'\\'+s+'-'+query_txt+'-'+sec_name+'.xls'

s_time = time.time( )

path = "E:/temp/chromedriver_240/chromedriver.exe"
driver = webdriver.Chrome(path)
    
driver.get(query_url)
time.sleep(5)

if sec == '1' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[1]/a""").click( )
elif sec == '2' :                    
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[2]/a""").click( )
elif sec == '3' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[3]/a""").click( )
elif sec == '4' : 
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[4]/a""").click( )
elif sec == '5' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[5]/a""").click( )
elif sec == '6' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[6]/a""").click( )
elif sec == '7' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[7]/a""").click( )  
elif sec == '8' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[8]/a""").click( )
elif sec == '9' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[9]/a""").click( )
elif sec == '10' : 
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[10]/a""").click( )
elif sec == '11' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[11]/a""").click( )
elif sec == '12' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[12]/a""").click( )
elif sec == '13' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[13]/a""").click( )
elif sec == '14' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[14]/a""").click( )
elif sec == '15' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[15]/a""").click( )
elif sec == '16' : 
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[16]/a""").click( )
elif sec == '17' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[17]/a""").click( )
elif sec == '18' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[18]/a""").click( )
elif sec == '19' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[19]/a""").click( )
elif sec == '20' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[20]/a""").click( )
elif sec == '21' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[21]/a""").click( )
elif sec == '22' : 
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[22]/a""").click( )
elif sec == '23' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[23]/a""").click( )
elif sec == '24' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[24]/a""").click( )
elif sec == '25' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[25]/a""").click( )
elif sec == '26' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[26]/a""").click( )
elif sec == '27' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[27]/a""").click( )
elif sec == '28' : 
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[28]/a""").click( )
elif sec == '29' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[29]/a""").click( )
elif sec == '30' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[30]/a""").click( )
elif sec == '31' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[31]/a""").click( )
elif sec == '32' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[32]/a""").click( )
elif sec == '33' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[33]/a""").click( )
elif sec == '34' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[34]/a""").click( )
elif sec == '35' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[35]/a""").click( )
elif sec == '36' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[36]/a""").click( )
elif sec == '37' : 
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[37]/a""").click( )
elif sec == '38' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[38]/a""").click( )
elif sec == '39' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[39]/a""").click( )
elif sec == '40' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[40]/a""").click( )
elif sec == '41' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[41]/a""").click( )

time.sleep(1)

def scroll_down(driver):
      
      driver.execute_script("window.scrollBy(0,9300);")
      time.sleep(1)

scroll_down(driver)

bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

img_src2=[]
file_no = 0


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

reple_result = soup.select('#zg-center-div > #zg-ordered-list')
slist = reple_result[0].find_all('li')

if cnt < 51 :
         
    ranking2=[]
    title3=[]
    price2=[]
    score2=[]
    sat_count2=[]
    store2=[]
       
    count = 0
    
    img_dir = ff_dir+"\\images"
    os.makedirs(img_dir)
    os.chdir(img_dir)

    for li in slist:
            
            try :
              photo = li.find('div','a-section a-spacing-small').find('img')['src']
            except AttributeError :
              continue
            file_no += 1

            urllib.request.urlretrieve(photo,str(file_no)+'.jpg')
            time.sleep(1)

            if cnt == file_no :
              break
            
            f = open(ff_name, 'a',encoding='UTF-8')
            f.write("-----------------------------------------------------"+"\n")


            print("-" *70)
            try :
             ranking = li.find('span',class_='zg-badge-text').get_text().replace("#","")
            except AttributeError :
             ranking = ''
             print(ranking.replace("#",""))
            else :
             print("1.판매순위:",ranking)

             f.write('1.판매순위:'+ ranking + "\n")

 
            try :
             title1 = li.find('div',class_='p13n-sc-truncated').get_text().replace("\n","")
            except AttributeError :
             title1 = ''
             print(title1.replace("\n",""))
             f.write('2.제품소개:'+ title1 + "\n")
            else :
             title2=title1.translate(bmp_map).replace("\n","") 
             print("2.제품소개:", title2.replace("\n",""))

             count += 1
             
             f.write('2.제품소개:'+ title2 + "\n")
            

             try :
               price = li.find('span','p13n-sc-price').get_text().replace("\n","")
             except AttributeError :
               price = ''
               
             print("3.가격:", price.replace("\n",""))
             f.write('3.가격:'+ price + "\n")
                  
             try :
                sat_count = li.find('a','a-size-small a-link-normal').get_text().replace(",","")
             except (IndexError , AttributeError) :
                sat_count='0'
                print('4.상품평 수: ',sat_count)
                f.write('4.상품평 수:'+ sat_count + "\n")
             else :
                print('4.상품평 수:',sat_count)
                f.write('4.상품평 수:'+ sat_count + "\n")


             try :
               score = li.find('span','a-icon-alt').get_text()
             except AttributeError :
               score=' '
               
             print('5.평점:',score)
             f.write('5.평점:'+ score + "\n")

             print("-" *70)
                          
             f.close( )
              
             time.sleep(0.3)
            
             ranking2.append(ranking)
             title3.append(title2.replace("\n",""))
             price2.append(price.replace("\n",""))

             try :   
               sat_count2.append(sat_count)
             except IndexError :
               sat_count2.append(0)

             score2.append(score)

             if count == cnt + 1 :
                break
                          
elif cnt >= 51 :    
    

    img_src2=[]   
    file_no = 0

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    count = 0

    reple_result = soup.select('#zg-center-div > #zg-ordered-list')
    slist = reple_result[0].find_all('li')


    img_dir = ff_dir+"\\images"
    os.makedirs(img_dir)
    os.chdir(img_dir)

    for li in slist:

            try :
              photo = li.find('div','a-section a-spacing-small').find('img')['src']
            except AttributeError :
              continue
            file_no += 1

            urllib.request.urlretrieve(photo,str(file_no)+'.jpg')
            time.sleep(1)

            if cnt == file_no :
              break
            
    ranking2=[]
    title3=[]
    price2=[]
    score2=[]
    sat_count2=[]
    store2=[]

    for li in slist:           
            f = open(ff_name, 'a',encoding='UTF-8')
            f.write("-----------------------------------------------------"+"\n")

            
            print("-" *70)
            try :
             ranking = li.find('span',class_='zg-badge-text').get_text().replace("#","")
            except AttributeError :
             ranking = ''
             print(ranking.replace("#",""))
            else :
             print("1.판매순위:",ranking)

             f.write('1.판매순위:'+ ranking + "\n")

             
            try :
             title1 = li.find('div',class_='p13n-sc-truncated').get_text().replace("\n","")
            except AttributeError :
             title1 = ''
             print(title1.replace("\n",""))
             f.write('2.제품소개:'+ title1 + "\n")
            else :
             title2=title1.translate(bmp_map).replace("\n","") 
             print("2.제품소개:", title2.replace("\n",""))

             count += 1
             
             f.write('2.제품소개:'+ title2 + "\n")
            
             
             try :
               price = li.find('span','p13n-sc-price').get_text().replace("\n","")
             except AttributeError :
               price = ''
               
             print("3.가격:", price.replace("\n",""))
             f.write('3.가격:'+ price + "\n")
                  
             try :
                sat_count = li.find('a','a-size-small a-link-normal').get_text().replace(",","")
             except (IndexError , AttributeError) :
                sat_count='0'
                print('4.상품평 수: ',sat_count)
                f.write('4.상품평 수:'+ sat_count + "\n")
             else :
                print('4.상품평 수:',sat_count)
                f.write('4.상품평 수:'+ sat_count + "\n")

            
             try :
               score = li.find('span','a-icon-alt').get_text()
             except AttributeError :
               score=' '
               
             print('5.평점:',score)
             f.write('5.평점:'+ score + "\n")

             print("-" *70)
                          
             f.close( )
              
             time.sleep(0.5)

             ranking2.append(ranking)
             title3.append(title2.replace("\n",""))
             price2.append(price.replace("\n",""))

             try :   
               sat_count2.append(sat_count)
             except IndexError :
               sat_count2.append(0)

             score2.append(score)

    
    driver.find_element_by_xpath("""//*[@id="zg-center-div"]/div[2]/div/ul/li[3]/a""").click( )
    print("*" *80)
    print("데이터 수집중...")
    print("*" *80)   
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    reple_result = soup.select('#zg-center-div > #zg-ordered-list')
    slist = reple_result[0].find_all('li')
    
    for li in slist:

        try :
              photo = li.find('div','a-section a-spacing-small').find('img')['src']
        except AttributeError :
              continue
        file_no += 1

        urllib.request.urlretrieve(photo,str(file_no)+'.jpg')
        time.sleep(1)

        if cnt == file_no :
              break


    for li in slist:
            
            f = open(ff_name, 'a',encoding='UTF-8')
            f.write("-----------------------------------------------------"+"\n")

            
            print("-" *70)
            try :
             ranking = li.find('span',class_='zg-badge-text').get_text().replace("#","")
            except AttributeError :
             ranking = ''
             print(ranking.replace("#",""))
            else :
             print("1.판매순위:",ranking)

             f.write('1.판매순위:'+ ranking + "\n")

             
            try :
             title1 = li.find('div',class_='p13n-sc-truncated').get_text().replace("\n","")
            except AttributeError :
             title1 = ''
             print(title1.replace("\n",""))
             f.write('2.제품소개:'+ title1 + "\n")
            else :
             title2=title1.translate(bmp_map).replace("\n","") 
             print("2.제품소개:", title2.replace("\n",""))

             count += 1
             
             f.write('2.제품소개:'+ title2 + "\n")
            
             
             try :
               price = li.find('span','p13n-sc-price').get_text().replace("\n","")
             except AttributeError :
               price = ''
               
             print("3.가격:", price.replace("\n",""))
             f.write('3.가격:'+ price + "\n")
                  
             try :
                sat_count = li.find('a','a-size-small a-link-normal').get_text().replace(",","")
             except IndexError :
                sat_count='0'
                print('4.상품평 수: ',sat_count)
                f.write('4.상품평 수:'+ sat_count + "\n")
             except AttributeError :
                sat_count='0'
                print('4.상품평 수: ',sat_count)
                f.write('4.상품평 수:'+ sat_count + "\n") 
             else :
                print('4.상품평 수:',sat_count)
                f.write('4.상품평 수:'+ sat_count + "\n")

            
             try :
               score = li.find('span','a-icon-alt').get_text()
             except AttributeError :
               score=' '
               
             print('5.평점:',score)
             f.write('5.평점:'+ score + "\n")

             print("-" *70)
                         
             f.close( )
              
             time.sleep(0.5)
             
             ranking2.append(ranking)
             title3.append(title2.replace("\n",""))
             price2.append(price.replace("\n",""))

             try :   
               sat_count2.append(sat_count)
             except IndexError :
               sat_count2.append(0)

             score2.append(score)
      
             if count == cnt + 1 :
                break
else :
      print(" 검색 건수는 최대 100 건까지만 가능합니다")
  

              
amazon_best_seller = pd.DataFrame()
amazon_best_seller['판매순위']=ranking2
amazon_best_seller['제품소개']=pd.Series(title3)
amazon_best_seller['판매가격']=pd.Series(price2)
amazon_best_seller['상품평 갯수']=pd.Series(sat_count2)
amazon_best_seller['상품평점']=pd.Series(score2)



amazon_best_seller.to_csv(fc_name,encoding="utf-8-sig",index=True)


amazon_best_seller.to_excel(fx_name ,index=True)

e_time = time.time( )
t_time = e_time - s_time


orig_stdout = sys.stdout
f = open(ff_name, 'a',encoding='UTF-8')
sys.stdout = f




import win32com.client as win32   
import win32api  
                     
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Open(fx_name)
sheet = wb.ActiveSheet
sheet.Columns(3).ColumnWidth = 30   
row_cnt = cnt+1
sheet.Rows("2:%s" %row_cnt).RowHeight = 120  

ws = wb.Sheets("Sheet1")
col_name2=[]
file_name2=[]

for a in range(2,cnt+2) :
      col_name='C'+str(a)
      col_name2.append(col_name)

for b in range(1,cnt+1) :
      file_name=img_dir+'\\'+str(b)+'.jpg'
      file_name2.append(file_name)
      
for i in range(0,cnt) :
      rng = ws.Range(col_name2[i])
      image = ws.Shapes.AddPicture(file_name2[i], False, True, rng.Left, rng.Top, 130, 100)
      excel.Visible=True
      excel.ActiveWorkbook.Save()


print("\n")
print("=" *50)
print("총 소요시간: %s 초" %t_time)
print("총 저장 건수: %s 건" %count)
print("=" *50)

sys.stdout = orig_stdout
f.close( )

print("\n") 
print("=" *80)
print("1.총 %s 건 중에서 실제 검색 건수: %s 건" %(cnt,count))
print("2.총 소요시간은: %s 초" %round(t_time,1))
print("3.파일 저장 완료: txt 파일명 : %s " %ff_name)
print("4.파일 저장 완료: csv 파일명 : %s " %fc_name)
print("5.파일 저장 완료: xls 파일명 : %s " %fx_name)
print("=" *80)    


# In[ ]:




