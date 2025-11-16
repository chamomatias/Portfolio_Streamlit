# languages.py
# Diccionario bilingüe: inglés (default) y español

# Constantes para nombres de idiomas
LANGUAGES = {
    "ENGLISH": "en",
    "SPANISH": "es"
}

language_dict = {
    "title": {
        LANGUAGES["ENGLISH"]: "Power BI Portfolio - Matías Chamorro",
        LANGUAGES["SPANISH"]: "Portfolio Power BI - Matías Chamorro"
    },
    "header": {
        LANGUAGES["ENGLISH"]: "I develop dashboards focused on simplicity and functionality. Below you'll find some examples of my work.",
        LANGUAGES["SPANISH"]: "Desarrollo dashboards, apunto a que sean simples y funcionales. Debajo te muestro algunos de mis trabajos."
    },
    "tools_header": {
        LANGUAGES["ENGLISH"]: "Additionally, I have experience with the following tools:",
        LANGUAGES["SPANISH"]: "Además, cuento con experiencia en las siguientes herramientas:"
    },
    "contact": {
        LANGUAGES["ENGLISH"]: "Contact me:",
        LANGUAGES["SPANISH"]: "Contáctame:"
    },
    "projects": [
        {
            "title": {
                LANGUAGES["ENGLISH"]: "Approved Purchase Orders",
                LANGUAGES["SPANISH"]: "Órdenes de Compra Aprobadas"
            },
            "image": "img/portada_proyecto_0001.png",
            "link": "https://app.powerbi.com/view?r=eyJrIjoiNjcxYzEwNjgtYWQwMC00OTcyLTliZDMtMGRlZGNlZWZmNDg0IiwidCI6IjkxZjVjYjg5LTUyZmUtNDdhYi05MDVmLTRlMzU4ODZmNWE1NyIsImMiOjR9",
            "description": {
                LANGUAGES["ENGLISH"]: "Comprehensive dashboard tracking approved purchase orders with year-over-year performance analysis. Features real-time monitoring of accumulated amounts (USD 48M), showing a 33.2% decrease compared to previous year. Includes detailed breakdowns by product categories and warehouse distribution, with temporal analysis across months and weeks for strategic procurement insights.",
                LANGUAGES["SPANISH"]: "Dashboard integral de seguimiento de órdenes de compra aprobadas con análisis de desempeño interanual. Monitorea en tiempo real montos acumulados (USD 48M), mostrando una disminución del 33.2% frente al año anterior. Incluye desgloses detallados por categorías de productos y distribución por depósitos, con análisis temporal por meses y semanas para insights estratégicos de compras."
            }
        },
        {
            "title": {
                LANGUAGES["ENGLISH"]: "POs/Items Dashboard",
                LANGUAGES["SPANISH"]: "Tablero de OCs/Items"
            },
            "image": "img/portada_proyecto_0002.png",
            "link": "https://app.powerbi.com/view?r=eyJrIjoiNjA4NzNmMDItZDkxYi00ZDI0LTg0ZTItNGYyYWM1Nzg3YjYxIiwidCI6IjkxZjVjYjg5LTUyZmUtNDdhYi05MDVmLTRlMzU4ODZmNWE1NyIsImMiOjR9",
            "description": {
                LANGUAGES["ENGLISH"]: "This dashboard is designed to analyze the volume, distribution, and temporal behavior of Purchase Orders (POs) and their line items, with the ability to switch between both metrics using the main selector.\n\nThe board allows visualization of the purchasing process performance from three key perspectives:\n\n• By buyer\n\n• By status\n\n• By temporal distribution (months and weeks)",
                LANGUAGES["SPANISH"]: "Este dashboard está diseñado para analizar el volumen, la distribución y el comportamiento temporal de las Órdenes de Compra (OCs) y de sus ítems, con la posibilidad de alternar entre ambas métricas mediante el selector principal.\n\nEl tablero permite visualizar el desempeño del proceso de compras desde tres enfoques clave:\n\n• Por comprador\n\n• Por estado\n\n• Por distribución temporal (meses y semanas)."
            }
        },
        {
            "title": {
                LANGUAGES["ENGLISH"]: "Unloading Operations Analysis",
                LANGUAGES["SPANISH"]: "Análisis de Descargas"
            },
            "image": "img/portada_proyecto_002.png",
            "link": "https://app.powerbi.com/view?r=eyJrIjoiMGNhZGJmYTUtZDA0Mi00MDM5LWI4NTMtMWIyYTE4ZDhiODI1IiwidCI6IjkxZjVjYjg5LTUyZmUtNDdhYi05MDVmLTRlMzU4ODZmNWE1NyIsImMiOjR9",
            "description": {
                LANGUAGES["ENGLISH"]: "Operational dashboard for monitoring gross tons unloaded across multiple time periods with comparative analysis. Tracks 4,585 tons in current period with detailed breakdowns by 20, 30, 90, 100, and 150-day intervals. Features advanced temporal comparisons, delivery date analysis, and performance metrics for logistics optimization and operational efficiency.",
                LANGUAGES["SPANISH"]: "Dashboard operativo para monitoreo de toneladas brutas descargadas en múltiples períodos con análisis comparativo. Realiza seguimiento de 4,585 tons en período actual con desgloses detallados por intervalos de 20, 30, 90, 100 y 150 días. Incluye comparativas temporales avanzadas, análisis de fechas de entrega y métricas de desempeño para optimización logística y eficiencia operativa."
            }
        },
        {
            "title": {
                LANGUAGES["ENGLISH"]: "Production Control Dashboard",
                LANGUAGES["SPANISH"]: "Panel de Control de Producción"
            },
            "image": "img/portada_proyecto_004.png",
            "link": "https://app.powerbi.com/view?r=eyJrIjoiZTZlYWM2YzUtOTg1MC00ZjU0LTg0YmUtZTE3MzQ0Y2Y3YmFlIiwidCI6IjkxZjVjYjg5LTUyZmUtNDdhYi05MDVmLTRlMzU4ODZmNWE1NyIsImMiOjR9",
            "description": {
                LANGUAGES["ENGLISH"]: "Production monitoring dashboard tracking monthly performance metrics with detailed filtering by product lines and time periods. Features comprehensive data visualization for PROD.023 product category across 2025, showing production volumes in thousands with monthly breakdowns. Enables real-time operational oversight and performance analysis for manufacturing processes.",
                LANGUAGES["SPANISH"]: "Dashboard de monitoreo de producción que realiza seguimiento de métricas de desempeño mensual con filtros detallados por líneas de producto y períodos temporales. Incluye visualización integral de datos para categoría de producto PROC.023 durante 2025, mostrando volúmenes de producción en miles con desgloses mensuales. Permite supervisión operativa en tiempo real y análisis de desempeño para procesos de manufactura."
            }
        },
        {
            "title": {
                LANGUAGES["ENGLISH"]: "Shipments Tracking Dashboard",
                LANGUAGES["SPANISH"]: "Dashboard de Seguimiento de Despachos"
            },
            "image": "img/portada_proyecto_003.png",
            "link": "https://app.powerbi.com/view?r=eyJrIjoiNDA5NmQzY2UtYTY3ZS00ZDFmLWJkOTYtMTMyOTM5MGYyOTlmIiwidCI6IjkxZjVjYjg5LTUyZmUtNDdhYi05MDVmLTRlMzU4ODZmNWE1NyIsImMiOjR9",
            "description": {
                LANGUAGES["ENGLISH"]: "Historical shipments analysis dashboard tracking dispatch performance across multiple product lines. Features comparative analysis between July 2023 and June 2023 with variance calculations (+722, -221, +694). Monitors over 300 product references including interference products, providing comprehensive logistics oversight with Top 4.0 rating system and year-over-year comparison capabilities (2023 vs 2022).",
                LANGUAGES["SPANISH"]: "Dashboard de análisis histórico de despachos que realiza seguimiento del desempeño de envíos a través de múltiples líneas de productos. Incluye análisis comparativo entre julio 2023 y junio 2023 con cálculos de variación (+722, -221, +694). Monitorea más de 300 referencias de productos incluyendo productos de interferencia, proporcionando supervisión logística integral con sistema de calificación Top 4.0 y capacidades de comparación interanual (2023 vs 2022)."
            }
        },
        {
            "title": {
                LANGUAGES["ENGLISH"]: "Quality Tracking Dashboard",
                LANGUAGES["SPANISH"]: "Panel de Seguimiento de Calidad"
            },
            "image": "img/portada_proyecto_005.png",
            "link": "https://app.powerbi.com/view?r=eyJrIjoiYTFjNTgxMjUtOWJlZS00ODJjLTlhYmItOGEyOWRjOTdmZGZhIiwidCI6IjkxZjVjYjg5LTUyZmUtNDdhYi05MDVmLTRlMzU4ODZmNWE1NyIsImMiOjR9",
            "description": {
                LANGUAGES["ENGLISH"]: "Quality control dashboard monitoring key product parameters including Humidity, Grade, PH, Gr.Daft, Gr.Quebr., Mat Ex., Starch, and Protein. Features real-time tracking across 2025 with monthly breakdowns and up-to-date records. Provides comprehensive quality assurance metrics for production analysis and compliance monitoring with latest updates as of October 2025.",
                LANGUAGES["SPANISH"]: "Panel de control de calidad que monitorea parámetros clave del producto como Humedad, Grado, PH, Gr.Daft, Gr.Quebr., Mat Ex., Almidón y Proteína. Incluye seguimiento en tiempo real durante 2025 con desgloses mensuales y registros actualizados. Proporciona métricas integrales de aseguramiento de calidad para análisis de producción y monitoreo de cumplimiento con últimas actualizaciones hasta octubre 2025."
            }
        },
        {
            "title": {
                LANGUAGES["ENGLISH"]: "Receipts Monitoring Dashboard",
                LANGUAGES["SPANISH"]: "Dashboard de Monitoreo de Recepciones"
            },
            "image": "img/portada_proyecto_006.png",
            "link": "https://app.powerbi.com/view?r=eyJrIjoiNjc0YWE3YWUtNDZlZC00OWQyLThlNzAtZmI3YzE3M2ExNjhjIiwidCI6IjkxZjVjYjg5LTUyZmUtNDdhYi05MDVmLTRlMzU4ODZmNWE1NyIsImMiOjR9",
            "description": {
                LANGUAGES["ENGLISH"]: "Receipts tracking dashboard designed to monitor incoming goods and materials with comprehensive accumulation analysis. Features monthly receipt tracking with year-over-year comparisons, accumulation indicators, and detailed breakdowns by time periods. Includes historical data visualization and index-based analysis for supply chain monitoring and inventory management optimization.",
                LANGUAGES["SPANISH"]: "Dashboard de seguimiento de recepciones diseñado para monitorear ingresos de bienes y materiales con análisis integral de acumulados. Incluye seguimiento mensual de recepciones con comparativas interanuales, indicadores de acumulación y desgloses detallados por períodos temporales. Cuenta con visualización de datos históricos y análisis basado en índices para monitoreo de cadena de suministro y optimización de gestión de inventarios."
            }
        },
        {
            "title": {
                LANGUAGES["ENGLISH"]: "Tracking System",
                LANGUAGES["SPANISH"]: "Sistema de Seguimiento"
            },
            "image": "img/portada_proyecto_010.png",
            "link": "https://app.powerbi.com/view?r=eyJrIjoiYzUyMDdmNmUtY2Y1Yy00YzY2LWJmZDQtZGIyMTQyYjQ1OTJmIiwidCI6IjkxZjVjYjg5LTUyZmUtNDdhYi05MDVmLTRlMzU4ODZmNWE1NyIsImMiOjR9",
            "description": {
                LANGUAGES["ENGLISH"]: "Interactive requirements management system with dynamic filtering capabilities and custom DAX-powered analytics. Features intuitive data slicers for real-time exploration of requirement statuses, categories, and timelines. Enables comprehensive tracking across multiple requirement types with customizable views and drill-through capabilities for detailed analysis.",
                LANGUAGES["SPANISH"]: "Sistema interactivo de gestión de requisitos con capacidades de filtrado dinámico y análisis personalizados con DAX. Incluye segmentadores de datos intuitivos para exploración en tiempo real de estados, categorías y cronogramas de requisitos. Permite seguimiento integral a través de múltiples tipos de requisitos con vistas personalizables y capacidades de profundización para análisis detallado."
            }
        }
    ]
}

# Herramientas (logos)
tools = [
    {"name": "SQL", "path": "img/logo_sql.png"},
    {"name": "Python", "path": "img/logo_python.png"},
    {"name": "Excel", "path": "img/logo_excel.png"},
    {"name": "Figma", "path": "img/logo_figma.png"},
]

# Función de utilidad para obtener texto
def get_text(key, language="en", project_index=None):
    """
    Obtiene texto traducido del diccionario de idiomas
    
    Args:
        key (str): La clave del texto a obtener
        language (str): Idioma ('en' o 'es')
        project_index (int, optional): Índice del proyecto para textos específicos
    
    Returns:
        str: Texto traducido
    """
    if project_index is not None and "projects" in language_dict:
        return language_dict["projects"][project_index][key][language]
    return language_dict[key][language]

# Función de validación
def validate_language_dict(lang_dict):
    """
    Valida que el diccionario de idiomas tenga la estructura correcta
    
    Args:
        lang_dict (dict): Diccionario a validar
    
    Raises:
        KeyError: Si faltan claves requeridas
        ValueError: Si hay problemas en la estructura de proyectos
    """
    required_keys = ["title", "header", "projects", "tools_header", "contact"]
    for key in required_keys:
        if key not in lang_dict:
            raise KeyError(f"Missing required key: {key}")
    
    for i, project in enumerate(lang_dict["projects"]):
        required_project_keys = ["title", "image", "link", "description"]
        for key in required_project_keys:
            if key not in project:
                raise KeyError(f"Project {i} missing key: {key}")
        
        if "en" not in project["description"] or "es" not in project["description"]:
            raise ValueError(f"Project {i} missing language in description")
        
        if "en" not in project["title"] or "es" not in project["title"]:
            raise ValueError(f"Project {i} missing language in title")

# Validar el diccionario al cargar el módulo
if __name__ != "__main__":
    validate_language_dict(language_dict)