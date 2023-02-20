f = open('smile.txt', 'r')
ref = f.read()
f = open('orig.txt','r')
orig = f.read()
letters = "-","А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы","Ь","Э","Ю","Я","а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы","ь","э","ю","я","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" , "M" , "N" ,"O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V" , "W" , "X" , "Y","Z"
wordsref = []
wordsorig = []
buff =""
for i in ref:
    if (i in letters):
        buff += i
    elif(buff != ""):
        wordsref.append(buff)
        buff = ""
buff =""
for i in orig:
    if (i in letters):
        buff += i
    elif(buff != ""):
        wordsorig.append(buff)
        buff = ""
amountofplag = 0
for i in range(len(wordsorig)-2):
    for j in range(len(wordsref)-2):
        if (wordsorig[i] == wordsref[j] and wordsorig[i + 1] == wordsref[j + 1] and wordsorig[i+ 2] == wordsref[j+2]):
            amountofplag += (len(wordsref[i]) + len(wordsref[i+1]) + len(wordsref[i+2]))
lenofref = 0
for i in range(len(wordsref)):
    lenofref += len(wordsref[i])
print("Процент плагиата - ",amountofplag/ lenofref* 100,"%")

