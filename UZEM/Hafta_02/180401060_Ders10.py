from sympy import Symbol
from sympy import factor, expand
from sympy import pprint

x = Symbol('x')
y = Symbol('y')
# Symbol() methodu argüman olarak girilen ifadeyi sembol olarak tanımlar.

k = 15 
k =  2 * (k + k) + 30
# print(x) """Output: 90 """

x = x + x + 1
# print(x) """Output: 2*x + 1 """

p = x * (x + x)
# print(p) """Output: 2*x**2 """

p = (x + 2)*(x + 3)
# print(p) """Output: (x + 2)*(x + 3) """

expr = x**2 - y**2
factors = factor(expr) 
# factor() methodu argüman olarak girilen ifadeyi çarpanlarına ayrılmış şekilde tanımlar.
# print(factors) """Output: (x - y)*(x + y) """

expands = expand(factors) 
# expand() methodu argümanına çarpanlarına ayrılmış ifade yazılırsa, o ifadenin çarpanlarına ayrılmadan önceki halini tanımlar.
# print(expands) """Output: x**2 - y**2 """

expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3
# print(expr) """Output: x**3 + 3*x**2*y + 3*x*y**2 + y**3 """
factors = factor(expr)
# print(factors) """Output: (x + y)**3 """
# pprint(factors) """Output: Görselleştirilmiş Çıktı """

series = x
n = 5
for i in range(2, n+1):
    series = series + (x**i)/i
# print(series) """Output: x**5/5 + x**4/4 + x**3/3 + x**2/2 + x """
# pprint(series) """Output: Görselleştirilmiş Çıktı """

expr = x*x + x*y + x*y + y*y
res = expr.subs({x:1,y:2}) # x yerine 1, y yerine 2 değeri yazılır.
# print(res) """Output: 9 """
res2 = expr.subs({x:1-y}) # x yerine (1 - y) ifadesi yazılır.
# print(res2) """Output: y**2 + 2*y*(1 - y) + (1 - y)**2 """

x = Symbol('x') 
series = x
n = 5
x_value = 10
for i in range(2, n+1):
    series = series + (x**i)/i
# pprint(series) """Output: Görselleştirilmiş Çıktı """
series_value = series.subs({x:x_value})
# print(series_value) """Output: 10085/12 """
