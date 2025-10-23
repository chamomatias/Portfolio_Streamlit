import streamlit as st
import base64
import os
from languages import language_dict, tools

# -------------------------------------------------------------
# CONFIGURACIÓN GENERAL DE LA PÁGINA
# -------------------------------------------------------------
st.set_page_config(
    page_title=language_dict["title"]["en"],
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------------------
# CARGAR ESTILOS CSS
# -------------------------------------------------------------
if os.path.exists("styles.css"):
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.warning("No se encontró el archivo styles.css")

# Color uniforme para todas las fuentes
texto_color = "#F5F5F5"

# -------------------------------------------------------------
# FUNCIÓN AUXILIAR: CONVERTIR IMAGEN LOCAL A BASE64
# -------------------------------------------------------------
def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# -------------------------------------------------------------
# FUNCIÓN: MOSTRAR PROYECTO
# -------------------------------------------------------------
def mostrar_proyecto_tarjeta(desc, imagen_local, link):
    if os.path.exists(imagen_local):
        img_base64 = get_base64(imagen_local)
        st.markdown(f"""
        <div style="
            display:flex; 
            flex-direction:row; 
            align-items:center; 
            justify-content:start; 
            margin-bottom:30px;
            color:{texto_color};
        ">
            <a href="{link}" target="_blank" style="text-decoration:none; width:45%;">
                <img class="proyecto-img" src="data:image/png;base64,{img_base64}" style="width:100%; height:auto; aspect-ratio:16/9;">
            </a>
            <div style="
                margin-left:20px; 
                width:55%; 
                font-size:16px; 
                line-height:1.5;
                color:{texto_color};
            ">
                {desc}
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning(f"No se encontró la imagen: {imagen_local}")

# -------------------------------------------------------------
# SELECCIÓN DE IDIOMA
# -------------------------------------------------------------
if "lang" not in st.session_state:
    st.session_state["lang"] = "en"

col1, col2 = st.sidebar.columns(2)
with col1:
    if st.button("English"):
        st.session_state["lang"] = "en"
with col2:
    if st.button("Español"):
        st.session_state["lang"] = "es"

lang = st.session_state["lang"]

# -------------------------------------------------------------
# HEADER
# -------------------------------------------------------------
st.markdown(f"# {language_dict['title'][lang]}", unsafe_allow_html=True)
st.markdown(f"<div style='color:{texto_color};'>{language_dict['header'][lang]}</div>", unsafe_allow_html=True)
st.write("---")

# -------------------------------------------------------------
# PROYECTOS
# -------------------------------------------------------------
for p in language_dict["projects"]:
    mostrar_proyecto_tarjeta(p["description"][lang], p["image"], p["link"])

# -------------------------------------------------------------
# HERRAMIENTAS
# -------------------------------------------------------------
st.write("---")
st.markdown(f"<h2 style='text-align:center; color:{texto_color};'>{language_dict['tools_header'][lang]}</h2>", unsafe_allow_html=True)

col_izq, col1, col2, col3, col4, col_der = st.columns([3,1,1,1,1,3])

for i, col in enumerate([col1, col2, col3, col4]):
    with col:
        tool = tools[i]
        if os.path.exists(tool["path"]):
            img_base64 = get_base64(tool["path"])
            st.markdown(f"""
            <div style="text-align:center; color:{texto_color};">
                <h4 style="color:{texto_color};">{tool['name']}</h4>
                <img src="data:image/png;base64,{img_base64}" style="width:100px; height:auto;">
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning(f"No se encontró la imagen: {tool['path']}")

# -------------------------------------------------------------
# FOOTER CONTACTO
# -------------------------------------------------------------
st.write("---")
linkedin_logo_path = "img/logo_linkedin.png"
linkedin_url = "https://www.linkedin.com/in/m-chamorro/"

# Información de contacto
email = "chamomatias@gmail.com"
telefono = "+54 9 2657 23-2257"

if os.path.exists(linkedin_logo_path):
    linkedin_base64 = get_base64(linkedin_logo_path)
    st.markdown(f"""
    <div style="text-align:center; margin-top:10px; color:{texto_color};">
        <p style="font-size:16px; font-weight:500; margin-bottom:8px; color:{texto_color};">{language_dict['contact'][lang]}</p>
        <a href="{linkedin_url}" target="_blank">
            <img class="linkedin-logo" src="data:image/png;base64,{linkedin_base64}" style="width:40px; height:auto;">
        </a>
        <p style="font-size:14px; margin-top:8px; color:{texto_color};">Correo: {email} | Teléfono: {telefono}</p>
        <p style="font-size:14px; margin-top:8px; color:{texto_color};">© 2025 Matías Chamorro</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.warning("No se encontró la imagen del logo de LinkedIn.")
