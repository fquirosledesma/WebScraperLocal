import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configurar Selenium en modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Iniciar WebDriver con WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL de Overwatch Patch Notes
url = "https://overwatch.blizzard.com/es-es/news/patch-notes/live/"
driver.get(url)

try:
    # Esperar a que la sección PatchNotes-body esté presente
    patch_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "PatchNotes-body"))
    )

    # Extraer todos los elementos dentro de PatchNotes-body
    elements = patch_section.find_elements(By.CSS_SELECTOR, "*")  # Captura todos los elementos hijos

    # Crear una lista para almacenar los datos
    data = []

    for elem in elements:
        tag_name = elem.tag_name  # Tipo de elemento (ejemplo: h2, p, div)
        class_name = " ".join(elem.get_attribute("class").split())  # Clases CSS
        text_content = elem.text.strip()  # Contenido del elemento

        # Agregar solo si tiene contenido
        if text_content:
            data.append([tag_name, class_name, text_content])

    # Convertir a un DataFrame de Pandas
    df = pd.DataFrame(data, columns=["Elemento HTML", "Clase CSS", "Contenido"])

    # Guardar en un archivo Excel
    df.to_excel("patch_notes.xlsx", index=False, engine="openpyxl")

    print("\n✅ Contenido exportado correctamente a 'patch_notes.xlsx'.")

except Exception as e:
    print(f"⚠ Error al obtener los Patch Notes: {e}")

# Cerrar el navegador
driver.quit()
