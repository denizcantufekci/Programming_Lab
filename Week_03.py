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

def fibonacci_ord(n): # This function finds the fibonacci number in the ordinary way, without recursion.
    fib1, fib2 = 0, 1 # 0 is the zeroth fibonacci number and 1 is the first fibonacci number.
    for i in range(n-1):
        fib = fib1 + fib2
        fib1, fib2 = fib2, fib
    return fib # It returns nth fibonacci number.

"""
    FiniteSet(0, 1, 3, Fraction(1,5)) = {0, 1, 1/5, 3}

    The finiteSet method allows us to create a finite set.
    The fraction method allows us to get a fractional number.

    FiniteSet metodu sonlu küme oluşturmamıza yarıyor.
    Fraction metodu ise kesirli sayı almamızı sağlıyor.
"""
s = FiniteSet(1, 1.5, Fraction(1, 5), 1, 1.5, 7, 42)
t = FiniteSet(Fraction(1,5), 1, 5, 1, 1, 91, 87)
v = FiniteSet() # An empty set is created.

members = [1, 3, 4, 5]
w = FiniteSet(*members) # A set was created with the elements of the "members" list.

for member in s: # Print s set.
    print(member)

if s == t:
    print("True")
else:
    print("False")

# print(s.union(t)) # It takes the combination of two sets. means SuT
# print(s.intersect(t)) # It takes the intersection of two sets. means SnT
# print(set(s ** t))
"""
The expression "s ** t" refers to the cartesian product. means SxT
Using this expression in set(), we can see the elements of cartesian products one by one.

"s ** t" ifadesi, kartezyen bir çarpımı belirtir. SxT anlamına gelir
Bu ifadeyi set() içinde kullanarak, kartezyen çarpımların elemanlarını teker teker görebiliriz.
"""

"""
We draw the numbers from 1 to 21 out of the bag. We calculate the probability that the number drawn from the bag is the prime number.
1'den 21'e kadar olan sayıların torbadan çekilişini yapıyoruz. Torbadan çekilen sayının asal sayı olma olasılığını hesaplıyoruz.
"""
from sympy import FiniteSet
from fractions import Fraction

t = FiniteSet(1,2,3)
s = FiniteSet(2,4,6)

if t == s:
    print("True")
else:
    print("False")

# print(t.union(s))
# print(t.intersect(s))
# print(t**2)

def probability (space, event):
    return len(event) / len(space)
    # space refers to the sample space. event indicates a particular event.
    # space, örneklem uzayını belirtir. event ise belirli bir olayı belirtir.

def check_prime(number):
    if number != 1:
        for factor in range(2, number):
            if number % factor == 0:
                return False
    else:
        return False
    return True

space = FiniteSet(* range(1, 21))
# With the operator *, all the values in the range in the range are transferred to the set as elements.
# * operatörü ile range içindeki aralıkta bulunan tüm değerler kümeye eleman olarak aktarılır.

primes = []
for num in space:
    if check_prime(num):
        primes.append(num)
# We determine the primes in our sample space and assign them to primes array.
# Örnek uzayımızdaki asalları belirler ve primes dizisine atarız.

event = FiniteSet(* primes)
p = probability(space, event)

print("Sample space: ", space)  # Örneklem uzayı
print("Event: ", event)         # Belirli bir olay / Gelen sayının asal olma durumu
print('Probability of event: {0:.3f}'.format(p))  # Olayın gerçekleşme olasılığı
