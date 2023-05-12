from sqlalchemy import create_engine
import pandas as pd
import psycopg2
import decimal
import numpy as np

#transformar o arquivo json em dataframe do pandas

df_hiring = pd.read_json(r'C:\Users\dleto\Documents\Iara2\DESAFIO001/json_data.json')

#remover coluna logo_url
df_hiring = df_hiring.drop('logo_url', axis=1)

#converter as listas e dicionários dentro do json em string
df_hiring = df_hiring.applymap(json.dumps)


#conectar=se ao banco de dados PostgreSQL

conn = psycopg2.connect(
    host="localhost",
    database="desafio_01",
    user="iara",
    password="iara"
)

#abrir um cursor para executar comandos SQL
cur = conn.cursor()

#criar tabelas no banco de dadosjon
cur.execute("""
CREATE SCHEMA ts_hiring;

CREATE TABLE ts_hiring.companys (
	id TEXT
	,company_name TEXT
	,headline TEXT
	,tags TEXT
	,website TEXT
	,employees TEXT
	,about TEXT
	,locations TEXT
	,industries TEXT
	,jobs TEXT
	);
""")

# popular a tabela ts_hiring
data_ts = [tuple(x) for x in df_hiring.to_numpy()]
cols = ','.join(list(df_hiring.columns))

ts = f"INSERT INTO ts_hiring.companys ({cols}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
cur.executemany(ts, data_ts)


# salvar as alterações e encerrar a conexão com o banco de dados
conn.commit()
cur.close()
conn.close()