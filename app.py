import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
from github import Github
import io

#CONFIGURATION


GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
REPO_NAME = "LaloEVG1/test3"
DATA_FILE = "wells_data.csv"



def load_well_data():
    """Fetch well data from GitHub repository."""
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)
    try:
        contents = repo.get_contents(DATA_FILE)
        data = contents.decoded_content.decode("utf-8")
        df = pd.read_csv(io.StringIO(data))
        return df
    except Exception as e:
        st.error(f"Error loading well data: {e}")
        return pd.DataFrame(columns=["latitude", "longitude", "name", "depth", "quality", "added_by"])

def save_well_data(df):
    """Save updated well data to GitHub."""
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)
    contents = repo.get_contents(DATA_FILE)
    csv_data = df.to_csv(index=False)
    repo.update_file(DATA_FILE, "Updated well data", csv_data, contents.sha)
    st.success("New well added successfully!")

def display_map(df):
    """Display map with well markers."""
    m = folium.Map(location=[df["latitude"].mean(), df["longitude"].mean()], zoom_start=12)
    for _, row in df.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=f"<b>{row['name']}</b><br>Depth: {row['depth']}m<br>Quality: {row['quality']}"
        ).add_to(m)
    folium_static(m)

# --- STREAMLIT UI ---
st.title("POZOS TR")

df = load_well_data()
if not df.empty:
    display_map(df)

st.subheader("AGREGAR UN POZO")
with st.form("well_form"):
    name = st.text_input("NOMBRE")
    latitude = st.number_input("Latitude", format="%.6f")
    longitude = st.number_input("Longitude", format="%.6f")
    depth = st.number_input("PROFUNDIDAD (m)", min_value=0.0, format="%.2f")
    quality = st.selectbox("AFORO", min_value=0.0, format="%.2f")
    added_by = st.text_input("ID")
    submit = st.form_submit_button("Add Well")

if submit and name and latitude and longitude:
    new_entry = pd.DataFrame([[latitude, longitude, name, depth, quality, added_by]],
                              columns=["latitude", "longitude", "name", "depth", "quality", "added_by"])
    df = pd.concat([df, new_entry], ignore_index=True)
    save_well_data(df)
    st.rerun()
