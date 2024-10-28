# logiska uttryck?

det_regnar = True
har_ett_paraply = False
lyckotal = 8

if det_regnar and (lyckotal % 2 == 0 or har_ett_paraply):
    print('Du kommer inte bli blöt!')
else:
    print('Du kommer bli dygnsur!!')


tal = input('Skriv in ett lyckotal: ')
namn = input('Skriv ditt namn: ')

if (tal.isdigit() 
    and int(tal) % 2 == 0 
    and namn 
    and (namn[0].lower() in ['a', 'b', 'c'])):
    print('Du har ett jämnt lyckotal och ditt namn börjar med antingen a,b eller c')