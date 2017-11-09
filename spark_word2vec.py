
# coding: utf-8

# In[ ]:


from pyspark.mllib.feature import Word2Vec
import pyspark
sc = pyspark.SparkContext()
from pyspark.sql.functions import format_number as fmt
import pymysql


# In[ ]:

conn = pymysql.connect(host = 'localhost', user = 'root', password = '140508    ', db = 'news', charset = 'utf8')
curs = conn.cursor()


# In[ ]:

def db_manager(noun, synonyms_1, synonyms_2, synonyms_3, synonyms_4, synonyms_5):
    sql = "insert into word2vec (noun, synonyms_1, synonyms_2, synonyms_3, synonyms_4, synonyms_5) values(%s,%s,%s,%s,%s,%s)"
    curs.execute(sql, (noun.encode('utf-8'), synonyms_1.encode('utf-8'), syn    onyms_2.encode('utf-8'), synonyms_3.encode('utf-8'), synonyms_4.encode('utf-8'),synonyms_5.encode('utf-8')))
    conn.commit()


# In[ ]:

def main():
    inp = sc.textFile("hdfs://hadoop2/input/result.txt").map(lambda row: row.split(" "))

    word2vec = Word2Vec()
    model = word2vec.fit(inp)

    ket = model.getVectors().keys()

    for noun in ket:
        num = 0
        synonym = ["" for _ in range(5)]
        synonyms = model.findSynonyms(noun, 5)

        for word, cosince_distance in synonyms:
            synonym[num] = word
            num = num + 1
        try:
            print(noun.encode('utf-8'))
            db_manager(noun, synonym[0], synonym[1], synonym[2], synonym[3],synonym[4])
        
        except Exception as err:
            print(err)
            pass


# In[ ]:

if __name__ == '__main__':
    main()

