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

st.header('Datos de consumo relacionados a la venta de vehiculos')

type_button = st.button('Tipo de vehiculo con mayor disponibilidad en stock')
if type_button:
     st.write('Visualización de stock por tipo de vehiculo')
     fig = px.bar(car_data, x='type', title = 'Tipo de vehículos disponibles en stock', color ='type')
     st.plotly_chart(fig, use_container_width=True)

fuel_per_type = car_data.groupby('fuel')['type'].count()
combustible_button = st.button('Combustible principal')
if combustible_button:
     st.write('Visualización de combustible principal')
     fig = px.bar(fuel_per_type, title = 'Combustible principal')
     st.plotly_chart(fig, use_container_width=True)

transmission_per_type = car_data.groupby('transmission')['type'].count()
transmission_button = st.button('Transmisión principal')
if transmission_button:
     st.write('Tipo de transmisión más comun en el stock actual')
     fig = px.bar(transmission_per_type, title = 'Transmisión principal')
     st.plotly_chart(fig, user_container_width=True)

model_per_type = car_data.groupby('model_year')['type'].count()
model_button = st.button('Modelos en stock')
if model_button:
     st.write('Visualización de los modelos en stock')
     fig = px.bar(model_per_type, title = 'Agrupación por modelo')
     st.plotly_chart(fig, user_container_width=True)