from sympy import FiniteSet
from fractions import Fraction

def my_histogram(inlist = [5, 0, 25, 100, 0, 0, 5, 100, 5]):    # This function returns a dictionary.
    my_dct = {}
        # dict() - An empty hash(dictionary) has been created. - built-in: we created without import.
        # dict() - Boş bir hash(sözlük) oluşturuldu. - built-in: import yapılmadan oluşturduk.
    for i in inlist:
        if i in my_dct:
            my_dct[i] += 1
            # If the list in hash has an index i, it increases the value of the current key by 1.
            # Hash içindeki listenin i indisi varsa, o andaki key'in value değerini 1 artırır.
        else:
            my_dct[i] = 1
            # If the list in hash doesn't have an index i, assign 1 to the current key.
            # Hash içindeki listenin i indisi yoksa, o andaki key'e 1 ataması yap.
    return my_dct

def lookup(dict, value):
    # This Lookup function returns the first number that repeats value times in the dictionary.
    # Bu Lookup fonksiyonu, sözlük içinde value kere tekrar eden ilk sayıyı döndürür.
    try:
        for k in dict:
            if dict[k] == value:
                return k
    except:
        print("Value not found")

# exlist = [2,3,4,5,2,1,4,3,5,5]
# print(lookup(my_histogram(exlist), 2))

known = {0:0, 1:1}
def fibo_rec(n): # This function finds the fibonacci number using known dictionary.
    """
    Ordinary way with recursive function - Özyineli fonksiyon ile sıradan yol
    if n < 2:
        return n
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)
    """
    if n in known:
        return known[n]
    else:
        result = fibo_rec(n-1) + fibo_rec(n-2)
        known[n] = result
        return result
        
"""
    FiniteSet(0, 1, 3, Fraction(1,5)) = {0, 1, 1/5, 3}

    The finiteSet method allows us to create a finite set.
    The fraction method allows us to get a fractional number.

    FiniteSet metodu sonlu küme oluşturmamıza yarıyor.
    Fraction metodu ise kesirli sayı almamızı sağlıyor.
"""
s = FiniteSet(1, 1.5, Fraction(1, 5), 1, 1.5, 7, 42)
t = FiniteSet(Fraction(1,5), 1, 5, 1, 1, 91, 87) 

for member in s: # Print s set.
    print(member)
    
if s == t:
    print("True")
else:
    print("False")

# print(s.union(t)) # It takes the combination of two sets. means SuT
# print(s.intersect(t)) # It takes the intersection of two sets. means SnT
# print(set(s ** 2)) 
"""
The expression "s ** 2" refers to the cartesian product. means SxS
Using this expression in set(), we can see the elements of cartesian products one by one.

"s ** 2" ifadesi, kartezyen bir çarpımı belirtir. SxS anlamına gelir
Bu ifadeyi set() içinde kullanarak, kartezyen çarpımların elemanlarını teker teker görebiliriz.
"""
