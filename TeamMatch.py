import csv
import numpy as np
from gensim.models import word2vec

#Word2Vecモデルのパスを指定
w2vPath = "./jawiki.all_vectors.100d.txt"
#類似度を測定するデータの指定
fileDirectory = "./testFile.csv"


csv_header = ['ID','Word1','Word2','Word3']
dictIDKeyword = {}
num = 0
w2vModel = word2vec.KeyedVectors.load_word2vec_format(w2vPath,binary=False,encoding='utf-8')

def cosWord(word1,word2):
    vec1 = w2vModel[word1]
    vec2 = w2vModel[word2]
    return np.dot(vec1,vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

#with open(fileDirectory) as dictFile :
#    for row in csv.DictReader(dictFile,csv_header):
#        print(row)
#        dictIDKeyword[num] = row
#        num += 1
