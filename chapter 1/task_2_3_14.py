dict = {}
#-----------WORDS-----------
wordsCol = int(input())
for i in range(0, wordsCol):
    words = input().lower()
    dict[words] = None 
#-----------SENTENCES-----------
sentenceCol = int(input())
massiv = []
# sozdat massiv i vse predlozheniya dobavit v massiv
for j in range(0, sentenceCol):
    sentence = input().lower()
    massiv.append(sentence)

#-----------SPLIT----------- 
dict2 = {}
for c in massiv:
    sentenceSplit = c.split(' ')
    for k in sentenceSplit:
        if k not in dict:
            dict2[k] = None
for v in dict2.keys():
    print(v)