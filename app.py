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
            popup=f"<b>{row['name']}</b><br>Prof(m): {row['depth']}m<br>Aforo(l/s): {row['quality']}",
            icon=folium.Icon(color="blue", icon="glyphicon glyphicon-record")
        ).add_to(m)
    
    locations = [
    [25.69169390944417, -100.507932218587],
    [25.69192559209441, -100.509466437571],
    [25.69194934992701, -100.5094825802249],
    [25.69196442160188, -100.5094918376959],
    [25.69197535731247, -100.5094994487448],
    [25.69198583651128, -100.5095075522501],
    [25.69200489199797, -100.5095244327667],
    [25.6920230189897, -100.5095437926367],
    [25.6920380777973, -100.5095630141827],
    [25.69206187231172, -100.509601776126],
    [25.6920877136758, -100.509652122399],
    [25.69209154169383, -100.5096573520691],
    [25.69209755065427, -100.5096612142497],
    [25.69210376903599, -100.5096622890876],
    [25.69210765687545, -100.5096617402603],
    [25.69211046662052, -100.5096606796265],
    [25.69211565022695, -100.5096570582278],
    [25.69211903975967, -100.50965231814],
    [25.69191485445513, -100.5094571351094],
    [25.69190672332935, -100.5094489615767],
    [25.6918924542562, -100.5094319421502],
    [25.69187690742733, -100.5094075331019],
    [25.69169048880424, -100.507922510229],
    [25.69168656941926, -100.5079173791212],
    [25.69167408561822, -100.5079110440803],
    [25.69166821697095, -100.5079110698047],
    [25.69166269189443, -100.5079127937701],
    [25.69165605265952, -100.507917492961],
    [25.69165156447617, -100.5079237138741],
    [25.69164881474944, -100.5079364334107],
    [25.6921203344951, -100.5096493451978],
    [25.69165704186733, -100.508205968896],
    [25.69178349121782, -100.5087593795758],
    [25.69179699226897, -100.5088331852019],
    [25.69180042282485, -100.5089291837378],
    [25.69179214889329, -100.5090046081256],
    [25.69178754544164, -100.5090568621729],
    [25.69179401792318, -100.5091031776674],
    [25.69186201152774, -100.5093725702049],
    [25.69187221690743, -100.5093984065329],
    [25.69168127083546, -100.5083511535583],
    [25.69212141514446, -100.5096408892292]]

    folium.Polygon(locations = locations, color ="blue", weight=6, fill_color = "red", fill_opacity = 0.5, fill = True, popup="Area de riego", tooltip="AREA DE RIEGO",).add_to(m)
    folium_static(m)

# --- STREAMLIT UI ---
st.title("POZOS TR")

df = load_well_data()
if not df.empty:
    display_map(df)

st.subheader("AGREGAR UN POZO")
with st.form("well_form"):
    name = st.text_input("NOMBRE")
    latitude = st.number_input("Latitud", format="%.6f")
    longitude = st.number_input("Longitud", format="%.6f")
    depth = st.number_input("Profundidad (m)", min_value=0.0, format="%.2f")
    quality = st.number_input("Aforo (l/s)", min_value=0.0, format="%.2f")
    added_by = st.text_input("ID")
    submit = st.form_submit_button("Add Well")

if submit and name and latitude and longitude:
    new_entry = pd.DataFrame([[latitude, longitude, name, depth, quality, added_by]],
                              columns=["latitude", "longitude", "name", "depth", "quality", "added_by"])
    df = pd.concat([df, new_entry], ignore_index=True)
    save_well_data(df)
    st.rerun()
