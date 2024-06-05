# Projeto Monitoramento de Preço

Para rodar o web scraping [comando a partir da diretório coleta]

```bash
scrapy crawl mercadolivre -o ../data/data.jsonl
```
Para rodar as transformações e criar um banco de dados SQLite [comando a partir do diretório scr]

```bash
python transformacao/main.py
```
