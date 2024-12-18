import time

condicao = True

while condicao:
    print("Execute minha ETL")
    time.sleep(5)

##############################################

#Validação de Entrada

numero = int(input("Digite um número entre 1 e 10: "))
while numero < 1 or numero > 10:
    print("Número fora do intervalo!")
    numero = int(input("Por favor, digite um número entre 1 e 10: "))

print("Número válido!")

############################################

#Consumo de API Simulado

pagina_atual = 1
paginas_totais = 5  # Simulação, na prática, isso viria da API

while pagina_atual <= paginas_totais:
    print(f"Processando página {pagina_atual} de {paginas_totais}")
    # Aqui iria o código para processar os dados da página
    pagina_atual += 1

print("Todas as páginas foram processadas.")

#####################################################

#Tentativas de Conexão

tentativas_maximas = 5
tentativa = 1

while tentativa <= tentativas_maximas:
    print(f"Tentativa {tentativa} de {tentativas_maximas}")
    # Simulação de uma tentativa de conexão
    # Aqui iria o código para tentar conectar
    if True:  # Suponha que a conexão foi bem-sucedida
        print("Conexão bem-sucedida!")
        break
    tentativa += 1
else:
    print("Falha ao conectar após várias tentativas.")

##########################################################

#Processamento de Dados com Condição de Parada

itens = [1, 2, 3, "parar", 4, 5]

i = 0
while i < len(itens):
    if itens[i] == "parar":
        print("Parada encontrada, encerrando o processamento.")
        break
    # Processa o item
    print(f"Processando item: {itens[i]}")
    i += 1

#######################################################

#Ajuste de validação de salário

#Solicitando nome
nome_valido = False
salario_valido = False
bonus_valido = False

while nome_valido is not True:
    try:
        nome = input("Digite seu nome: ")
        #verificar se o nome está válido
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
          
        #verificar se há números
        elif nome.isdigit():
            raise ValueError("O nome não deve ter números.")
          
        else:
            nome_valido = True
            print("Nome válido: ", nome)
    except ValueError as e:
        print(e)

#solicitando salário

while salario_valido is not True:
    try:
        salario = float(input("Digite o valor do seu salário: "))
        if salario < 0:
            print("Digite uma salário com valor positivo.")
        else:
            salario_valido = True
    except ValueError:
            print("Entrada inválida para salário, digite um valor válido.")

#Solicitando bonus

while bonus_valido is not True:
    try:
        bonus = float(input("Digite seu bônus: "))
        if bonus < 0:
            print("Digite um valor positivo.")
        else:
            bonus_valido = True
    except ValueError:
        print("Valor inválido para o bônus. Digite um valor válido.")

bonus_recebido = 1000 + salario * bonus

print(f"{nome}, seu salário é de R${salario:.2f} e seu bônus é de R${bonus_recebido:.2f}.")
