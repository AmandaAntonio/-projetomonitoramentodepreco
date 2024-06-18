# Projeto Monitoramento de Preço

Este projeto consiste em uma solução ETL (Extração, Transformação e Carga) em Python voltada para monitoramento de preço. Ele fornece uma pipeline que coleta, consolida e gera insights sobre detreminado produto.

# Arquitetura
* Extração: Realizada com Scrapy
* Transformação e Carga: Gerenciadas com Pandas
* Dashboard: Construído com Streamlit
* Banco de Dados: Sqlite3

**Diagrama**



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
