# loopar osv 
# Dvs upprepa saker osv

for item in [1,2,3,4,5]:
    if item % 2 == 0:
        print(item)

min_lista = ['a', 'b', 'c', 'd']

längden_på_listan = len(min_lista)
index = 0
while längden_på_listan > 0:
    print(min_lista[index])
    längden_på_listan -= 1
    index += 1

for bokstav in "Hello world!":
    print(bokstav, end=' ')
print()

mängder = {'a', 'b', 'c'}
ordbok = {'a':1, 'b':2, 'c':3}

for key in ordbok.keys():
    print(key)

break_the_computer = True

# while break_the_computer:
#     if input() == 'q': break


finns_lyckotal = False

for tal in range(100000000):
    if tal == 87:
        finns_lyckotal = True
        break
else:
    print('Ditt lycktal fanns inte!')

print(f"{finns_lyckotal=}")