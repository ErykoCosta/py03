#dados de vendas e verificar se tem algum negativo

qtd = 40
preco = 20

if qtd > 0 and preco > 0:
    print("Valores válidos")
else:
    print("valores inválidos")

#####################################################

#Estruturas de Controle de Fluxo

x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

#######################################################

#Verificação de Qualidade de Dados

quantidade = 10  # Exemplo de valor, substitua com input do usuário se necessário
preço = 20  # Exemplo de valor, substitua com input do usuário se necessário

if quantidade > 0 and preço > 0:
    print("Dados válidos")
else:
    print("Dados inválidos")

##########################################################

#Classificação de Dados de Sensor

temperatura = 22  # Exemplo de valor, substitua com input do usuário se necessário

if temperatura < 18:
    print("Baixa")
elif 18 <= temperatura <= 26:
    print("Normal")
else:
    print("Alta")

#########################################################

#Filtragem de Logs por Severidade - dicionário

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level'] == 'ERROR':
    print(log['message'])

########################################################

#Validação de Dados de Entrada

idade = 25  # Exemplo de valor, substitua com input do usuário se necessário
email = "usuario@exemplo.com"  # Exemplo de valor, substitua com input do usuário se necessário

if not 18 <= idade <= 65:
    print("Idade fora do intervalo permitido")
elif "@" not in email or "." not in email:
    print("Email inválido")
else:
    print("Dados de usuário válidos")

######################################################

#Detecção de Anomalias em Dados de Transações

transacao = {'valor': 12000, 'hora': 20}

if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
    print("Transação suspeita")
else:
    print("Transação normal")

######################################################

lista = ["Zé", "Luciano", "Jorge", "Lucas"]

for aluno in lista:
    print(aluno)

######################################################

#contagem de palavras

texto = "Testando a quantidade de palavras em um texto"

palavras = texto.split()

contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] = +1
    else:
        contagem[palavra] = 1
print(contagem)

###################################################

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

#####################################################

#Normalização de Dados

numeros = [10, 20, 30, 40, 50]
minimo = min(numeros)
maximo = max(numeros)
normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

print(normalizados)

##################################################

#Filtragem de Dados Faltantes

usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]

print(usuarios_validos)

###################################################

#Extração de Subconjuntos de Dados

numeros = range(1, 11)
pares = [x for x in numeros if x % 2 == 0]

print(pares)

##################################################

#Agregação de Dados por Categoria

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

total_por_categoria = {}
for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in total_por_categoria:
        total_por_categoria[categoria] += valor
    else:
        total_por_categoria[categoria] = valor

print(total_por_categoria)