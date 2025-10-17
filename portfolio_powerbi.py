import streamlit as st
import base64
import os

# -------------------------------------------------------------
# CONFIGURACIÓN GENERAL DE LA PÁGINA
# -------------------------------------------------------------
st.set_page_config(
    page_title="Portfolio Power BI - Matías Chamorro",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------------------
# FUNCIÓN AUXILIAR: CONVERTIR IMAGEN LOCAL A BASE64
# -------------------------------------------------------------
def get_base64(path):
    """Convierte una imagen local a base64 para insertarla en HTML."""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# -------------------------------------------------------------
# FUNCIÓN: MOSTRAR UN PROYECTO EN DOS COLUMNAS
# -------------------------------------------------------------
def mostrar_proyecto(nombre, descripcion, imagen_local, link):
    col1, col2 = st.columns([1, 1.3], vertical_alignment="center")

    with col1:
        if os.path.exists(imagen_local):
            img_base64 = get_base64(imagen_local)
            st.markdown(f"""
            <div style="text-align:center;">
                <a href="{link}" target="_blank" style="text-decoration:none;">
                    <img src="data:image/png;base64,{img_base64}"
                         style="
                            width:100%;
                            height:auto;
                            aspect-ratio:1920/1080;
                            border-radius:15px;
                            box-shadow:0px 2px 10px rgba(0,0,0,0.25);
                            transition:transform 0.2s ease-in-out;
                         "
                         onmouseover="this.style.transform='scale(1.02)'"
                         onmouseout="this.style.transform='scale(1)'">
                </a>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning(f"No se encontró la imagen: {imagen_local}")

    with col2:
        st.markdown(f"""
        ### {nombre}

        {descripcion}
        """)
    st.write("---")

# -------------------------------------------------------------
# CABECERA DEL PORTFOLIO
# -------------------------------------------------------------
st.markdown("""
# Hola, soy analista de datos y desarrollador de Power BI

Tras años de experiencia transformando datos en valor, te invito a recorrer algunos de mis proyectos destacados.
""")

st.write("---")
st.subheader("Proyectos Power BI")

# -------------------------------------------------------------
# LISTA DE PROYECTOS
# -------------------------------------------------------------
proyectos = [
    {
        "nombre": "Proy_Dash_001",
        "imagen": "img/portada_proyecto_001.png",
        "link": "https://app.powerbi.com/view?r=eyJrIjoiZWM0OGViZDQtNWQyZS00YmRlLWJmZmYtOTAxZDgwNDQ5ZDFkIiwidCI6IjkxZjVjYjg5LTUyZmUtNDdhYi05MDVmLTRlMzU4ODZmNWE1NyIsImMiOjR9",
        "descripcion": """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec justo at enim mattis sodales. 
        Integer viverra malesuada ligula, nec placerat erat malesuada in. Suspendisse id risus vel libero tincidunt dignissim. 
        Cras euismod, nisi nec fringilla tincidunt, justo purus imperdiet justo, vitae pulvinar odio orci nec justo."""
    },
    {
        "nombre": "Proy_Dash_002",
        "imagen": "img/portada_proyecto_002.png",
        "link": "https://app.powerbi.com/view?r=eyJrIjoiMGNhZGJmYTUtZDA0Mi00MDM5LWI4NTMtMWIyYTE4ZDhiODI1IiwidCI6IjkxZjVjYjg5LTUyZmUtNDdhYi05MDVmLTRlMzU4ODZmNWE1NyIsImMiOjR9",
        "descripcion": """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec justo at enim mattis sodales. 
        Integer viverra malesuada ligula, nec placerat erat malesuada in. Suspendisse id risus vel libero tincidunt dignissim. 
        Cras euismod, nisi nec fringilla tincidunt, justo purus imperdiet justo, vitae pulvinar odio orci nec justo."""
    },
    {
        "nombre": "Proy_TCon_001",
        "imagen": "img/portada_proyecto_003.png",
        "link": "https://app.powerbi.com/view?r=eyJrIjoiNDA5NmQzY2UtYTY3ZS00ZDFmLWJkOTYtMTMyOTM5MGYyOTlmIiwidCI6IjkxZjVjYjg5LTUyZmUtNDdhYi05MDVmLTRlMzU4ODZmNWE1NyIsImMiOjR9",
        "descripcion": """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec justo at enim mattis sodales. 
        Integer viverra malesuada ligula, nec placerat erat malesuada in. Suspendisse id risus vel libero tincidunt dignissim. 
        Cras euismod, nisi nec fringilla tincidunt, justo purus imperdiet justo, vitae pulvinar odio orci nec justo."""
    },
    {
        "nombre": "Proy_TCon_002",
        "imagen": "img/portada_proyecto_004.png",
        "link": "https://app.powerbi.com/view?r=eyJrIjoiZTZlYWM2YzUtOTg1MC00ZjU0LTg0YmUtZTE3MzQ0Y2Y3YmFlIiwidCI6IjkxZjVjYjg5LTUyZmUtNDdhYi05MDVmLTRlMzU4ODZmNWE1NyIsImMiOjR9",
        "descripcion": """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec justo at enim mattis sodales. 
        Integer viverra malesuada ligula, nec placerat erat malesuada in. Suspendisse id risus vel libero tincidunt dignissim. 
        Cras euismod, nisi nec fringilla tincidunt, justo purus imperdiet justo, vitae pulvinar odio orci nec justo."""
    },
]

# -------------------------------------------------------------
# MOSTRAR LOS PROYECTOS
# -------------------------------------------------------------
for p in proyectos:
    mostrar_proyecto(p["nombre"], p["descripcion"], p["imagen"], p["link"])
