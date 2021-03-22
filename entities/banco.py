from entities.pessoa import Pessoa
import MySQLdb

class Banco:

    con = MySQLdb.connect(host='', user='', passwd='', db='')
    cur = con.cursor()

    def __init__(self):
        pass
    
    def fechar_banco(self):
        Banco.cur.close() 

    def add_pessoa(self, nome, email):
        Banco.cur.execute(f"insert into pessoa(NOME, EMAIL) values ('{nome}', '{email}')")
        Banco.con.commit() 

     
    def rmv_pessoa(self, identity):
        Banco.cur.execute(f"delete from pessoa where ID='{identity}'")
        Banco.con.commit() 


    def atualizar_pessoa(self, identity, nome = False, email = False ):
        if(nome):
            Banco.cur.execute(f"update pessoa set NOME='{nome}' where ID='{identity}'")            
            Banco.con.commit() 

        if(email):
            Banco.cur.execute(f"update pessoa set EMAIL='{email}' where ID='{identity}'")
            Banco.con.commit() 
   
            
    def apresentar_pessoa(self, identity):
        if(identity):
            Banco.cur.execute(f"select ID, NOME, EMAIL from pessoa where ID={identity}")
            representacao = Banco.cur.fetchall()
            print()
            for representado in representacao:
                print(f'Id: {representado[0]}, Nome: {representado[1]}, Email: {representado[2]}')
            print()

    def apresentar_pessoas(self):
        Banco.cur.execute(f"select * from pessoa")
        representacao = Banco.cur.fetchall()
        print()       
        for representado in representacao:
            print(f'Id: {representado[0]}, Nome: {representado[1]}, Email: {representado[2]}')
        print()