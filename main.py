print('テキストファイルのパスを入力してください')
path = input()

f = open(path,'r',encoding='utf-8')
words_in_file = f.readlines()
f.close()

for i,word in enumerate(words_in_file):
    print(word,end='')