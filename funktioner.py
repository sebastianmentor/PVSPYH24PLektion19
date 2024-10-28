def kontrollera_lyckotal(tal):
    if tal % 2 == 0:
        return True
    return False

def skriv_ut_om_det_är_lyckotal(är_lyckotal):
    if är_lyckotal:
        print(f'talet {talet} är ett jämnt lyckotal!')
    else:
        print(f'talet {talet} är ett inte ett jämnt lyckotal!')

talet = 4
skriv_ut_om_det_är_lyckotal(kontrollera_lyckotal(talet))

talet =  5 
skriv_ut_om_det_är_lyckotal(kontrollera_lyckotal(talet))


def run_fuction(fun):
    fun()

def meny_1():
    print('Meny 1')

def meny_2():
    print('Meny 2')

def error_input():
    print('Fel input!')

meny_dict = {'1': meny_1, '2': meny_2}

# val = input('Välj 1 eller 2: ')

# menu_func = meny_dict.get(val, error_input)
# run_fuction(menu_func)

def return_fun_function(val):
    if not isinstance(val, int):
        return None, None
    
    return val**2, val**3

kvadrat, kubik = return_fun_function('8')
print(kvadrat, kubik)


def dictionary_manipulater(dicten:dict):
    if 4 in dicten.keys():
        dicten.pop(4)

    for key, val in dicten.items():
        if val == '4':
            dicten.pop(key)
            break


d = {'1': 1, 4:'4', 5:'5', 'Banan':'4'}

print(d)
dictionary_manipulater(d)
print(d)