import time
fib = []
fib.append(1)
fib.append(2)
for i in range(2,500):
    fib.append(fib[i-2] + fib[i-1])
fib1 = list(map(str,fib))
fib1 = "".join(fib1)
numb = [str(i) for i in range(10,100)]
stats = [0] * 90
# Наивный алгоритм
def naiv():
    start = time.time()
    for i in range(len(numb)):
        for j in range(len(fib1) - 1):
            if (fib1[j] == numb[i][0] and fib1[j + 1] == numb[i][1]):
                stats[i] += 1
    end = time.time() - start
    print("Наиболее часто встречаемое число - ",(max(stats) in stats) + 10," время выполнения программы наивным алгоритмом - ",end)
# Алгоритм Рабина-карпа
def rabin_carp():
    start = time.time()
    for i in range(len(numb)):
        basehash = int(numb[i][0]) * 10 + int(numb[i][1])*1
        for j in range(len(fib1)-1):
            newhash = int(fib1[j])*10 + int(fib1[j + 1])
            if (basehash == newhash):
                if (fib1[j] == numb[i][0] and fib1[j + 1] == numb[i][1]):
                     stats[i] +=1
    end = time.time() - start
    print("Наиболее часто встречаемое число - ",(max(stats) in stats) + 10," время выполнения программы алгоритмом Рабина Карпа - ",end)
#Алгоритм Бойера-Мура
def boyer_mur():
    start = time.time()
    for i in range(len(numb)):
        j = 0
        while j < len(fib1) - 1:
             if(fib1[j+1] != numb[i][1]):
                 if (fib1[j+1] != numb[i][0]):
                     j += 2
                 else:
                    j+=1
             elif(fib1[j] == numb[i][0]):
                 stats[i] += 1
                 j+=1
             else:
                 j+=1


    end = time.time() - start
    print("Наиболее часто встречаемое число - ",(max(stats) in stats) + 10," время выполнения программы алгоритмом Бойера - Мура - ",end)
# Алгоритм Кнута-Морриса-Пратта
def prefixdouble(s):
    arr = [0]*2
    if(s[0] == s[1]):
        arr[1] = 1
    return arr
def KnutMorrisPrat():
    start = time.time()
    for p in range(len(numb)):
        n = prefixdouble(numb[0])
        i = 0
        j = 0
        while i < len(fib1):
            if fib1[i] == numb[j]:
                i += 1
                j += 1
                if j == len(numb[p]):
                    stats[p] +=1
                    j = 0
            else:
                if j > 0:
                    j = n[j - 1]
                else:
                    i += 1
    end = time.time() - start
    print("Наиболее часто встречаемое число - ",(max(stats) in stats) + 10," время выполнения программы алгоритмом Кнутта Морриса Пратта - ",end)

naiv()
rabin_carp()
boyer_mur()
KnutMorrisPrat()



