import pickle
import pandas as pd
from gensim.models import word2vec

w2vModel = word2vec.KeyedVectors.load_word2vec_format('jawiki.all_vectors.300d.txt', binary=False, encoding='utf-8')
with open('./jawiki.all_vectors.300d.pickle',mode='wb') as fp:
  pickle.dump(w2vModel,fp) 