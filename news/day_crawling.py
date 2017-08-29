
# coding: utf-8

# In[16]:


import requests
from bs4 import BeautifulSoup
import re
from konlpy.tag import Twitter
import urllib.request
import sys
import pymysql


# In[ ]:

conn = pymysql.connect(host = 'localhost',
                      user = 'root',
                      password = '140508',
                      db = 'news',
                      charset = 'utf8')
curs = conn.cursor()


# In[10]:

#크롤링함수 url의 본문 내용 저장
def get_text(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    text = ''
    for item in soup.find_all('div', id='articleBodyContents'):
        text = text + str(item.find_all(text=True))
    return text


# In[11]:

#클리닝함수 본문 내용 클리닝
def clean_text(text):   
    cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;▶“’ⓒ:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]', '', cleaned_text)
    return cleaned_text


# In[12]:

# text저장 함수
# url을 get_text(url)을 통해 기사의 내용을 가져온후 clean_text 함수를 통해 clean_text로 
# 변경시켜 준후 명사화 시켜서 저장 
def article_text(URL, num, day):
    spliter = Twitter()
    #spliter = Mecab()
    try:
        OUTPUT_FILE_NAME = 'article_dict/'+ day +'/article_'+ day +'_'+ str(num) +'.txt'
        open_output_file = open(OUTPUT_FILE_NAME, 'w')
        #result_text = clean_text(get_text(URL))
        #article_nouns = spliter.nouns(result_text)
        article_nouns = spliter.nouns(get_text(URL))
        for n in article_nouns: 
            if len(n) > 1 :
                open_output_file.write(' ' + n)
        open_output_file.close()
    finally:
        open_output_file.close()


# In[13]:

#db에 저장하는 함수
def db_manager(url, title, day):
    sql = "insert into data (url, title, date) values(%s,%s,%s)"
    curs.execute(sql, (url, title, day))
    conn.commit()


# In[14]:

#input ex) 20170808. 날짜 입력해서 crawling하기
def main(day):
    page = 1
    temp_page = 0
    #db에 저장 시킬 id
    db_id = 0
    first_url = ''
    
    while 1 == 1:
        url = 'http://news.naver.com/main/list.nhn?sid1=100&listType=title&mid=sec&mode=LSD&date='+str(day)+'&page='+str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'lxml')
        
        for body in soup.find_all("a", class_="nclicks(fls.list)"):
             
            #db에 저장 시킬 url
            url = body.get('href')
            
            #마지막 페이지에 도달할시 함수 종료
            if first_url == url:
                return
            
            #db에 저장 시킬 article title
            title = str(body.find_all(text=True))
            #db에 저장 시킬 명사화된 article title 하지만 넣을지 말지 고민....
            #nouns_title = clean_text(str(spliter.nouns(title)))
            
            #마지막 페이지를 구별하기 위해 만듬
            if temp_page != page:
                first_url = url
                temp_page += 1
            
            #db에 저장시킬 함수 호출
            db_manager(url, title, str(day))
            
            print(url)
            #print(title)
            #날짜 폴더가 생성되있어야 한다. 본문내용 저장 함수 호출
            article_text(url,db_id,str(day))
            
            db_id += 1
        page += 1


# In[ ]:

if __name__ == '__main__':
    main(sys.argv[1])

