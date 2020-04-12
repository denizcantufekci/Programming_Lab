# added contents

"""
Rastgele Değişken(Random Variable): 
        Değeri bir deney sonucu ile belirlenen, izini sürebilmemize olanak sağlayan değişken türüdür.
Kesikli Rastgele Değişken(Discrete Random Variable): 
        Rastgele değişkenin alabileceği değerlerin sonlu veya sayılabilir olması durumudur. 
        (Müsabakalardaki skor sayısı / Zar atma gibi durumlar)
Sürekli Rastgele Değişken(Continuous Random Variable): 
        Rastgele değişkenin alabileceği değerlerin sonsuz veya sayılamaz olması durumudur. 
        (Zaman / Yükseklik / Ağırlık gibi kestirelemeyen durumlar)
Kesikli ve Sürekli Değişkenlerin farkına bir örnek:
        Bir hisse senedi fiyatı, kesikli bir değişken olarak alınırsa ondalık sayının ötesine yalnızca iki ondalık basamağa (ör. 42.59) 
        kadar giderken, sürekli bir değişken olarak alınırsa ondalık sayının sonsuz sayıda değeri olabilir. (örn. 42.5972608914…)
Olasılık Dağılımı(Probability Distribution): 
        Bir rastgele değişkenin alabileceği değerlerin, o değerlere karşılık gelen olasılık değerleri ile belirtilmesidir.
Kesikli Olasılık Dağılımı(Discrete Probability Distribution): 
        Kesikli rastgele değişkenler ile elde edilen olasılık dağılımı türüdür.
Sürekli Olasılık Dağılımı(Continuous Probability Distribution): 
        Sürekli rastgele değişkenler ile elde edilen olasılık dağılımı türüdür.
Olasılık Yoğunluk Fonksiyonu(Probability Density Function):
        Sürekli rastgele değişkenlerin varlığı durumunda tanımlanan bir olasılık dağılım fonksiyondur.
Olasılık Kütle Fonksiyonu(Probability Mass Function):
        Ayrık/Kesikli rastgele değişkenlerin olasılığının belli bir değere eşit olması durumunda tanımlanan bir fonksiyondur.
Birikimli/Yığmalı Dağılım Fonksiyonu (Cumulative Distribution Function) / Dağılım Fonksiyonu (Distribution Function):
        Reel değerli bir X değişkeninin x sayısından küçük veya ona eşit bir değer alma olasılığını açıklayan fonksiyondur.
        X değişkeninin olasılık dağılımını tümüyle tanımlar. Yalnız "dağılım fonksiyonu" da denmektedir.
  Ayrıntılı Açıklama:
        Rastgele değişkenin belirli bir değer aldığı bir olayın olasılığını tanımlanırken, bu olayın olasılığı genellikle sıfır olur.
        Çünkü herhangi bir sürekli aralıkta sonsuz sayıda farklı değer vardır. 
        Olasılığı her yerde sıfır değerine sahip olarak tanımlamak çok yararlı bir durum olmadığı için,
        rastgele değişkenin belirli bir aralık içinde bir değer aldığı olayların olasılığını tanımlanır. 
        Bunu yaparken genelde, rastgele değişkenin belirli bir x değerine eşit veya x değerinden daha küçük bir değer alma olasılığı 
        olarak tanımlanan kümülatif/birikimli/yığmalı dağılım fonksiyonu kullanılır.

Tekdüze Dağılım(Uniform Distribution):
        Rastgele değişkenler için olası değerlerin(olayların) gerçekleşme olasılıklarının eşit olması durumunda 
        oluşan olasılık dağılımıdır. Kesikli dağılım gösterebildiği gibi sürekli dağılım da gösterebilir. 
        Sürekli dağılım gösterdiği duruma şeklinden dolayı dikdörtgen dağılım(rectangular distribution) da denmektedir.

Sürekli Tekdüze Dağılım Bazında Oluşturulan Soru: 
        ÇOMÜ'de bulunan ÖSEM binasında öğle yemeklerinin 11:30–13:30 saatleri arasında verildiği bilindiğine göre,
        üniversitede bulunan bir öğrencinin 12:30'dan sonra öğle yemeğini alma olasılığı kaçtır?
Kesikli Tekdüze Dağılım Bazında Oluşturulan Soru: 
        ÇOMÜ öğrenci işleri başkanlığı, bünyesinde bulunan 9999 aktif öğrenci arasından kura ile çekeceği bir kişiye tam bir 
        senelik burs imkanı sağlayacaktır. Bu talihli kişinin öğrenci numarasının son hanesinin 4'den küçük olma olasılığı kaçtır?
"""
