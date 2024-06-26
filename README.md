# Projeto Monitoramento de Preço

Este projeto consiste em uma solução ETL (Extração, Transformação e Carga) em Python voltada para monitoramento de preço. Ele fornece uma pipeline que coleta, consolida e gera insights sobre tênis esportivos do Mercado Livre.

**Objetivo** 

Realizar uma pesquisa de mercado na categoria de tênis esportivo dentro do mercado livre para avaliar os seguintes pontos:

 * Quais marcas são mais encontradas até a 10ª página.
 * Qual o preço médio por marca.
 * Qual a satisfação por marca.



# Arquitetura
* Extração: Scrapy
* Transformação e Carga: Pandas
* Dashboard: Streamlit
* Banco de Dados: Sqlite3

**Diagrama**

![Diagrama](img/Diagrama%20Monitoramente%20de%20Preco.drawio.png)


# Como Usar
Para rodar o web scraping [comando a partir da diretório coleta]

```bash
scrapy crawl mercadolivre -o ../data/data.jsonl
```
Para rodar as transformações e criar um banco de dados SQLite [comando a partir do diretório scr]

```bash
python transformacao/main.py
```
Para rodar o dashboard [comando a partir do diretóro scr]

```bash
streamlit run dashboard/app.py
```
