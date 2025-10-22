# lenguages.py

# Diccionario de textos por idioma
language_dict = {
    "en": {
        "title": "Power BI Portfolio - Matías Chamorro",
        "intro": "I present dashboards that are simple, functional, and scalable. Each project combines strategic vision and operational analysis in an intuitive environment.",
        "projects": [
            {
                "imagen": "img/portada_proyecto_001.png",
                "link": "https://app.powerbi.com/view?r=...",
                "descripcion": "Integrated dashboards with hierarchical drill-downs, key indicators, and interactive filters."
            },
            {
                "imagen": "img/portada_proyecto_002.png",
                "link": "https://app.powerbi.com/view?r=...",
                "descripcion": "DAX measures from basic to advanced, including full time calculations and scalable logic."
            },
            # más proyectos...
        ],
        "tools_title": "Also:",
        "tools_intro": "I have experience using the following tools:",
        "contact": "Contact me:"
    },
    "es": {
        "title": "Portfolio Power BI - Matías Chamorro",
        "intro": "Presento dashboards simples, funcionales y escalables. Cada proyecto combina visión estratégica y análisis operativo en un entorno intuitivo.",
        "projects": [
            {
                "imagen": "img/portada_proyecto_001.png",
                "link": "https://app.powerbi.com/view?r=...",
                "descripcion": "Dashboards integrados entre jerarquías con drill-down, indicadores clave y filtros interactivos."
            },
            # más proyectos...
        ],
        "tools_title": "Además:",
        "tools_intro": "También cuento con experiencia en el uso de las siguientes herramientas:",
        "contact": "Contactame:"
    }
}

# Lista de herramientas con rutas de imagen
tools = [
    {"en": {"nombre": "SQL", "ruta": "img/logo_sql.png"},
     "es": {"nombre": "SQL", "ruta": "img/logo_sql.png"}},
    {"en": {"nombre": "Python", "ruta": "img/logo_python.png"},
     "es": {"nombre": "Python", "ruta": "img/logo_python.png"}},
    {"en": {"nombre": "Excel", "ruta": "img/logo_excel.png"},
     "es": {"nombre": "Excel", "ruta": "img/logo_excel.png"}},
    {"en": {"nombre": "Figma", "ruta": "img/logo_figma.png"},
     "es": {"nombre": "Figma", "ruta": "img/logo_figma.png"}}
]
