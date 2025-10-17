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
# ESTILO GLOBAL DE TEMA OSCURO + HOVER EN IMÁGENES
# -------------------------------------------------------------
st.markdown("""
<style>
/* Fondo oscuro */
[data-testid="stAppViewContainer"] {
    background-color: #121212;
}

/* Color de texto claro en toda la app */
body, .css-1d391kg, .css-10trblm, .css-ffhzg2 {
    color: #F5F5F5;
}

/* Legibilidad de markdown */
div.stMarkdown {
    color: #F5F5F5;
    line-height: 1.5;
}

/* Hover suave en portadas de proyectos */
.proyecto-img {
    border-radius:15px;
    overflow:hidden;
    box-shadow:0px 4px 15px rgba(255,255,255,0.15);
    transition: transform 0.05s, box-shadow 0.05s;
}

.proyecto-img:hover {
    transform: scale(1.03);
    box-shadow: 0px 8px 25px rgba(255,255,255,0.25);
}
</style>
""", unsafe_allow_html=True)

# Color uniforme para todas las fuentes
texto_color = "#F5F5F5"

# -------------------------------------------------------------
# FUNCIÓN AUXILIAR: CONVERTIR IMAGEN LOCAL A BASE64
# -------------------------------------------------------------
def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# -------------------------------------------------------------
# FUNCIÓN: MOSTRAR UN PROYECTO COMO TARJETA CON HOVER
# -------------------------------------------------------------
def mostrar_proyecto_tarjeta(descripcion, imagen_local, link):
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
                {descripcion}
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning(f"No se encontró la imagen: {imagen_local}")

# -------------------------------------------------------------
# CABECERA DEL PORTFOLIO
# -------------------------------------------------------------
st.markdown(f"""
# Portfolio de Matías Chamorro
<div style="color:{texto_color};">
Presento dashboards simples, funcionales y escalables. Cada proyecto combina visión estratégica y análisis operativo en un entorno intuitivo, adaptable a distintos contextos y necesidades.
</div>
""", unsafe_allow_html=True)

st.write("---")

# -------------------------------------------------------------
# LISTA DE PROYECTOS
# -------------------------------------------------------------
proyectos = [
    {
        "imagen": "img/portada_proyecto_001.png",
        "link": "https://app.powerbi.com/view?r=eyJrIjoiZWM0OGViZDQtNWQyZS00YmRlLWJmZmYtOTAxZDgwNDQ5ZDFkIiwidCI6IjkxZjVjYjg5LTUyZmUtNDdhYi05MDVmLTRlMzU4ODZmNWE1NyIsImMiOjR9",
        "descripcion": """Dashboards integrados entre jerarquías que permiten explorar la información desde un nivel global hasta los detalles más específicos. Presento los indicadores clave y métricas agregadas, mientras que los niveles intermedios y detallados permiten segmentar y analizar datos por áreas, categorías o periodos. Con funcionalidades de drill-down y filtros interactivos, mis tableros ofrecen una experiencia intuitiva que combina visión estratégica y análisis operativo en un mismo entorno."""
    },
    {
        "imagen": "img/portada_proyecto_002.png",
        "link": "https://app.powerbi.com/view?r=eyJrIjoiMGNhZGJmYTUtZDA0Mi00MDM5LWI4NTMtMWIyYTE4ZDhiODI1IiwidCI6IjkxZjVjYjg5LTUyZmUtNDdhYi05MDVmLTRlMzU4ODZmNWE1NyIsImMiOjR9",
        "descripcion": """Desarrollo medidas DAX desde nivel básico hasta avanzado, incluyendo cálculos de tiempo completos, con lógica escalable y adaptable a distintos contextos."""
    },
    {
        "imagen": "img/portada_proyecto_004.png",
        "link": "https://app.powerbi.com/view?r=eyJrIjoiZTZlYWM2YzUtOTg1MC00ZjU0LTg0YmUtZTE3MzQ0Y2Y3YmFlIiwidCI6IjkxZjVjYjg5LTUyZmUtNDdhYi05MDVmLTRlMzU4ODZmNWE1NyIsImMiOjR9",
        "descripcion": """Tableros simples, funcionales y escalables, con medidas DAX desde nivel básico hasta avanzado, incluyendo cálculos de tiempo completos."""
    },
    {
        "imagen": "img/portada_proyecto_003.png",
        "link": "https://app.powerbi.com/view?r=eyJrIjoiNDA5NmQzY2UtYTY3ZS00ZDFmLWJkOTYtMTMyOTM5MGYyOTlmIiwidCI6IjkxZjVjYjg5LTUyZmUtNDdhYi05MDVmLTRlMzU4ODZmNWE1NyIsImMiOjR9",
        "descripcion": """Tableros a demanda del usuario según requerimientos o necesidades específicas."""
    },
]

# -------------------------------------------------------------
# MOSTRAR LOS PROYECTOS
# -------------------------------------------------------------
for p in proyectos:
    mostrar_proyecto_tarjeta(p["descripcion"], p["imagen"], p["link"])

# -------------------------------------------------------------
# SECCIÓN: OTRAS HERRAMIENTAS
# -------------------------------------------------------------
st.write("---")
st.markdown(f"""
<h2 style="text-align:center; color:{texto_color};">Además:</h2>
<p style="text-align:center; color:{texto_color};">También cuento con experiencia en el uso de las siguientes herramientas:</p>
""", unsafe_allow_html=True)

col_izq, col1, col2, col3, col4, col_der = st.columns([3, 1, 1, 1, 1, 3])

herramientas = [
    {"nombre": "SQL", "ruta": "img/logo_sql.png"},
    {"nombre": "Python", "ruta": "img/logo_python.png"},
    {"nombre": "Excel", "ruta": "img/logo_excel.png"},
    {"nombre": "Figma", "ruta": "img/logo_figma.png"},
]

for i, col in enumerate([col1, col2, col3, col4]):
    with col:
        herramienta = herramientas[i]
        if os.path.exists(herramienta["ruta"]):
            img_base64 = get_base64(herramienta["ruta"])
            st.markdown(f"""
            <div style="text-align:center; color:{texto_color};">
                <h4 style="color:{texto_color};">{herramienta['nombre']}</h4>
                <img src="data:image/png;base64,{img_base64}" 
                     style="width:100px; height:auto;">
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning(f"No se encontró la imagen: {herramienta['ruta']}")

# -------------------------------------------------------------
# FOOTER CON CONTACTO
# -------------------------------------------------------------
st.write("---")
linkedin_logo_path = "img/logo_linkedin.png"
linkedin_url = "https://www.linkedin.com/in/m-chamorro/"

if os.path.exists(linkedin_logo_path):
    linkedin_base64 = get_base64(linkedin_logo_path)
    st.markdown(f"""
    <div style="text-align:center; margin-top:10px; color:{texto_color};">
        <p style="font-size:16px; font-weight:500; margin-bottom:8px; color:{texto_color};">Contactame:</p>
        <a href="{linkedin_url}" target="_blank">
            <img src="data:image/png;base64,{linkedin_base64}" 
                 style="width:40px; height:auto; transition:transform 0.2s;"
                 onmouseover="this.style.transform='scale(1.15)'"
                 onmouseout="this.style.transform='scale(1)'">
        </a>
        <p style="font-size:14px; margin-top:8px; color:{texto_color};">© 2025 Matías Chamorro</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.warning("No se encontró la imagen del logo de LinkedIn.")
