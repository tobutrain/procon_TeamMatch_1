# NITOyC Procon Project TeamMatchingApp (2022)

## 関数仕様
### cosWord(Word1,Word2)
入力された文字列2つのcos類似度を返します。  

IN: 文字列 x 2  
OUT: 実数型 x 1 

## 使用法
モデルを同ディレクトリに配置しておきます。
その際に、付属のtopickle.pyで直列化しておくとプログラム実行時に高速にモデルを読み込めます。
次に、TeamMatch.pyを実行し入力に
```
N
Word Word Word ... Word 
Word Word Word ... Word 
Word Word Word ... Word 
:
:
Word Word Word ... Word 
```
の形式で入力します。
結果が配列で返されるので、Excel等で解析しましょう。