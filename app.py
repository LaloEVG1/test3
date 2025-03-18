import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# Initialize session state for storing well data
if 'wells' not in st.session_state:
    st.session_state.wells = []

st.title("UBICACIÓN POZOS DE AGUA TR")

# Sidebar to select map coordinates and zoom
st.sidebar.header("Configuración del mapa")
lat = st.sidebar.number_input("Latitud", value=25.67507, format="%.6f")
lon = st.sidebar.number_input("Longitud", value=-100.31847, format="%.6f")
zoom = st.sidebar.slider("Zoom", min_value=5, max_value=20, value=12)

# Sidebar to add water well locations
st.sidebar.header("Agregar pozos")
well_lat = st.sidebar.number_input("Latitud del pozo", format="%.6f")
well_lon = st.sidebar.number_input("Longitud del pozo", format="%.6f")
well_name = st.sidebar.text_input("Id del pozo")
well_info = st.sidebar.text_area("Información adicional")

if st.sidebar.button("Agregar pozo"):
    if well_name and well_info:
        st.session_state.wells.append({
            "lat": well_lat,
            "lon": well_lon,
            "name": well_name,
            "info": well_info
        })
        st.sidebar.success("Pozo agregado satisfactoriamente!")
    else:
        st.sidebar.error("Please enter a well name and information.")

# Create a Folium map centered at selected coordinates
m = folium.Map(location=[lat, lon], zoom_start=zoom)

# Add well markers
for well in st.session_state.wells:
    folium.Marker(
        location=[well["lat"], well["lon"]],
        popup=f"<b>{well['name']}</b><br>{well['info']}",
        tooltip=well["name"],
        icon=folium.Icon(color="red")
    ).add_to(m)

# Display the map
st_folium(m, width=1500, height=1500)
