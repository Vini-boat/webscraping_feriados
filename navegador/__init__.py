from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

_service = Service(ChromeDriverManager().install())
_chrome_options = Options()
# _chrome_options.add_argument("--headless")  # Executa o navegador em modo headless (sem interface gráfica)
# Iniciar o navegador
driver = webdriver.Chrome(service=_service,options=_chrome_options)