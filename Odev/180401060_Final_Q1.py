import random, enum


class direction(enum.Enum):                                 # Direction adında class tanımlandı.
    LR = 0                                                  # Soldan sağa (LR) değişkenine 0 ataması yapıldı.
    RL = 1                                                  # Sağdan sola (RL) değişkenine 1 ataması yapıldı.
    DU = 2                                                  # Aşağıdan yukarı (DU) değişkenine 2 ataması yapıldı.
    UD = 3                                                  # Yukarıdan aşağı (UD)  değişkenine 3 ataması yapıldı.


# Satır(rows) ve sütun(columns) parametreleri büyüklüğünde random harflerden matris oluşturan fonksiyon tanımlandı.
def createRandMatrix(rows, columns):                        
    words = 'ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ'              # Harf stringi oluşturuldu.
    wordList = list(words)                                  # String, harf listesine dönüştürüldü.
    random.shuffle(wordList)                                # Listenin elemanları karıştırıldı.
    wordMatrix = []                                         # Matris ana bloğu oluşturuldu.
    for row in range(rows):
        tempRow = []                                        # Bir tane iç blok oluşturuldu.
        for col in range(columns): 
            tempRow.append(random.choice(wordList))         # Harf listesinden rastgele eleman iç bloğa eklendi.
        wordMatrix.append(tempRow)                          # Oluşturulan iç blok, ana bloğa eklendi.
    return wordMatrix                                       # Oluşturulan matrix return edildi.
    

# Parametreleri baz alınan matris, satır, sütun değerleri ile atanacak kelime(sentence) olan fonksiyon tanımlandı.
def assign_operations_0(matrix, row, column, sentence):     # assign_operations_0 fonksiyonu, soldan sağa (LR) operasyonu yapmaktadır.
    row, column = row-1, column-1                           # Dizi işlemlerinde kolaylık olması için, satır ve sütun değerleri 1 azaltıldı.
    wordList = list(sentence)                               # Argümandaki kelime, harf atamasının yapılabilmesi dizi haline çevrildi.
    lenght = len(wordList)                                  # Atanacak harf sayısı hesaplandı.
    columnSize = len(matrix[0])                             # Matrisdeki sütun büyüklüğü hesaplandı.
    index, flag = 0, 1                                      # index değişkeni atanmakta olan harfin kelime dizisindeki sırasını belirtmektedir.
    controlsize = columnSize - column                       # controlsize argümandaki sütun sayısından sonra gelen, atama yapılabilecek max sütun sayısını ifade etmektedir.
    if controlsize < lenght:                                # Argümandaki kelime uzunluğunun, uygun sütun sayısından fazla olduğu durumda bu scope'a girilir.
        for i in range(column, columnSize):                 # İlk sefer ataması için, argümandaki sütun sayısından başlayıp sütun sonuna kadar(sağa doğru) atamalar yapılır.
            matrix[row][i] = wordList[index]                
            index += 1                                      # Atama yapıldığı için, index yani atama yapılacak harfin kelime dizisindeki sıra sayısı 1 artırılır.
        lenght -= index                                     # Atanacak harf sayısından, atama yapılan toplam harf sayısı çıkarıldı.
        while flag == 1:                                    # Kelimenin tüm harfleri için atamalar yapılacağı için, kelime bitene kadar flag değeri 1 olarak belirlendi.
            if index != len(wordList):                      # Atanacak harfin dizideki sırasının, dizi büyüklüğüne eşitliği kontrol edildi.
                if lenght < columnSize:                     # Atanacak harf sayısının, matrisin sütun büyüklüğü ile karşılaştırılması yapıldı.
                    for i in range(0, lenght):              # Sütun başından başlayıp, atanacak harf sayısınca sağa doğru atamalar yapılır.
                        matrix[row][i] = wordList[index]    
                        index += 1                          # Atama yapıldığı için, index yani atama yapılacak harfin kelime dizisindeki sıra sayısı 1 artırılır.
                else:                                       # Atanacak harf sayısının, matrisin sütun büyüklüğünden büyük olduğu durumda bu scope'a girilir. 
                    for i in range(0, columnSize):          # Sütun başından başlayıp, matrisdeki sütun sayısınca sağa doğru atamalar yapılır.
                        matrix[row][i] = wordList[index]    
                        index += 1                          # Atama yapıldığı için, index yani atama yapılacak harfin kelime dizisindeki sıra sayısı 1 artırılır.
                    lenght -= columnSize                    # Atanacak harf sayısından, atama yapılan toplam harf sayısı (bu durumda sütun sayısı oluyor.) çıkarıldı.
            else:                                           # Atanacak harfin dizideki sırasının, dizi büyüklüğüne eşit olması durumunda kelimenin tüm harfler atanmış demektir.
                flag = 0                                    # Kelimenin türm harfleri atandığı için while döngüsünün kırılması adına flag = 0 ataması yapıldı.
    else:                                                   # Argümandaki kelime uzunluğunun, uygun sütun sayısından az olduğu durumda bu scope'a girilir.
        for i in range(column, column+lenght):              # Argümandaki sütun sayısından başlayıp, argümanda bulunan kelimenin uzunluğundaki aralık boyunca sağa doğru atamalar yapılır.
            matrix[row][i] = wordList[index]                
            index += 1                                      # Atama yapıldığı için, index yani atama yapılacak harfin kelime dizisindeki sıra sayısı 1 artırılır.
    return matrix                                           # Sonuç matrisi return edilir.


# Parametreleri baz alınan matris, satır, sütun değerleri ile atanacak kelime(sentence) olan fonksiyon tanımlandı.
def assign_operations_1(matrix, row, column, sentence):                     # assign_operations_1 fonksiyonu, sağdan sola (RL) operasyonu yapmaktadır.
    row, column = row-1, column-1                                           # Dizi işlemlerinde kolaylık olması için, satır ve sütun değerleri 1 azaltıldı.
    wordList = list(sentence)                                               # Argümandaki kelime, harf atamasının yapılabilmesi dizi haline çevrildi.
    lenght = len(wordList)                                                  # Atanacak harf sayısı hesaplandı.
    columnSize = len(matrix[0])                                             # Matrisdeki sütun büyüklüğü hesaplandı.
    index, flag = 0, 1                                                      # index değişkeni atanmakta olan harfin kelime dizisindeki sırasını belirtmektedir.
    if column < lenght:                                                     # Argümandaki kelime uzunluğunun, uygun sütun sayısından fazla olduğu durumda bu scope'a girilir.
        for i in range(column, -1, -1):                                     # İlk sefer ataması için, argümandaki sütun sayısından başlayıp sütun başına kadar(sola doğru) atamalar yapılır.
            matrix[row][i] = wordList[index]                                
            index += 1                                                      # Atama yapıldığı için, index yani atama yapılacak harfin kelime dizisindeki sıra sayısı 1 artırılır.
        lenght -= index                                                     # Atanacak harf sayısından, atama yapılan toplam harf sayısı çıkarıldı.
        while flag == 1:                                                    # Kelimenin tüm harfleri için atamalar yapılacağı için, kelime bitene kadar flag değeri 1 olarak belirlendi.
            if index != len(wordList):                                      # Atanacak harfin dizideki sırasının, dizi büyüklüğüne eşitliği kontrol edildi.
                if lenght < columnSize:                                     # Atanacak harf sayısının, matrisin sütun büyüklüğü ile karşılaştırılması yapıldı.
                    for i in range(columnSize-1, columnSize-lenght-1, -1):  # Sütun sonundan başlayıp, atanacak harf sayısınca sola doğru atamalar yapılır.
                        matrix[row][i] = wordList[index]                    
                        index += 1                                          # Atama yapıldığı için, index yani atama yapılacak harfin kelime dizisindeki sıra sayısı 1 artırılır.
                else:                                                       # Atanacak harf sayısının, matrisin sütun büyüklüğünden büyük olduğu durumda bu scope'a girilir. 
                    for i in range(columnSize-1, -1, -1):                   # Sütun sonundan başlayıp, matrisdeki sütun sayısınca sola doğru atamalar yapılır.
                        matrix[row][i] = wordList[index]                    
                        index += 1                                          # Atama yapıldığı için, index yani atama yapılacak harfin kelime dizisindeki sıra sayısı 1 artırılır.
                    lenght -= columnSize                                    # Atanacak harf sayısından, atama yapılan toplam harf sayısı (bu durumda sütun sayısı oluyor.) çıkarıldı.
            else:                                                           # Atanacak harfin dizideki sırasının, dizi büyüklüğüne eşit olması durumunda kelimenin tüm harfler atanmış demektir.
                flag = 0                                                    # Kelimenin türm harfleri atandığı için while döngüsünün kırılması adına flag = 0 ataması yapıldı.
    else:                                                                   # Argümandaki kelime uzunluğunun, uygun sütun sayısından az olduğu durumda bu scope'a girilir.
        for i in range(column, column-lenght, -1):                          # Argümandaki sütun sayısından başlayıp, argümanda bulunan kelimenin uzunluğundaki aralık boyunca sola doğru atamalar yapılır.
            matrix[row][i] = wordList[index]                                
            index += 1                                                      # Atama yapıldığı için, index yani atama yapılacak harfin kelime dizisindeki sıra sayısı 1 artırılır.
    return matrix                                                           # Sonuç matrisi return edilir.
    

# Parametreleri baz alınan matris, satır, sütun değerleri ile atanacak kelime(sentence) olan fonksiyon tanımlandı.
def assign_operations_2(matrix, row, column, sentence):                     # assign_operations_2 fonksiyonu, aşağıdan yukarı (DU) operasyonu yapmaktadır.
    row, column = row-1, column-1                                           # Dizi işlemlerinde kolaylık olması için, satır ve sütun değerleri 1 azaltıldı.
    wordList = list(sentence)                                               # Argümandaki kelime, harf atamasının yapılabilmesi dizi haline çevrildi.
    lenght = len(wordList)                                                  # Atanacak harf sayısı hesaplandı.
    rowSize = len(matrix)                                                   # Matrisdeki satır büyüklüğü hesaplandı.
    index, flag = 0, 1                                                      # index değişkeni atanmakta olan harfin kelime dizisindeki sırasını belirtmektedir.
    if row < lenght:                                                        # Argümandaki kelime uzunluğunun, uygun satır sayısından fazla olduğu durumda bu scope'a girilir.
        for i in range(row, -1, -1):                                        # İlk sefer ataması için, argümandaki satır sayısından başlayıp satır başına kadar(yukarı doğru) atamalar yapılır.
            matrix[i][column] = wordList[index]                             
            index += 1                                                      # Atama yapıldığı için, index yani atama yapılacak harfin kelime dizisindeki sıra sayısı 1 artırılır.
        lenght -= index                                                     # Atanacak harf sayısından, atama yapılan toplam harf sayısı çıkarıldı.
        while flag == 1:                                                    # Kelimenin tüm harfleri için atamalar yapılacağı için, kelime bitene kadar flag değeri 1 olarak belirlendi.
            if index != len(wordList):                                      # Atanacak harfin dizideki sırasının, dizi büyüklüğüne eşitliği kontrol edildi.
                if lenght < rowSize:                                        # Atanacak harf sayısının, matrisin satır büyüklüğü ile karşılaştırılması yapıldı.
                    for i in range(rowSize-1, rowSize-lenght-1, -1):        # Satır sonundan başlayıp, atanacak harf sayısınca yukarı doğru atamalar yapılır.
                        matrix[i][column] = wordList[index]
                        index += 1                                          # Atama yapıldığı için, index yani atama yapılacak harfin kelime dizisindeki sıra sayısı 1 artırılır.
                else:                                                       # Atanacak harf sayısının, matrisin satır büyüklüğünden büyük olduğu durumda bu scope'a girilir.  
                    for i in range(rowSize-1, -1, -1):                      # Satır sonundan başlayıp, matrisdeki satır sayısınca yukarı doğru atamalar yapılır.
                        matrix[i][column] = wordList[index]
                        index += 1                                          # Atama yapıldığı için, index yani atama yapılacak harfin kelime dizisindeki sıra sayısı 1 artırılır.
                    lenght -= rowSize                                       # Atanacak harf sayısından, atama yapılan toplam harf sayısı (bu durumda satır sayısı oluyor.) çıkarıldı.
            else:                                                           # Atanacak harfin dizideki sırasının, dizi büyüklüğüne eşit olması durumunda kelimenin tüm harfler atanmış demektir.
                flag = 0                                                    # Kelimenin türm harfleri atandığı için while döngüsünün kırılması adına flag = 0 ataması yapıldı.
    else:                                                                   # Argümandaki kelime uzunluğunun, uygun satır sayısından az olduğu durumda bu scope'a girilir.
        for i in range(row, row-lenght, -1):                                # Argümandaki satır sayısından başlayıp, argümanda bulunan kelimenin uzunluğundaki aralık boyunca yukarı doğru atamalar yapılır.
            matrix[i][column] = wordList[index]
            index += 1                                                      # Atama yapıldığı için, index yani atama yapılacak harfin kelime dizisindeki sıra sayısı 1 artırılır.
    return matrix                                                           # Sonuç matrisi return edilir.


# Parametreleri baz alınan matris, satır, sütun değerleri ile atanacak kelime(sentence) olan fonksiyon tanımlandı.
def assign_operations_3(matrix, row, column, sentence):     # assign_operations_3 fonksiyonu, yukarıdan aşağı (UD) operasyonu yapmaktadır.
    row, column = row-1, column-1                           # Dizi işlemlerinde kolaylık olması için, satır ve sütun değerleri 1 azaltıldı.
    wordList = list(sentence)                               # Argümandaki kelime, harf atamasının yapılabilmesi dizi haline çevrildi.
    lenght = len(wordList)                                  # Atanacak harf sayısı hesaplandı.
    rowSize = len(matrix)                                   # Matrisdeki satır büyüklüğü hesaplandı.
    index, flag = 0, 1                                      # index değişkeni atanmakta olan harfin kelime dizisindeki sırasını belirtmektedir.
    controlsize = rowSize - row                             # controlsize argümandaki satır sayısından sonra gelen, atama yapılabilecek max satır sayısını ifade etmektedir.
    if controlsize < lenght:                                # Argümandaki kelime uzunluğunun, uygun satır sayısından fazla olduğu durumda bu scope'a girilir.
        for i in range(row, rowSize):                       # İlk sefer ataması için, argümandaki satır sayısından başlayıp satır sonuna kadar(aşağı doğru) atamalar yapılır.
            matrix[i][column] = wordList[index]                             
            index += 1                                      # Atama yapıldığı için, index yani atama yapılacak harfin kelime dizisindeki sıra sayısı 1 artırılır.
        lenght -= index                                     # Atanacak harf sayısından, atama yapılan toplam harf sayısı çıkarıldı.
        while flag == 1:                                    # Kelimenin tüm harfleri için atamalar yapılacağı için, kelime bitene kadar flag değeri 1 olarak belirlendi.
            if index != len(wordList):                      # Atanacak harfin dizideki sırasının, dizi büyüklüğüne eşitliği kontrol edildi.
                if lenght < rowSize:                        # Atanacak harf sayısının, matrisin satır büyüklüğü ile karşılaştırılması yapıldı.
                    for i in range(0, lenght):              # Satır başından başlayıp, atanacak harf sayısınca aşağı doğru atamalar yapılır.
                        matrix[i][column] = wordList[index]
                        index += 1                          # Atama yapıldığı için, index yani atama yapılacak harfin kelime dizisindeki sıra sayısı 1 artırılır.
                else:                                       # Atanacak harf sayısının, matrisin satır büyüklüğünden büyük olduğu durumda bu scope'a girilir. 
                    for i in range(0, rowSize):             # Satır başından başlayıp, matrisdeki satır sayısınca aşağı doğru atamalar yapılır.
                        matrix[i][column] = wordList[index]
                        index += 1                          # Atama yapıldığı için, index yani atama yapılacak harfin kelime dizisindeki sıra sayısı 1 artırılır.
                    lenght -= rowSize                       # Atanacak harf sayısından, atama yapılan toplam harf sayısı (bu durumda satır sayısı oluyor.) çıkarıldı.
            else:                                           # Atanacak harfin dizideki sırasının, dizi büyüklüğüne eşit olması durumunda kelimenin tüm harfler atanmış demektir.
                flag = 0                                    # Kelimenin türm harfleri atandığı için while döngüsünün kırılması adına flag = 0 ataması yapıldı.
    else:                                                   # Argümandaki kelime uzunluğunun, uygun satır sayısından az olduğu durumda bu scope'a girilir.
        for i in range(row, row+lenght):                    # Argümandaki satır sayısından başlayıp, argümanda bulunan kelimenin uzunluğundaki aralık boyunca aşağı doğru atamalar yapılır.
            matrix[i][column] = wordList[index]
            index += 1                                      # Atama yapıldığı için, index yani atama yapılacak harfin kelime dizisindeki sıra sayısı 1 artırılır.
    return matrix                                           # Sonuç matrisi return edilir.


# Parametreleri baz alınan satır, sütun değerleri ile atanacak kelime(sentence) ve atama doğrultusu(orientation) olan fonksiyon tanımlandı.
def assignmentWord(row, column, my_word, orientation):                      # assignmentWord fonksiyonu, argümanındaki değerlere göre ilgili operasyonu çağırır.
    operation = direction(orientation).value                                # Operasyon değeri direction class'ı içindeki enum type değişkenlerinden elde edildi.
    if operation == 0:                                                      # Soldan sağa (LR) atama operasyonu saptandığı durumda bu scope'a girilir.
        assign_operations_0(main_matrices, row, column, my_word)            # İlgili operasyonun fonksiyonu çağrılır. Global olarak tanımlanan matris fonksiyona parametre olarak gönderilir.
    elif operation == 1:                                                    # Sağdan sola (RL) atama operasyonu saptandığı durumda bu scope'a girilir.
        assign_operations_1(main_matrices, row, column, my_word)            # İlgili operasyonun fonksiyonu çağrılır. Global olarak tanımlanan matris fonksiyona parametre olarak gönderilir.
    elif operation == 2:                                                    # Aşağıdan yukarı (DU) atama operasyonu saptandığı durumda bu scope'a girilir.
        assign_operations_2(main_matrices, row, column, my_word)            # İlgili operasyonun fonksiyonu çağrılır. Global olarak tanımlanan matris fonksiyona parametre olarak gönderilir.
    elif operation == 3:                                                    # Yukarıdan aşağı (UD) atama operasyonu saptandığı durumda bu scope'a girilir.
        assign_operations_3(main_matrices, row, column, my_word)            # İlgili operasyonun fonksiyonu çağrılır. Global olarak tanımlanan matris fonksiyona parametre olarak gönderilir.
    else:                                                                   # Hatalı operasyon değeri saptandığı durumda bu scope'a girilir.
        print ("Incorrect Orientation Value!")                              # Hata mesajı ekrana yazdırıldı.


# Parametresi string olan bir fonksiyon tanımlandı.
def isPalindrome(string_num):                                               # isPalindrome fonksiyonu, argümanındaki kelimenin palindromluğunu kontrol eder.
    if string_num == string_num[::-1]:                                      
        return True                                                         # Argümanındaki kelimeni palindrom ise True değer döndürür.
    return False                                                            # Argümanındaki kelimeni palindrom ise False değer döndürür.


# Parametresi matris olan bir fonksiyon tanımlandı.
def plndrm_operations_0(matrix):                                            # plndrm_operations_0 fonksiyonu, argümanındaki matrix'in içinde soldan sağa doğru palindrom kelimeleri yazdırır.
    rowSize, colSize = len(matrix), len(matrix[0])                          # Argümandaki matrisin satır ve sütun sayıları belirlendi.
    pword = 10                                                              # Palindrom büyüklüğü en az 10 olacak şekilde belirlendi.
    pwords = []                                                             # Palindrom kelimeleri atayacağımız liste oluşturuldu.
    while(pword <= colSize):                                                # Sütunda sağa doğru, en az pword kadar uygun sütun mevcut olduğunda aramalar yapılır.
        for i in range(0, rowSize):                                         # Satır sınır değeri rowSize olarak belirlendi.
            for j in range(0, colSize-pword+1):                             # Sütun sınır değerinin colSize-pword+1 olması, iç döngüde pword kadar sağa gitmesinden kaynaklanmaktadır.
                word = ""                                                   # Geçici kelime oluşturuldu.
                for k in range(0, pword):                                   # Word'e atanacak harflerin sınır değeri pword olarak belirlendi. 
                    word += matrix[i][j+k]                                  
                if isPalindrome(word):                                      # Elde edilen kelime isPalindrome fonksiyonuna gönderildi.
                    pwords.append(word)                                     # Kelimenin palindrom olduğu durumlarda, palindrom listesine eklenmesi gerçekleştirildi.
        pword += 1                                                          # Kelime uzunluğu 1 karakter artırılır.
    print("Soldan Sağa Palindromlar: ")                                     
    print(pwords)                                                           # Arama sonucu bulunan palindrom kelimeler ekrana yazdırılır.


# Parametresi matris olan bir fonksiyon tanımlandı.
def plndrm_operations_1(matrix):                                            # plndrm_operations_1 fonksiyonu, argümanındaki matrix'in içinde sağdan sola doğru palindrom kelimeleri yazdırır.
    rowSize, colSize = len(matrix), len(matrix[0])                          # Argümandaki matrisin satır ve sütun sayıları belirlendi.
    pword = 10                                                              # Palindrom büyüklüğü en az 10 olacak şekilde belirlendi.
    pwords = []                                                             # Palindrom kelimeleri atayacağımız liste oluşturuldu.
    while(pword <= colSize):                                                # Sütunda sola doğru, en az pword kadar uygun sütun mevcut olduğunda aramalar yapılır.
        for i in range(0, rowSize):                                         # Satır sınır değeri rowSize olarak belirlendi.
            j = colSize-1                                                   # j'ye matrisin sütun sayısı atandı. (-1 olması sütun dizisinin ilk elemanının 0'dan başlamasındandır.)
            while(j >= pword-1):                                            # Sütunda sola doğru, en az pword kadar uygun sütun mevcut olduğunda aramalar yapılır.
                word = ""                                                   # Geçici kelime oluşturuldu.
                k = 0                                                       # k değerine 0 atandı.
                while(k > 0-pword):                                         # Word'e atanacak harflerin sınır değeri pword olarak belirlendi.(k değeri 0'dan başlayıp -pword değerine eşit olana kadar atama yapılıyor.)
                    word += matrix[i][j+k]                                  
                    k -= 1                                                  # k değeri 1 azaltıldı. 
                if isPalindrome(word):                                      # Elde edilen kelime isPalindrome fonksiyonuna gönderildi.
                    pwords.append(word)                                     # Kelimenin palindrom olduğu durumlarda, palindrom listesine eklenmesi gerçekleştirildi.
                j -= 1                                                      # j değeri 1 azaltıldı.
        pword += 1                                                          # Kelime uzunluğu 1 karakter artırılır.
    print("Sağdan Sola Palindromlar: ")                                     
    print(pwords)                                                           # Arama sonucu bulunan palindrom kelimeler ekrana yazdırılır.


# Parametresi matris olan bir fonksiyon tanımlandı.
def plndrm_operations_2(matrix):                                            # plndrm_operations_2 fonksiyonu, argümanındaki matrix'in içinde aşağıdan yukarı doğru palindrom kelimeleri yazdırır.
    rowSize, colSize = len(matrix), len(matrix[0])                          # Argümandaki matrisin satır ve sütun sayıları belirlendi.
    pword = 10                                                              # Palindrom büyüklüğü en az 10 olacak şekilde belirlendi.
    pwords = []                                                             # Palindrom kelimeleri atayacağımız liste oluşturuldu.
    while(pword <= rowSize):                                                # Satırda yukarı doğru, en az pword kadar uygun satır mevcut olduğunda aramalar yapılır.
        for i in range(0, colSize):                                         # Sütun sınır değeri rowSize olarak belirlendi.
            j = rowSize-1                                                   # j'ye matrisin satır sayısı atandı. (-1 olması satır dizisinin ilk elemanının 0'dan başlamasındandır.)
            while(j >= pword-1):                                            # Satırda yukarı doğru, en az pword kadar uygun satır mevcut olduğunda aramalar yapılır.
                word = ""                                                   # Geçici kelime oluşturuldu.
                k = 0                                                       # k değerine 0 atandı.
                while(k > 0-pword):                                         # Word'e atanacak harflerin sınır değeri pword olarak belirlendi.(k değeri 0'dan başlayıp -pword değerine eşit olana kadar atama yapılıyor.)
                    word += matrix[j+k][i]                                  
                    k -= 1                                                  # k değeri 1 azaltıldı.
                if isPalindrome(word):                                      # Elde edilen kelime isPalindrome fonksiyonuna gönderildi.
                    pwords.append(word)                                     # Kelimenin palindrom olduğu durumlarda, palindrom listesine eklenmesi gerçekleştirildi.
                j -= 1                                                      # j değeri 1 azaltıldı.
        pword += 1                                                          # Kelime uzunluğu 1 karakter artırılır.
    print("Aşağıdan Yukarı Palindromlar: ")                                 
    print(pwords)                                                           # Arama sonucu bulunan palindrom kelimeler ekrana yazdırılır.


# Parametresi matris olan bir fonksiyon tanımlandı.
def plndrm_operations_3(matrix):                                            # plndrm_operations_3 fonksiyonu, argümanındaki matrix'in içinde yukarıdan aşağıya doğru palindrom kelimeleri yazdırır.
    rowSize, colSize = len(matrix), len(matrix[0])                          # Argümandaki matrisin satır ve sütun sayıları belirlendi.
    pword = 10                                                              # Palindrom büyüklüğü en az 10 olacak şekilde belirlendi.
    pwords = []                                                             # Palindrom kelimeleri atayacağımız liste oluşturuldu.
    while(pword <= rowSize):                                                # Satırda aşağıya doğru, en az pword kadar uygun satır mevcut olduğunda aramalar yapılır.
        for i in range(0, colSize):                                         # Sütun sınır değeri rowSize olarak belirlendi.
            for j in range(0, rowSize-pword+1):                             # Satır sınır değerinin rowSize-pword+1 olması, iç döngüde pword kadar aşağı gitmesinden kaynaklanmaktadır.
                word = ""                                                   # Geçici kelime oluşturuldu.
                for k in range(0, pword):                                   # Word'e atanacak harflerin sınır değeri pword olarak belirlendi. 
                    word += matrix[j+k][i]                                  
                if isPalindrome(word):                                      # Elde edilen kelime isPalindrome fonksiyonuna gönderildi.
                    pwords.append(word)                                     # Kelimenin palindrom olduğu durumlarda, palindrom listesine eklenmesi gerçekleştirildi.
        pword += 1                                                          # Kelime uzunluğu 1 karakter artırılır.
    print("Yukarıdan Aşağı Palindromlar: ")                                 
    print(pwords)                                                           # Arama sonucu bulunan palindrom kelimeler ekrana yazdırılır.


# Parametresi matris olan bir fonksiyon tanımlandı.
def GetPalindromes(matrix):                                 # GetPalindromes fonksiyonu, argümandaki matrisinde palindrom kelimeleri arar ve ekrana yazdırır.
    plndrm_operations_0(matrix)                             # Soldan sağa doğru palindrom kelime araması yapan fonksiyon çağırılır.
    plndrm_operations_1(matrix)                             # Sağdan sola doğru palindrom kelime araması yapan fonksiyon çağırılır.
    plndrm_operations_2(matrix)                             # Aşağıdan yukarıya doğru palindrom kelime araması yapan fonksiyon çağırılır.
    plndrm_operations_3(matrix)                             # Yukarıdan aşağıya doğru palindrom kelime araması yapan fonksiyon çağırılır.


# Parametresi matris olan bir fonksiyon tanımlandı.
def GetMatrix(matrix):                                      # GetMatrix fonksiyonu, argümanındaki matrisi, satırları alt alta gelecek şekilde ekrana yazdırır.
    row = len(matrix)                                       # Argümandaki matrisin satır sayısını bulunur.
    for i in range(0, row):                                 # Matrisin artan sayıdaki satırları ayrı ayrı line'larda ekrana yazılır.
        print(matrix[i])                                    


# Parametresi olmayan bir fonksiyon tanımlandı. Bu fonksiyon ödev sorularındaki görevleri gerçeklemektedir.
def Test():                                                 # Soru 4 gerçeklendi.
    global main_matrices                                    # 1. soruda üretilen matrisin 2. soruda da kullanılması için, matris global olarak oluşturuldu.
    main_matrices = createRandMatrix(5, 6)                  # Soru 1 gerçeklendi.

    assignmentWord(1, 1, "PIECES", 0)                       # Soru 2 - Soldan sağa doğru yapılan atama operasyonları gerçeklendi.
    GetMatrix(main_matrices)                                # Operasyon sonucu hakkında bilgi verilmesi için, üzerinde işlem yapılan matris ekrana basıldı.
    print("-----------")
    assignmentWord(2, 2, "QWERTY", 1)                       # Soru 2 - Sağdan sola doğru yapılan atama operasyonları gerçeklendi.
    GetMatrix(main_matrices)                                # Operasyon sonucu hakkında bilgi verilmesi için, üzerinde işlem yapılan matris ekrana basıldı.
    print("-----------")
    assignmentWord(3, 3, "KLMNPR", 2)                       # Soru 2 -  Aşağıdan yukarıya doğru yapılan atama operasyonları gerçeklendi.
    GetMatrix(main_matrices)                                # Operasyon sonucu hakkında bilgi verilmesi için, üzerinde işlem yapılan matris ekrana basıldı.
    print("-----------")
    assignmentWord(4, 4, "ASDFGH", 3)                       # Soru 2 -  Yukarıdan aşağıya doğru yapılan atama operasyonları gerçeklendi.
    GetMatrix(main_matrices)                                # Operasyon sonucu hakkında bilgi verilmesi için, üzerinde işlem yapılan matris ekrana basıldı.
    print("-----------")

    base_matrices = createRandMatrix(25, 21)                                # Soru 3 için  bir matris oluşturuldu.
    assign_operations_0(base_matrices, 1, 3, "AKAKAKAKAKA")                 # Soru 3 için, soldan sağa doğru 11 harfli palindrom kelime ataması yapıldı.
    GetMatrix(base_matrices)                                                # Atama sonrası işlem yapılan matris ekrana yazdırıldı.
    print("-----------")
    assign_operations_1(base_matrices, 2, 16, "NANANANANAN")                # Soru 3 için, sağdan sola doğru 11 harfli palindrom kelime ataması yapıldı.
    GetMatrix(base_matrices)                                                # Atama sonrası işlem yapılan matris ekrana yazdırıldı.
    print("-----------")
    assign_operations_2(base_matrices, 13, 3, "XDEFEDEFEDX")                # Soru 3 için, aşağıdan yukarıya doğru 11 harfli palindrom kelime ataması yapıldı.
    GetMatrix(base_matrices)                                                # Atama sonrası işlem yapılan matris ekrana yazdırıldı.
    print("-----------")
    assign_operations_3(base_matrices, 4, 5, "MSDSAFASDSM")                 # Soru 3 için, yukarıdan aşağıya 11 harfli palindrom kelime ataması yapıldı.
    GetMatrix(base_matrices)                                                # Atama sonrası işlem yapılan matris ekrana yazdırıldı.
    print("-----------")

    GetPalindromes(base_matrices)                                           # Soru 3 gerçeklendi.


Test()                                                                      # Test fonksiyonu başlatıldı.



