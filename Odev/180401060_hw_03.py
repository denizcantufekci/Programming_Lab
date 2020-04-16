from sympy import Symbol, pprint, Piecewise
import sympy as sym
import sympy.plotting as syp
import matplotlib.pyplot as plt
import math
%matplotlib inline

a = Symbol('a')
b = Symbol('b')
x = Symbol('x')
f = 1 / abs(a-b)

def uniform_dist_syp(lower, upper):
    if lower > upper:
        lower, upper = upper, lower
    syp.plot(Piecewise((0, (x < lower) | (x > upper)), (f.subs({a: lower, b: upper}), (x >= lower) & 
        (x <= upper))), (x, -10, 10), title="uniform_distribution_sympy")
    
def uniform_dist_plt(lower, upper):
    if lower > upper:
        lower, upper = upper, lower
    x_value=[]
    y_value=[]
    function = Piecewise((0, (x < lower) | (x > upper)), (f.subs({a:lower, b:upper}), (x >= lower) & (x <= upper)))
    value = float(0)
    while value < 10.0:
        y=function.subs({x:value}).evalf()
        y_value.append(y)
        x_value.append(value)
        plt.title('uniform_distribution_matplotlib')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.plot(x_value,y_value)
        value += 0.01
        
pprint(f)
uniform_dist_syp(3,9)
uniform_dist_plt(3, 9)

"""       
Uniform Distribution / Tekdüze Dağılım = Olasılık uzayındaki olayların herbirinin gerçekleşme 
    olasılıklarının eşit olduğu, yani tüm olasılıkların tekdüze dağılım gösterdiği bir olasılık dağılımı türüdür.

Bu dağılım için olasılık yoğunluk fonksiyonu(probability density function) şu şekilde ifade edilir:

            |1 / (b - a)   ,  a <= x <= b
    f(x)=   |
            |     0        ,  x < a veya x > 

Piecewise methodu ile koşullu fonksiyonumuzu oluşturuyoruz.
syp.plot içinde fonksiyonu hazır olarak çizidiriyoruz.
plt.plot içinde ise fonksiyondaki x değerlerine karşılık gelen f(x)=y değerlerini buluyor 
    ve bu veriler baz alınarak fonksiyon çizimi yapıyoruz.
    Burada grafiği idealine daha yakın/benzer yapmak için x'in artış değerlerini olabildiğince küçülttük.
"""
