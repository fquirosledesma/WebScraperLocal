from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuración de Selenium (modo sin interfaz gráfica)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Corre en segundo plano
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Ruta al driver de Chrome (Asegúrate de tenerlo instalado)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL de la página de Overwatch Patch Notes
url = "https://overwatch.blizzard.com/es-es/news/patch-notes/live/"

# Abrir la página
driver.get(url)
time.sleep(5)  # Esperar a que cargue el contenido dinámico

# Extraer los títulos de los patch notes
patch_titles = driver.find_elements(By.CSS_SELECTOR, "section.patch-notes-container")

print("Últimos Patch Notes de Overwatch:")

for i, patch in enumerate(patch_notes, 1):
    # Obtener título de la actualización
    title_element = patch.find_element(By.CSS_SELECTOR, "h2")
    title = title_element.text if title_element else "Sin título"

    # Obtener fecha (si está disponible)
    try:
        date_element = patch.find_element(By.CSS_SELECTOR, "p.NewsArticleListItem-published")
        date = date_element.text
    except:
        date = "Fecha no disponible"

    # Obtener contenido (resumen de los cambios)
    try:
        description_element = patch.find_element(By.CSS_SELECTOR, "div.patch-notes-description")
        description = description_element.text.strip()
    except:
        description = "No hay descripción"

    print(f"🔸 {i}. {title}")
    print(f"   📅 Fecha: {date}")
    print(f"   📝 Descripción: {description}\n")
    
# Cerrar el navegador
driver.quit()