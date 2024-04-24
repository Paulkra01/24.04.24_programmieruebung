import streamlit as st
import read_data


st.write("# EKG APP")
st.write("## Versuchsperson auswählen")


# Session State wird leer angelegt, solange er noch nicht existiert
if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'

person_names = read_data.get_person_list()


st.session_state.current_user = st.selectbox('Versuchsperson', options = person_names, key="sbVersuchsperson")

st.write("Der Name ist: ", st.session_state.current_user)