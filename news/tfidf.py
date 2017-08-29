
# coding: utf-8

# In[1]:

#전체 기사 내용에서 쓰이는 단어들의 tf-idf 값을 구해서 자주 쓰이는 쓸모없는 단어들을 수치로 표현해준다.
import sys
from konlpy.tag import Twitter
from konlpy.tag import Mecab
from collections import Counter
import os
import math
import re


# In[111]:

#tfidf를 구하기 위해서 tf와 idf를 구하기 위한 시작 1글자 이상의 단어만
# 생각해볼점 한글자인 것들을 제거 한후 할 것인지 아니면 1글자들도 tf-idf 를 구해서 제거해서 할 것인지
# 제거 한 후 하는 것은 한 글자들은 대체로 의미가 없는 단어들이지만 필요한 단어가 있을 수도 있으며 좋은 점은 tf-idf 후 글자 clean의 시간을 단축시킴
# 제거 하지 않으면 실제로 필요한 단어들도 존재 할 수 있으며 자주쓰이는 단어는 당연히 골라 낼 수 있을 것이다. 하지만 clean 시간이 길어 진다.
def get_tags(text):
    spliter = Twitter()
    #spliter = Mecab()
    nouns = spliter.nouns(text)
    count = Counter(nouns)
    return_list = []
    for n, c in count.most_common():
        if len(n) > 1:
            temp = {'tag': n, 'count': c, 'dict_count' : 1}
            return_list.append(temp)
        #temp = {'tag': n, 'count': c, 'dict_count' : 1}
        #return_list.append(temp)
    return return_list


# In[112]:

#tfidf가 0에 가까울 수록 좋지 제거 대상
#파라미터로는 각각의 단어에 대한 단어의 총 count와 어떤 문서에 쓰여져있는지의 count를 저장한 dict를 가져오고 총 문서의 수인 dict_num을 가져온다.
#많은 문서에서 쓰이는 단어 일수록 idf 값이 0에 가까워 지며 그로 인해 tf-idf 값이 0에 가까워 지면 제거 대상이다.
#로그빈도를 이용해서 tf값을 구했다. 값이 커지는 것을 막을 수 있다.
def tfidf_func(result_dict, dict_num):
    result = []
    for tag in result_dict:
        tf = math.log10(result_dict[tag][0] + 1)
        idf = math.log10(dict_num / result_dict[tag][1])
        tfidf = tf * idf
        #print(tag,result_dict[tag][0],result_dict[tag][1],tfidf)
        #tfidf 값을 조절해서 자주쓰이는 단어에 대해 알아낼수 있다.
        if tfidf < 1.9 and result_dict[tag][0] > 10:
            result.append(tag)
            print(tag,result_dict[tag][0],result_dict[tag][1],tfidf)
    #print(dict_num)
    #print(result)
    return result


# In[113]:

#tfidf 하기
#처음에는 각각의 문서에 쓰여져 있는 단어의 count와 문서 count값을 가져와서 diction에 저장하고 계속해서 
def result_tfidf():
    num = 0
    #전체 문서에 쓰인 명사와 그 명사의 count, 명사의 문서에 쓰인 count 수를 저장하기 위한 변수
    result_dict = {}
    
    for (path, dir , files) in os.walk("article_dict"):
        #존재 여부 확인
        for fname in dir:
            fullname = path+"/"+fname
            #print(fullname)
            for file in os.listdir(fullname):
                #print(file)
                if file.endswith(".txt"):
                    open_text_file = open(fullname+"/"+file, 'r')
                    text = open_text_file.read()
            
                    #get_tags(text)를 통해 하나의 문서에 쓰인 명사와 그 명사의 count수 그리고 문서 count수인 1을 return 받는다.
                    tags = get_tags(text)
                    open_text_file.close()
            
                    #전체적인 명사와 count, dict_count를 저장해 result_dict에 그 값들을 저장한다. 
                    for tag in tags:
                        noun = tag['tag']
                        count = tag['count']
                        dict_count = tag['dict_count']
                        if noun in result_dict:
                            result_dict[noun][0] += count
                            result_dict[noun][1] += dict_count
                        else:
                            result_dict[noun] = [count, dict_count]
                    
                    #총 문서의 수를 저장하기 위해 사용하는 변수 하나의 문서를 처리할떄 마다 값을 1증가 시킨다.        
                    num = num + 1
                
    #위에서 계산한 result_dict와 전체 문서의 수인 num값을 파라미터로 넘겨준다.        
    return tfidf_func(result_dict, num)  


# In[94]:

#tfidf를 통해 얻어온 제거 대상을 clean해주는 함수.
def clean_text(text,remove_list):
    cleaned_text = re.sub(remove_list, '', text)
    return cleaned_text


# In[109]:

#main function 각 문서들의 최종 clean된 명사들을 word2vec하기위해 하나의 txt파일에 저장한다.
def main():
    spliter = Twitter()
    remove_list = '|'.join(result_tfidf())
    #입력 파일명 = file
    for (path, dir , files) in os.walk("article_dict"):
        for fname in dir:
            fullname = path+"/"+fname
            print(fullname)
            for file in os.listdir(fullname):
                #존재 여부 확인
                if file.endswith(".txt"):
                    #출력 파일명
                    output_file_name = 'result.txt'
                    #output_file_name = 'konlpy/konlpy'+str(num)+'.txt'
                    print(fullname+"/"+file)
                    open_text_file = open(fullname+'/'+file, 'r')
                    text = open_text_file.read()
                    open_text_file.close()
            
                    #open_output_file = open(output_file_name, 'w')
                    open_output_file = open(output_file_name, 'a+')
            
                    result_text = clean_text(text,remove_list)
                    nouns = spliter.nouns(result_text)
                    
                    for n in nouns:
                        if len(n) > 1:
                            open_output_file.write(' ' + n)
                    open_output_file.write('\n')
                    open_output_file.close()


# In[110]:

if __name__ == '__main__':
    main()

