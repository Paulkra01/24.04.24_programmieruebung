from PIL import Image
import streamlit as st
import read_data as rd
import matplotlib.pyplot as plt
import plotly.express as px
import EKG_Plot as ekg
import plotly.graph_objects as go


col1,col2 = st.columns([0.6,0.4], gap="small")

with col1:
   st.header("EKG APP")
#    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    
    st.image("https://cdn.pixabay.com/photo/2020/04/25/11/16/electrocardiogram-5090352_1280.jpg")

with st.container():
   st.write("Bitte eine Versuchsperson auswählen:")

   # You can call any Streamlit command, including custom components:


# Session State wird leer angelegt, solange er noch nicht existiert
if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'

person_names = rd.get_person_list()


st.session_state.current_user = st.selectbox('Versuchsperson', options = person_names, key="sbVersuchsperson")

st.write( st.session_state.current_user)

print(st.session_state.current_user)

# Auslesen des Pfades aus dem zurückgegebenen Dictionary
current_picture_path = rd.find_person_data_by_name(st.session_state.current_user)["picture_path"]


if 'picture_path' not in st.session_state:
        st.session_state.picture_path = 'data/pictures/none.jpg'

# Suche den Pfad zum Bild, aber nur wenn der Name bekannt ist
if st.session_state.current_user in person_names:
        st.session_state.picture_path = rd.find_person_data_by_name(st.session_state.current_user)["picture_path"]


# Öffne das Bild und Zeige es an
image = Image.open("../" + st.session_state.picture_path)
st.image(image, caption=st.session_state.current_user)

def callback_function():
    # Logging Message
    print(f"The user has changed to {st.session_state.current_user}")
    # Manuelles wieder ausführen
    #st.rerun()

# Nutzen Sie ihre neue Liste anstelle der hard-gecodeten Lösung
Input_max_heart_rate = st.number_input("Maximale Herzfrequenz", min_value=0, max_value=300, value=0, step=1)

def ekg():
    st.title("EKG-Diagramm")
    ekg_fig = ekg.create_figure()
    st.plotly_chart(ekg_fig, use_container_width=True)   
   # You can call any Streamlit command, including custom components:


# Extrafunktionen