# Importar as bibliotecas necessárias
import streamlit as st 
import pandas as pd 
import sqlite3

# Conectar ao banco de dados SQlite
conn = sqlite3.connect('../data/quotes.db')

# Carregar os dados em um dataframe
df = pd.read_sql_query('SELECT * FROM mercadolivre_items', conn)

# Encerrar a conexão com o SQlite
conn.close()

# Título da aplicação
st.title('Pesquisa de Mercado - Tênis Esportivos no Mercado Livre')

# Melhorar o layout das colunas para KPI
col1, col2, col3 = st.columns(3)

# KPI 1: Número total de items
total_itens = df.shape[0]
col1.metric(label='Número Total de Itens', value=total_itens)

# KPI 2: Número total de marcas únicas
unique_brands = df['brand'].nunique()
col2.metric(label='Número de Marcas Únicas', value=unique_brands)

# KPI 3: Preço médio
avg_new_price = df['new_price'].mean()
col3.metric(label='Preço médio (R$)', value=f'{avg_new_price:.2f}')

# KPI 4: Qual marcas mais encontradas até a página 10
st.subheader('Marcas mais encontradas até a página 10')
col1, col2 = st.columns([4,2])
top_10_brands = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10_brands)
col2.write(top_10_brands)

# KPI 5: Qual o preço médio por marca
st.subheader('Preço médio por marca')
col1, col2 = st.columns([4,2])
agv_price_brand = df.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(agv_price_brand)
col2.write(agv_price_brand)

# KPI 6: Qual a satisfação por marca
st.subheader('Satisfação por marca')
col1, col2 = st.columns([4,2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_brand)
col2.write(satisfaction_brand)