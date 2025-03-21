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
    [25.69212141514446, -100.5096408892292],
    [25.69169390944417, -100.507932218587],
    [25.69169048880424, -100.507922510229],
    [25.69168656941926, -100.5079173791212],
    [25.69167408561822, -100.5079110440803],
    [25.69166821697095, -100.5079110698047],
    [25.69166269189443, -100.5079127937701],
    [25.69165605265952, -100.507917492961],
    [25.69165156447617, -100.5079237138741],
    [25.69164881474944, -100.5079364334107],
    [25.69165704186733, -100.508205968896],
    [25.69179401792318, -100.5091031776674],
    [25.69186201152774, -100.5093725702049],
    [25.69187221690743, -100.5093984065329],
    [25.69187690742733, -100.5094075331019],
    [25.6918924542562, -100.5094319421502],
    [25.69190672332935, -100.5094489615767],
    [25.69209154169383, -100.5096573520691],
    [25.69209755065427, -100.5096612142497],
    [25.69210376903599, -100.5096622890876],
    [25.69210765687545, -100.5096617402603],
    [25.69211046662052, -100.5096606796265],
    [25.69211565022695, -100.5096570582278],
    [25.69211903975967, -100.50965231814],
    [25.6921203344951, -100.5096493451978],
]

    folium.Polygon(locations = locations, color ="blue", weight=6, fill_color = "red", fill_opacity = 0.5, fill = True, popup="Area de riego", tooltip="AREA DE RIEGO",).add_to(m)
    
    
    locations = [
    [25.60374115904774, -100.1064613009849],
    [25.60363570392093, -100.10656417112764],
    [25.60375951431288, -100.10686108027129],
    [25.603763218957027, -100.1068690806999],
    [25.60377074438254, -100.10687689723784],
    [25.603776536148942, -100.10687994789635],
    [25.603784831208696, -100.10688151796373],
    [25.603792632139584, -100.10688037493317],
    [25.60401081088894, -100.10681186203003],
    [25.603970094514793, -100.10668467310947],
    [25.603937010936118, -100.10659882011586],
    [25.60388852753371, -100.10649093793172],
    [25.603829186451705, -100.10637886320006]
]

    folium.Polygon(locations = locations, color ="blue", weight=6, fill_color = "red", fill_opacity = 0.5, fill = True, popup="Area de riego", tooltip="AREA DE RIEGO",).add_to(m)
    
    locations = [
        [25.604123475872328, -100.10815911110811],
        [25.6041149955729, -100.1078186014567],
        [25.60411043615318, -100.10779472017153],
        [25.604095009998495, -100.10777024084659],
        [25.604073339256107, -100.10775600046856],
        [25.604051471318822, -100.10775229375471],
        [25.60371822359774, -100.10776232728459],
        [25.603695939311976, -100.10776471097348],
        [25.603678731472705, -100.10777398251174],
        [25.60366084887421, -100.107791273884],
        [25.60341424193021, -100.10803183369416],
        [25.603400552696602, -100.10805100584878],
        [25.603393480144, -100.10807875296327],
        [25.603396025527857, -100.10810269521117],
        [25.603408889201198, -100.1081281167216],
        [25.60353313614243, -100.10828245401123],
        [25.60354591860097, -100.1082923803689],
        [25.603554861458893, -100.10829663517059],
        [25.60356834432573, -100.10829992608623],
        [25.603579963904437, -100.10830007304985],
        [25.604063396689586, -100.10822916882755],
        [25.604085005698796, -100.10822415010419],
        [25.60410657359546, -100.10820787854989],
        [25.604120114685497, -100.10818323803954],
    ]

    folium.Polygon(locations = locations, color ="blue", weight=6, fill_color = "red", fill_opacity = 0.5, fill = True, popup="Area de riego", tooltip="AREA DE RIEGO",).add_to(m)
    locations = [
    [25.603467259541922, -100.1096584021227],
    [25.60346424503534, -100.10969154394095],
    [25.60347719701499, -100.1097160005299],
    [25.603694443605495, -100.11002022784531],
    [25.603705194147057, -100.11003137041217],
    [25.603720131497994, -100.11004050031998],
    [25.60373914048986, -100.11004494779199],
    [25.603753865430996, -100.1100439983606],
    [25.60377182968223, -100.11003739288799],
    [25.60382153896132, -100.11000844627081],
    [25.603832716440877, -100.10999784475072],
    [25.60384265048124, -100.1099821432623],
    [25.60384855473787, -100.10996204300221],
    [25.60384924691335, -100.10994579810814],
    [25.60379594300774, -100.10944074949781],
    [25.60379119270053, -100.10942064050249],
    [25.603771738077967, -100.10939876270551],
    [25.603750345536945, -100.10939309838895],
    [25.60371967655934, -100.10940691570762],
]
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
