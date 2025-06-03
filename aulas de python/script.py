print("Bem vindo a segunda calculadora")

i = 1
while i < 6: 
    op = input("Digite a operação desejada +, -, *, / .: ")

    match op:
        case '+':
              n1 = int(input("Digite o primeiro numero: "))
              n2 = int(input("Digite o segundo numero: "))
              print(n1 + n2)
        case '-':
              n1 = int(input("Digite o primeiro numero: "))
              n2 = int(input("Digite o segundo numero: "))
              print(n1 - n2)
        case '*':
              n1 = int(input("Digite o primeiro numero: "))
              n2 = int(input("Digite o segundo numero: "))
              print(n1 * n2)
        case '/':
              n1 = int(input("Digite o primeiro numero: "))
              n2 = int(input("Digite o segundo numero: "))
              print(n1 / n2)
        case _:
              print("Opçao invalida")
        
    pergunta = input("Deseja realizar outro calculo ? Y ou N: ")

    if pergunta.lower() == 'y':
        print("Continuando")
    elif pergunta.lower() == 'n':
        print("Finalizando")
        break
    else:
        print("Opção inválida, encerrando a calculadora...")
        break
        
    i = i + 1
   
else:
  print("i is no longer less than 6")
