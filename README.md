# Desafio #1 Bootcamp Engenharia de dados
## Descrição
Inserir dados de planilhas no Banco de Dados usando Python, de forma performática.

Enunciado: Fazer um script python que leia as fontes de dados e então insere os dados no banco de dados postgres.

## Tecnologias utilizadas

* Python 3.9.7 - Linguagem de programação
* PostgreSQL 14.0 - Banco de dados relacional
* Psycopg2-binary 2.9.1 - Biblioteca Python para conectar o banco de dados PostgreSQL

## Fontes de dados

NBA: https://www.kaggle.com/datasets/loganlauton/nba-players-and-team-data

Startups tech: https://www.kaggle.com/datasets/chickooo/top-tech-startups-hiring-2023?select=json_data.json (somente o arquivo json_data.json).

## Pré-requisitos
* Python 3.x instalado
* PostgreSQL 14.x instalado
* Dbeaver 23.x instalado
* Docker Desktop instalado

## Estrutura do projeto

O projeto tem a seguinte estrutura de diretórios e arquivos:

>README.md
>
> dados_nba.py
> 
> dados_ts_hiring.py
> 
> docker-compose.yml

README.md: Arquivo que contém informações sobre o projeto.

dados_nba.py: script python que lê os dados dos arquivos CSV da NBA e insere no banco de dados PostgreSQL.

dados_ts_hiring.py: script python que lê os dados do arquivo JSON de startups de tecnologia e insere no banco de dados PostgreSQL.

docker-compose.yml: script com conexão com o banco de dados criado 'how_postgres'

## Comprovações

Estrutura do banco de dados, com diferentes schemas e respectivas tabelas para cada uma das fontes utilizadas no projeto:

![image](https://github.com/iararosso/bootcamp_desafio1/assets/101842238/983b8846-7e3f-4836-ad68-99001e37af35)


Consulta na tabela ts_hiring.companys

![image](https://github.com/iararosso/bootcamp_desafio1/assets/101842238/2ae4ca71-b17b-4e52-a1ba-0d8646174614)

Consulta na tabela nba.payroll

![image](https://github.com/iararosso/bootcamp_desafio1/assets/101842238/cf54ab46-dbe0-42eb-8a08-74d045735903)




