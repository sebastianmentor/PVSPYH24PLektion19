with open('filnamn.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())


lista_med_djur = ['Ko', 'Katt', 'Hund', 'Fågel']

with open('djur.txt', 'a', encoding='utf-8') as f:
    for djur in lista_med_djur:
        f.write(djur + '\n')


ny_lista_med_djur = []

with open('djur.txt', 'r', encoding='utf-8') as f:
    for djurrad in f.readlines():
        djur = djurrad.strip()
        ny_lista_med_djur.append(djur)

for djur in ny_lista_med_djur:
    print(djur)

# with open('djur.txt', 'a+', encoding='utf-8') as f:
#     f.write('Nytt Djur\n')
#     f.seek(0)
#     data = f.read()
#     f.write('Opsidopsi\n')
#     print('test', f.read())

# print(data)