from math import pow

def composto(capital, juros, tempo):
    return capital*pow((1+juros),tempo)

capital = float(input('Qual o capital de investimento? '))
juros = float(input('Qual o juros anual em porcentagem (%)? '))
tempo = int(input('Quanto meses será o investimento? '))

juros = juros / 100
tempo = tempo / 12
valor_final_composto = composto(capital, juros, tempo)
print(f'O montante final será de: {valor_final_composto:.02f}')
print(f'Os juros do rendimento foram de: {(valor_final_composto - capital):.02f}')
