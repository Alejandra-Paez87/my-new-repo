import pandas as pd
import plotly.express as px
import streamlit as st
car_data = pd.read_csv("vehicles_us.csv")

st.header('Explorador de Datos de Vehículos')

build_histogram = st.checkbox('Construir un histograma')
     
if build_histogram: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
         fig = px.histogram(car_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir grafico de dispersion') # crear un botón
     
if disp_button: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Creación de un gráfico de dispersión de precio en función del kilometraje')
         # crear un gráfico de dispersión
         fig = px.scatter(car_data, x="odometer", y="price")
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)


