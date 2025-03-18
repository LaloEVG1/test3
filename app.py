import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# Initialize session state for storing well data
if 'wells' not in st.session_state:
    st.session_state.wells = []

st.title("City Water Well Map")

# Sidebar to select map coordinates and zoom
st.sidebar.header("Map Settings")
lat = st.sidebar.number_input("Latitude", value=0.0, format="%.6f")
lon = st.sidebar.number_input("Longitude", value=0.0, format="%.6f")
zoom = st.sidebar.slider("Zoom Level", min_value=5, max_value=20, value=12)

# Sidebar to add water well locations
st.sidebar.header("Add a Water Well")
well_lat = st.sidebar.number_input("Well Latitude", format="%.6f")
well_lon = st.sidebar.number_input("Well Longitude", format="%.6f")
well_name = st.sidebar.text_input("Well Name")
well_info = st.sidebar.text_area("Additional Information")

if st.sidebar.button("Add Well"):
    if well_name and well_info:
        st.session_state.wells.append({
            "lat": well_lat,
            "lon": well_lon,
            "name": well_name,
            "info": well_info
        })
        st.sidebar.success("Well added successfully!")
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
        icon=folium.Icon(color="blue")
    ).add_to(m)

# Display the map
st_folium(m, width=700, height=500)
