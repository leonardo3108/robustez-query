import pyodbc


conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Fontes/robustez-query/data/dados_robustez_query.accdb')
cursor = conn.cursor()
cursor.execute('select * from metrica')
   
for row in cursor.fetchall():
    print (row)