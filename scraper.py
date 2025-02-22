from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configurar Selenium en modo headless (sin abrir ventana)
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

    # Extraer el contenido de la sección
    patch_content = patch_section.text.strip()
    
    print("\n🔹 **Contenido de PatchNotes-body:** 🔹\n")
    print(patch_content)

except Exception as e:
    print(f"⚠ Error al obtener los Patch Notes: {e}")

# Cerrar el navegador
driver.quit()
