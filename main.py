# pip install mysql-connector-python


import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='q1w2e3',
    database='db_crud_0223'
)

meu_cursor = conexao.cursor()

# Crud

# C
meu_cursor.execute('insert into pessoas (nome, dataNasc) value ("Matheus", "1988-05-06")')
conexao.commit() # executa o scripit sql no banco

#Read

meu_cursor.execute('select * from pessoas')
lista = meu_cursor.fetchall()
for i in lista:
    print(i)

# U
nome = input('Informe o novo nome:')
cod = int (input('Informe o id da pessoa: '))
sql = f'update pessoas set nome = "{nome}" where id = {cod}'
meu_cursor.execute(sql)
conexao.commit()

# D
cod = int (input('Informe o id da pessoa: '))
sql = f'delete from pessoa where id = {cod}'
meu_cursor.execute(sql)
conexao.commit()