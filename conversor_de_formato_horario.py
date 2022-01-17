print('Digite a hora no formato de 24 horas para ser convertida para o formato de 12 horas')

def converter(hora, minuto):
    if minuto < 0 or minuto > 60:
        return 'Formato de minutos inválidos'
    if hora >= 13 and hora <= 23:
        horaconvertida = hora - 12
        return f'{horaconvertida}: {minuto} P.M'
    elif hora == 12:
        horaconvertida = hora
        return f'{horaconvertida} {minuto} P.M'
    elif hora >= 0 and hora <= 11   :
        horaconvertida = hora
        return f'{horaconvertida}:{minuto} A.M'
    else:
        return 'Formato de horas inválido'

while True:
    print() 
    stop = input('Deseja parar o programa: [s] ou [n]: ')
    if stop == 's':
        break
    elif stop == 'n':
        hora = int(input('Digite a hora: '))
        minuto = int(input('Digte os minutos: '))
        resultado = converter(hora, minuto)
        print()
        print(resultado)
    else:
        print('Comando inválido. Digite apenas s ou n')
        continue