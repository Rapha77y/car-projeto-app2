import pandas as pd
import plotly.express as px
import streamlit as st

# Carregar os dados
car_data = pd.read_csv('../vehicles_us.csv')

# Título do aplicativo
st.header('Análise de Anúncios de Venda de Carros 🚗')
st.write('Explore os dados de anúncios de vendas de carros nos EUA.')

# Seção de histograma
st.subheader('Distribuição da Quilometragem')
build_histogram = st.checkbox('Criar um histograma')

if build_histogram:
    st.write('Histograma da coluna odometer (quilometragem)')
    fig = px.histogram(car_data, x='odometer',
                       title='Distribuição da Quilometragem')
    st.plotly_chart(fig, use_container_width=True)

# Seção de dispersão
st.subheader('Preço vs Quilometragem')
build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_scatter:
    st.write('Relação entre preço e quilometragem dos veículos')
    fig = px.scatter(car_data, x='odometer', y='price',
                     title='Preço vs Quilometragem',
                     opacity=0.5)
    st.plotly_chart(fig, use_container_width=True)