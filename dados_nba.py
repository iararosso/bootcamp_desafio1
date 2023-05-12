from sqlalchemy import create_engine
import pandas as pd
import psycopg2
import decimal
import numpy as np

#transformar os arquivos csv em dataframes do pandas

df_payroll = pd.read_csv(r'C:\Users\dleto\Documents\Iara2\DESAFIO001/NBA Payroll(1990-2023).csv')
df_box_score = pd.read_csv(r'C:\Users\dleto\Documents\Iara2\DESAFIO001/NBA Player Box Score Stats(1950 - 2022).csv')
df_player_stats = pd.read_csv(r'C:\Users\dleto\Documents\Iara2\DESAFIO001/NBA Player Stats(1950 - 2022).csv')
df_salaries = pd.read_csv(r'C:\Users\dleto\Documents\Iara2\DESAFIO001/NBA Salaries(1990-2023).csv')

#corrigir o titulo das colunas dos dataframes

df_payroll.rename(columns = {'Unnamed: 0': 'id'}, inplace = True)
df_box_score.rename(columns = {'Unnamed: 0': 'id'}, inplace = True)
df_player_stats.rename(columns = {'Unnamed: 0.1': 'id', 'Unnamed: 0':'Unnamed'}, inplace = True)
df_salaries.rename(columns = {'Unnamed: 0': 'id'}, inplace = True)


#conectar=se ao banco de dados PostgreSQL

conn = psycopg2.connect(
    host="localhost",
    database="desafio_01",
    user="iara",
    password="iara"
)

#abrir um cursor para executar comandos SQL
cur = conn.cursor()

#criar tabelas no banco de dados
cur.execute("""
CREATE SCHEMA nba;

CREATE TABLE nba.Payroll (
	id serial
	,team VARCHAR(100)
	,seasonStartYear INT
	,payroll VARCHAR(20)
	,inflationAdjPayroll VARCHAR(30)
	);

CREATE TABLE nba.Salaries (
	id serial
	,playerName VARCHAR(100)
	,seasonStartYear INT
	,salary VARCHAR(30)
	,inflationAdjSalary VARCHAR(30)
	);

CREATE TABLE nba.PlayerStats (
	id serial
	,Unnamed INT
	,Season INT
	,Player VARCHAR(100)
	,Pos VARCHAR(30)
	,Age INT
	,Tm VARCHAR(30)
	,G FLOAT
	,GS FLOAT
	,MP FLOAT
	,FG_UM FLOAT
	,FGA DECIMAL
	,FG_DOIS DECIMAL
	,TRESP_UM FLOAT
	,TRESPA FLOAT
	,TRESP_DOIS DECIMAL
	,DOISP_UM FLOAT
	,DOISPA FLOAT
	,DOISP_DOIS DECIMAL
	,eFG DECIMAL
	,FT_UM FLOAT
	,FTA FLOAT
	,FT_DOIS DECIMAL
	,ORB FLOAT
	,DRB FLOAT
	,TRB FLOAT
	,AST FLOAT
	,STL FLOAT
	,BLK FLOAT
	,TOV FLOAT
	,PF FLOAT
	,PTS FLOAT
	);

CREATE TABLE nba.BoxScore (
	id serial
	,Season INT
	,Game_ID INT
	,PLAYER_NAME VARCHAR(100)
	,Team VARCHAR(3)
	,GAME_DATE VARCHAR(15)
	,MATCHUP VARCHAR(20)
	,WL VARCHAR(2)
	,MIN INT
	,FGM INT
	,FGA FLOAT
	,FG_PCT DECIMAL
	,FG3M FLOAT
	,FG3A FLOAT
	,FG3_PCT DECIMAL
	,FTM INT
	,FTA FLOAT
	,FT_PCT DECIMAL
	,OREB FLOAT
	,DREB FLOAT
	,REB FLOAT
	,AST FLOAT
	,STL FLOAT
	,BLK FLOAT
	,TOV FLOAT
	,PF FLOAT
	,PTS INT
	,PLUS_MINUS DECIMAL
	,VIDEO_AVAILABLE INT
	);
""")

# popular a tabela Payroll
data_payroll = [tuple(x) for x in df_payroll.to_numpy()]
cols = ','.join(list(df_payroll.columns))

payroll = f"INSERT INTO nba.Payroll ({cols}) VALUES (%s, %s, %s, %s, %s)"
cur.executemany(payroll, data_payroll)

# popular a tabela Salaries
data_salaries = [tuple(x) for x in df_salaries.to_numpy()]
cols = ','.join(list(df_salaries.columns))

query_salaries = f"INSERT INTO nba.salaries ({cols}) VALUES (%s, %s, %s, %s, %s)"
cur.executemany(query_salaries, data_salaries)

# popular a tabela Player Stats
data_player_stats = [tuple(x) for x in df_player_stats.to_numpy()]
cols = ','.join(list(df_player_stats.columns))

query_player_stats = f"INSERT INTO nba.playerstats ({cols}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" 
cur.executemany(query_player_stats, data_player_stats)

# popular a tabela box score
data_player_box = [tuple(x) for x in df_box_score.to_numpy()]
cols = ','.join(list(df_box_score.columns))

query_player_box = f"INSERT INTO nba.boxscore ({cols}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
cur.executemany(query_player_box, data_player_box)

# salvar as alterações e encerrar a conexão com o banco de dados
conn.commit()
cur.close()
conn.close()