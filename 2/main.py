from PIL import Image
import streamlit as st
import read_data



col1, col2 = st.columns(2)

with col1:
   st.header("# EKG APP")
#    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("## Versuchsperson auswählen")
#    st.image("https://static.streamlit.io/examples/dog.jpg")




# Session State wird leer angelegt, solange er noch nicht existiert
if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'

person_names = read_data.get_person_list()


st.session_state.current_user = st.selectbox('Versuchsperson', options = person_names, key="sbVersuchsperson")

st.write("Der Name ist: ", st.session_state.current_user)


# Auslesen des Pfades aus dem zurückgegebenen Dictionary
current_picture_path = st.session_state.current_user["picture_path"]

if 'picture_path' not in st.session_state:
    st.session_state.picture_path = 'data/pictures/none.jpg'

# Suche den Pfad zum Bild, aber nur wenn der Name bekannt ist
if st.session_state.current_user in person_names:
    st.session_state.picture_path = read_data.find_person_data_by_name(st.session_state.current_user)["picture_path"]


# Öffne das Bild und Zeige es an
image = Image.open("../" + st.session_state.picture_path)
st.image(image, caption=st.session_state.current_user)

def callback_function():
    # Logging Message
    print(f"The user has changed to {st.session_state.current_user}")
    # Manuelles wieder ausführen
    #st.rerun()

# Nutzen Sie ihre neue Liste anstelle der hard-gecodeten Lösung
st.session_state.current_user = st.selectbox(
    'Versuchsperson',
    options = person_names, key="sbVersuchsperson", on_change = callback_function)

#commit