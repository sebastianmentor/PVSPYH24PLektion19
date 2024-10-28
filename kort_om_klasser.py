import random

class MinKlass:
    def __init__(self, värde1, värde2):
        self.värde1 = värde1
        self._värde2 = värde2 # säga att _värde2 är ett hemligt värde
        self.standard_attribut = True
        self._internt_hemligt_från_start = 'Bananer'

    def kan_göra_saker(self):
        print(f'Instansen av MinKlass {id(self)} kan nu göra den här saken!')

min_klass = MinKlass(12, 'Hemligt tal 42')
print(id(min_klass))
print(id(MinKlass))
print(min_klass.värde1)
print(min_klass._värde2)

min_klass._värde2 = 'Ny hemlighet' # Fy fy fy du får inte göra såhär!

min_klass.värde1 = 206 # Helt okej!!

if min_klass.standard_attribut:
    print('Standard är bra')

min_klass.kan_göra_saker()
print(id(MinKlass))

class A:
    def __init__(self):
        self._a = [random.randint(1,10), random.randint(1,10), random.randint(1,10)]

    def print_a_times_10(self):
        print(self._a*10)        

    def get_a(self):
        return self._a.copy()

a1, a2, a3, a4 = A(),A(),A(),A()

massa_a = [a1,a2,a3,a4]

for a in massa_a:
    print(f"{id(a)=}")
    print(a.get_a())
    # a.print_a_times_10()

print(a1.get_a())
a1.get_a().append(42)
print(a1.get_a())


class B:
    def __init__(self, c):
        self.c = c

    def print_c_value(self):
        self.c.print_val()
    
class C:
    def __init__(self, val):
        self._val = val
    
    def print_val(self):
        print(self._val)


c = C('hejsa')
b = B(c)
b.print_c_value()