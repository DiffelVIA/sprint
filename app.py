import pandas as pd
import streamlit as st
import plotly.express as px
car_data = pd.read_csv('vehicles_us.csv')
st.header('Sitio Web Venta de autos')
hist_button = st.button('Construir histograma')
if hist_button:
     st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
     fig = px.histogram(car_data, x="odometer")
     st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir diagrama de dispersión')
if scatter_button:
     st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
     fig = px.scatter(car_data, x="odometer")
     st.plotly_chart(fig, use_container_width=True)
st.header('Datos agrupados')
fuel_per_type = car_data.groupby('fuel')['type'].count()
fig = px.bar(fuel_per_type, title = 'Combustible principal')
button_1 = st.button('Combustible principal')
if button_1:
     st.write('Visualización de combustible principal')
     fig = px.bar(fuel_per_type, title = 'Combustible principal')
     st.plotly_chart(fig, use_container_width=True)