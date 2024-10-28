########################
########################
########################
# Sekvenser
min_lista = [1,2,3,4] # Mutable type
min_tuple = (1,2,3,4) # Imutable type
min_sträng = 'Jag är också en sekvens!!' # Imutable type
# print(id(min_sträng))
min_sträng = min_sträng.replace(' ', '@')
# print(id(min_sträng))
# print(id(ny_text))
########################
ny_sträng = ''
for char in min_sträng:
    
    tal = ord(char)
    char = chr(tal + 2)

    print(f"{id(ny_sträng)=}, {ny_sträng}")
    ny_sträng += char

print(f"{id(ny_sträng)=}, {ny_sträng}")

########################
print(min_lista[::2])
print(min_sträng[:10:3])

min_sträng = 'j' + min_sträng[1:]
print(min_sträng)

########################
########################
########################
# Oårdnade data
min_mängd = {1,2,3,4} # ett set (mängd på svenska) 
print(5 in min_mängd, 3 in min_mängd)

min_dict = {1:'1', 2:'2', 3:'3', 4:'4'} # Ordbok!! ;D Mutable

# min_dict[min_lista] = 'Hejsan'

class A:
    ...

a = A()

min_dict[a] = 'Vår klass a'
print(min_dict[a], min_dict[3])

# Värdet i en dictionary

min_dict['chr'] = chr
min_dict['make_class_a'] = A
min_dict['float'] = float
min_dict['vår_lista'] = [{'Hejsan':'Då', 2:4, 'lista2':[(1,2,3),()]}]

tabell_med_data = []

for rad in range(1, 5):
    rad_lista = []
    for värde in range(rad, rad + 5):
        rad_lista.append(värde)
    tabell_med_data.append(rad_lista)

for rad in tabell_med_data:
    print(rad)

dictionary_tabell = {} 

for rad in range(1, 5):

    column_dict = {}

    for key in range(1, 5):
        column_dict[key] = str(key + rad)
        
    dictionary_tabell[rad] = column_dict

for rad_id, rad in dictionary_tabell.items():
    print(rad_id,  rad) 

print(dictionary_tabell[3][4])

# Datatyper
int
float
complex
str
list
dict
frozenset
set
...