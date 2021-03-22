#!/usr/bin/python
# import MySQLdb

from entities.pessoa import Pessoa
from entities.banco import Banco

db = Banco()
print("Bem-vindo ao sistema de cadastros. Selecione uma das opções abaixo:")
selecao = int(input("[1] Cadastro / [2] Atualização / [3] Deleção / [4] Listagem / [5] Sair\nR: "))
print()

# Create
if(selecao == 1):
    cadastro = int(input("Quantas pessoas deseja cadastrar? "))
    
    for item in range(1, cadastro + 1):
        print()
        print(f"Cadastro num: {item}")
        nome = input('Digite o nome: ')
        email = input('Digite o emmail: ')
        pessoa = Pessoa(nome, email)
        db.add_pessoa(pessoa.nome, pessoa.email)
        print(f"Você cadastrou: {pessoa}")

# Update
if(selecao == 2):
    identity = int(input('Informe o ID do cliente para atualizar os dados: '))
    escolha = int(input("Deseja atualizar: [1] Nome e Email / [2] Nome / [3] Email: " ))
    
    if(escolha == 1):
        nome = input('Digite o nome: ')
        email = input('Digite o email: ')
        db.atualizar_pessoa(identity, nome=nome, email=email)
    elif(escolha == 2):
        nome = input('Digite o nome: ')
        db.atualizar_pessoa(identity, nome=nome)
    elif(escolha == 3):
        email = input('Digite o email: ')
        db.atualizar_pessoa(identity, email=email)

    db.apresentar_pessoa(identity)

# Delete
if (selecao == 3):
    identity = int(input('Informe o ID do cliente para deleta-lo do Banco de Dados: '))
    print('Usuario removido: ')
    db.rmv_pessoa(identity)
    db.apresentar_pessoas()


# Read
if(selecao == 4):
    print("Você deseja listar todos os clientes ou listar apenas um cliente?")
    selecao = int(input("Selecione: [1] Todos / [2] Apenas um\nR: "))
    
    if(selecao == 1):
        db.apresentar_pessoas()
    elif(selecao == 2):
        identity = int(input('Informe o ID do cliente: '))
        db.apresentar_pessoa(identity)


db.fechar_banco()