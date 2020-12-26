import math

def add_word_dic(words_dict, word):
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

def find_word_dic(dicts_list, word):
    numberOfRepeat = 0
    for i in range(len(dicts_list)):
        if word in dicts_list[i]:
            numberOfRepeat += 1
    return numberOfRepeat

text=[  "duran duran sang wild boys in 1984",
        "wild boys don't remain forever wild",
        "who brought wild flowers",
        "it was john krakauner who wrote in to the wild"]

dictForSentences = dict()       # Her Kelimenin Olduğu Sözlük
dictForEachSentences = dict()   # Terimin Her Cümledeki Tekrarlama 
                                # Sayısını Tutan Dictionary (Geçici Sözlük)

N = len(text)                   # Toplam Cümle Sayısı
listForEachSentences = []       # Elemanları, Cümlelerin Sözlüklerinden Oluşan Liste
listForSentences = []           # Elemanları, Cümlelerin Kelime Listesinden Oluşan Liste
          
for i in  range(N):
    listForSentences.append(text[i].split())

for i in range(N):
    for j in range( len(listForSentences[i]) ):
        add_word_dic(dictForSentences, listForSentences[i][j])

for i in range(N):
    for j in range( len(listForSentences[i]) ):
        add_word_dic(dictForEachSentences, listForSentences[i][j])
    listForEachSentences.append(dictForEachSentences.copy())
    dictForEachSentences.clear()

listAllSentences = list(dictForSentences.keys())
width, height = len(listAllSentences), N
answerMatrix = [[0.0 for x in range(width)] for y in range(height)] 

for i in range(N):
    for j in range( len(listAllSentences) ):
        if listAllSentences[j] in listForEachSentences[i]:
            df = find_word_dic(listForEachSentences, listAllSentences[j])
            idf = math.log10( N / df )
            tf = listForEachSentences[i].get(listAllSentences[j])
            tfidf = idf * tf
            answerMatrix[i][j] = format(tfidf, ".3f")

print(listAllSentences,end="\n\n")
for i in range(N):
    print(answerMatrix[i])
