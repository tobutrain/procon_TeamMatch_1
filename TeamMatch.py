import csv
import numpy as np
from gensim.models import word2vec

#Word2Vecモデルのパスを指定
w2vPath = "./jawiki.all_vectors.100d.txt"
#類似度を測定するデータの指定
csvDirectory = "./testFile.csv"

#以下変数定義
csv_header = ['ID','Word1','Word2','Word3']
dictIDKeyword = {}
num = 0
#w2vModel = word2vec.KeyedVectors.load_word2vec_format(w2vPath,binary=False,encoding='utf-8')

#仕様: cosWord 
#IN: 単語1,単語2(文字列) OUT:cos類似度(0<=n<=1) (実数型)
def cosWord(word1,word2):
    vec1 = w2vModel[word1]
    vec2 = w2vModel[word2]
    return np.dot(vec1,vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

#csvDirectoryに指定したcsvファイルをdictIDKeyword(辞書型)に落とし込む
# dictIDKeyword = {key -> 0-n(グループ数), value -> {key -> csv_header : value -> csv内の値(チームID,収集した単語など)}}
#ex) dictIDKeyword[0]['ID'] = 101 , dictIDKeyword[0]['Word1']='かっつー' 

with open(csvDirectory) as dictFile :
    for row in csv.DictReader(dictFile,csv_header):
        dictIDKeyword[num] = row
        num += 1