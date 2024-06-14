import random as rd

#temel yapı
hash_word = {"a": 1, "b": 2, "c": 3, "d": 4,"e": 5,"f": 6,"g": 7,"h": 8,"i": 9
       , "j": 10,"k": 11,"l": 12,"m": 13,"n": 14, "o": 15, "p": 16, "q": 17, "r": 18
       , "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24,"y": 25}
findCripted = []
find = []



#mesaj
def clearList():
    findCripted.clear()
    find.clear()


#yazimizi cripto yapiyor 
#kontrol edecegimiz yapi burda list yeni eklenmeden bos mu dolu mu kontrolu
def cripto(wordList, hash_word):
    for i in hash_word:
        for j in wordList:
            findCripted.append(hash_word[j])
        break
    return findCripted


#sifreleme de dictonary icin valueleri random olusturuyor
def randomRefresh():
    for i in hash_word:
        hash_word[i] = rd.randint(1, 100)  # 1 ile 100 arasında rastgele bir sayı

#sifrelemeyi cozuyoruz
def uncripted(findCripted,hash_word):
    for findCripted in findCripted:
        for key, value in hash_word.items():
            if value == findCripted:
                find.append(key)
    return str(find) 


def interface():
    while True:
        print("----------------------------------------------")
        print("-------------Welcome to Interface-------------")
        print("------------1)Create hash message-------------")
        print("------------2)Uncripted hash message----------")
        print("------------3)Clear hash code---------------")
        print("------------4)Resrefh hash code---------------")
        print("------------5)Exit----------------------------")
        whichOne = int(input("Which one: "))
        if whichOne == 1:
            #interface alani
            word = input("enter word:")
            wordNew = (" ").join(word)
            wordList = wordNew.split()
            cripto(wordList,hash_word)
        elif whichOne == 2:
            uncript = uncripted(findCripted,hash_word)
            print(uncript)
        elif whichOne == 3:
            clearList()
        elif whichOne == 4:
            randomRefresh()
        elif whichOne == 5:
            break
        else:
            print("Unknown")


interface()