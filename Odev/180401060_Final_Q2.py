import random

# Parametre olarak oluşturulacak vektörün eleman sayısını(elementSize) alan fonksiyon tanımlandı.
def createRandList(elementSize):        # createRandList fonksiyonu, elementSize büyüklüğünde random bir vektör oluşturur.
    integerList = []                    # Vektör elemanlarının tutulacağı eleman listesi oluşturuldu.
    for times in range(elementSize):
        element = random.randint(0,10)  # 0-10 aralığındaki sayılardan rastgele bir rakam seçildi ve element'e atandı.
        integerList.append(element)     # Element değeri eleman listesine eklendi.
    return integerList                  # Vektörü oluşturan liste return edildi.


# Parametre olarak skaler çarpım yapılacak iki vektörü alan bir fonksiyon tanımlandı.
def vectorDotProduct(x, y):             # vectorDotProduct fonksiyonu, argümanındaki vektörlerin skaler çarpımını bulur.
    size = len(x)                       # İlk vektörün uzunluğu size değişkenine atandı.
    resultList = []                     # Sonuç listesi oluşturuldu.
    for i in range(size):               # Sonuç listesine, argümadaki x ve y vektörünün aynı değerlerindeki elemanların çarpımı eklendi.
        resultList.append(x[i]*y[i])    
    sum = 0                             # Toplam değişkeni oluşturuldu.
    for i in range(len(resultList)):    # Sonuç listesindeki elemanlar toplandı.
        sum = sum+resultList[i]         
    return sum                          # Sonuç listesindeki elemanların toplamı, yani skaler çarpım sonucu return edildi.


# Parametre olarak iki vektör alan bir fonksiyon tanımlandı.
def vectorAddProduct(x, y):             # vectorAddProduct fonksiyonu, argümanındaki vektörlerin toplamını bulur.
    size = len(x)                       
    resultList = []                     # Sonuç listesi oluşturuldu.
    for i in range(size):
        resultList.append(x[i]+y[i])    # Aynı indisteki elemanlar toplanarak sonuç listesine eklendi.
    return resultList                   # Sonuç listesi return edildi.
    

# Parametre olarak satır ve sütun sayısı alan bir fonksiyon tanımlandı.
def createMatrices(rows, columns):                                          # createMatrices fonksiyonu, argümanındaki mXn değerlerindeki matrisi oluşturur.
    sumproduct = vectorAddProduct(v1, v2)
    intMatrix = []                                                          # Matris ana bloğu oluşturuldu.
    for row in range(rows):               
        for col in range(columns): 
            tempRow = [i*(val-row) for i in sumproduct]                     # Bir tane iç blok oluşturuldu. 
        intMatrix.append(tempRow)                                           # Oluşturulan iç blok, ana bloğa eklendi.
    return intMatrix                                                        # Sonuç matrisi return edildi.
"""
createMatrices fonksiyonu açıklama:
- 1. soruda üretilen v1 ve v2 vektörleri global olarak alınarak toplam vektörü hesaplandı.
- 2. soruda üretilen v1 ve v2 vektörlerinin skaler çarpım sonucu global olarak alınarak belirlendi.
- Matrisin her satırındaki elemanlar ( skaler_çarpım - row(her adımda artan değer) ) * ( toplam vektörü ) yöntemine göre atandı.
Böylece 1. ve 2. soruları kullanarak, MxN parametrelerini alan bir fonksiyon gerçeklendi.
"""


# Parametre olarak iki tane matris alan bir fonksiyon tanımlandı.
def Multiplication_Matrices(x, y):                                          # createMatrices fonksiyonu, argümanındaki matrislerin çarpımını bulur.
    rows_x, cols_x = len(x), len(x[0])                                      # Argümandaki ilk matrisin satır ve sütun sayısı belirlendi.
    rows_y, cols_y = len(y), len(y[0])                                      # Argümandaki ikinci matrisin satır ve sütun sayısı belirlendi.
    if cols_x != rows_y:                                                    # Matris çarpımı için gerekli koşul kontrol edildi.
        print("Verilen iki matris çarpılamaz!")                             # Matris çarpımı yapılamadığında verilen hata mesajı ekrana yazdırıldı.
        return                                                              # Matris çarpımı yapılamadığı durumda fonksiyon herhangi bir değer return etmemektedir.
    multMatrix = [[0 for row in range(rows_x)] for col in range(cols_y)]    # Tüm elemanları 0 olan, matris çarpımının atanacağı sonuç matrisi oluşturuldu.
    for i in range(rows_x): 
        for j in range(cols_y):
            for k in range(cols_x):
                multMatrix[i][j] += x[i][k]*y[k][j]                         # Argümandaki matrislerin uygun indisleri belirlenerek çarpım yapıldı ve sonuç matrisine atandı.
    return multMatrix                                                       # Sonuç matrisi return edildi.
"""
Multiplication_Matrices fonksiyonu açıklama:
- 3. soru olan createMatrices fonksiyonu ile elde edilen iki ayrı matris bu fonksiyonda çarpıldı.
Böylece 1.-2.-3. sorular kullanılarak oluşturulan iki ayrı matrisi, parametre olarak alan bir fonksiyon gerçeklendi.
"""


def GetMatrix(matrix):
    row = len(matrix)
    for i in range(0, row):
        print(matrix[i])


# Parametresi olmayan bir fonksiyon tanımlandı. Bu fonksiyon ödev sorularındaki görevleri gerçeklemektedir.
def Test():                                                                 # Soru 5 gerçeklendi.
    global v1, v2, val                                                      # Diğer sorularsa kullanılabilmesi için global olarak değişken tanımlandı.           
    vectorSize, controlsize = 2, 3

    v1 = createRandList(vectorSize)                                         # Soru 1 gerçeklendi.
    v2 = createRandList(vectorSize)                                         # Soru 1 gerçeklendi.
    val = vectorDotProduct(v1, v2)                                          # Soru 2 gerçeklendi.
    m1 = createMatrices(controlsize, vectorSize)                            # Soru 3 gerçeklendi.
    print("Birinci vektör: ", v1)
    print("İkinci vektör: ", v2)
    print("Vektörlerin skaler çarpımları: ", val)
    print("İki vektör ve skaler çarpımları ile elde edilen matris:")
    GetMatrix(m1)
    print("----------")

    v1 = createRandList(controlsize)                                        # Soru 1 gerçeklendi.
    v2 = createRandList(controlsize)                                        # Soru 1 gerçeklendi.
    val = vectorDotProduct(v1, v2)                                          # Soru 2 gerçeklendi.
    m2 = createMatrices(vectorSize, controlsize)                            # Soru 3 gerçeklendi.
    print("Birinci vektör: ", v1)
    print("İkinci vektör: ", v2)
    print("Vektörlerin skaler çarpımları: ", val)
    print("İki vektör ve skaler çarpımları ile elde edilen matris:")
    GetMatrix(m2)
    print("----------")

    resultMatrix = Multiplication_Matrices(m1, m2)                          # Soru 4 gerçeklendi.
    print("İki matrisin çarpımı ile elde edilen matris:")
    GetMatrix(resultMatrix)                                                 
"""
Test fonksiyonu açıklama:
- 1. soruda üretilen vektörlerin ve 2. soruda üretilen skaler çarpım sonucunun diğer sorularda da kullanılması için global tanımlaması yapıldı.
- Çarpım matrisi elde edebilmek için vectorSize ile controlsize değişkenleri ayrı ayrı gerçeklendi.
"""

Test()                                                                      # Test fonksiyonu başlatıldı.
