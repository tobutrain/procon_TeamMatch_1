import csv
import numpy as np
from gensim.models import word2vec
import pickle


print("起動準備中...")

# Word2Vecモデルのパスを指定
# w2vPath = "./jawiki.all_vectors.300d.txt"
# 類似度を測定するデータの指定
csvDirectory = "./testFile.csv"

# 以下変数定義
csv_header = ['ID', 'Word1', 'Word2', 'Word3']
dictIDKeyword = {}
num = 0
with open('./jawiki.all_vectors.300d.pickle', mode='rb') as fp:
    w2vModel = pickle.load(fp)

# 仕様: cosWord
# IN: 単語1,単語2(文字列) OUT:cos類似度(0<=n<=1) (実数型)


def cosWord(word1, word2):
    vec1 = w2vModel[word1]
    vec2 = w2vModel[word2]
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def teamcos(t1, t2):
    # s1 = len(t1)
    # s2 = len(t2)
    if len(t1) < len(t2):
        t1, t2 = t2, t1
        # s1, s2 = s2, s1
    max = 0
    for i in t1:
        for j in t1:
            if j == i:
                break
            for k in t1:
                if k == i or k == j:
                    break
                for a in t2:
                    for b in t2:
                        if b == a:
                            break
                        for c in t2:
                            if c == a or c == b:
                                break
                            t = abs(cosWord(i, a))
                            t += abs(cosWord(j, b))
                            t += abs(cosWord(k, c))
                            if max < t:
                                max = t
    print(max)
    return max


word1 = ["人工知能", "コンピュータ", "スマホ"]
word2 = ["AI", "機械学習", "人類", "感情"]


print("OK.")
n = int(input())
w = [list(map(str, input().split(" "))) for _ in range(n)]
table = [[-1 for i in range(n)] for j in range(n)]
for i in range(n):
    print(w[i])


# for i in range(n):
#    input_line = input()
#    m.append(input_line[0])
#    w.append([])
#    for j in range(len(input_line)-1):
#       w[i].append(input_line[j+1])

for i in range(n-1):
    for j in range(i+1, n):
        table[i][j] = teamcos(w[i], w[j])
for i in range(n):
    print(table[i])

# ans = teamcos(word1, word2)
# print(str(ans))

# csvDirectoryに指定したcsvファイルをdictIDKeyword(辞書型)に落とし込む
# dictIDKeyword = {key -> 0-n(グループ数), value -> {key -> csv_header : value -> csv内の値(チームID,収集した単語など)}}
# ex) dictIDKeyword[0]['ID'] = 101 , dictIDKeyword[0]['Word1']='かっつー'

# with open(csvDirectory) as dictFile :
#     for row in csv.DictReader(dictFile,csv_header):
#         dictIDKeyword[num] = row
#         num += 1
