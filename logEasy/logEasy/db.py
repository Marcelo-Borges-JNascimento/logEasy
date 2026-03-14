import pymysql

conexao = pymysql.connect(
    host="localhost",
    database="db_projeto",
    user="root",
    passwd="",
)

cursor = conexao.cursor()
cursor.execute('SHOW TABLES')

for x in cursor:
    print(x)