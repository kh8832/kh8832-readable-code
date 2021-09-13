path = './dictionary-data.txt'
f = open(path,'r',encoding='utf-8')
words_in_file = f.readline()

print(words_in_file)