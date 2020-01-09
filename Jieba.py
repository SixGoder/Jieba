import jieba

text = open('text.txt', 'r', encoding = 'utf-8').read()
len(text)

text = text.lower()

stwlist = ['the','a','of','to','end','in','you','is','that','for','on','it','as','your','...','14',
           'this','or','20','40','27','30','13','21','26','10','15','22',
           '32','31','1','2','4','5','6','7','8','9','0','10','11','12','13',
           '12','13','15','16','17','25','33','35','36','18','23','19','24',
           '38','29','34','37','000','...............................']

words = jieba.cut(text, cut_all = False, HMM = True)

word_  = {}
for word in words:
    if (word.strip() not in stwlist):
        if len(word) > 1:
            if word != '\t':
                if word != '\r\n':

                    if word in word_:
                        word_[word] += 1
                    else:
                        word_[word] = 1

word_freq = []
for word, freq in word_.items():
    word_freq.append((word, freq))

word_freq.sort(key = lambda x:x[1], reverse = True)

for i in range(3500):
    word, freq = word_freq[i]
    print('{0:10}{1:5}'.format(word, freq))