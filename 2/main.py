from PIL import Image
import streamlit as st
import read_data as rd
from PIL import Image
import streamlit as st
import read_data as rd
import create_plots as cp
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Inhalt für jeden Tab hinzufügen
def tab1_content():
    st.header('EKG-Verzeichnis')
    st.write('Patientenverzeichnis')
    
    col1,col2 = st.columns([0.6,0.4], gap="small")

    with col1:

        st.write("EKG-Verzeichnis")
        
    with col2:
    
        st.image("https://cdn.pixabay.com/photo/2020/04/25/11/16/electrocardiogram-5090352_1280.jpg")

    with st.container():
        st.write("Bitte eine Versuchsperson auswählen:")

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
        st.image(image)

def callback_function():
    # Logging Message
    print(f"The user has changed to {st.session_state.current_user}")
    # Manuelles wieder ausführen
    #st.rerun()

# Funktion für Tab 2
def tab2_content():
    st.header('CSV-Datenanalyse')
    st.write('Analyse Leistung und Herzfrequenz über die Zeit')
    with st.expander("HERZFREQUENZEINGABE"):
        Input_max_heart_rate = st.number_input("Maximale Herzfrequenz", min_value=0, max_value=300, value=0, step=1)

    #st.title("Power and Heart Rate Plot")
    #st.write("Dies ist der Inhalt von Tab 1.")
    with st.expander("DATENANALYSE"):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.button("Leistung")
            
                
        with col2:
            st.button("Power Zone")
        with col3:
            st.button("Heart Rate")
    with st.expander("GRAFIK"):
    # Daten einlesen
        fig = cp.createFigure()
        st.plotly_chart(fig)

def main():
    st.title('Datenauswertung')

    # Tab-Titel definieren
    tab_titles = ['EKG-Verzeichnis', 'CSV-Analyse']

    # Tabs erstellen
    tabs = st.tabs(tab_titles)

    # Inhalt für jeden Tab hinzufügen
    with tabs[0]:
        tab1_content()

    with tabs[1]:
        tab2_content()

if __name__ == "__main__":
    main()

# Session State wird leer angelegt, solange er noch nicht existiert

# Nutzen Sie ihre neue Liste anstelle der hard-gecodeten Lösung
