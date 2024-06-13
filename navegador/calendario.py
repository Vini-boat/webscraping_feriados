import datetime
from enum import Enum
from typing import List
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from navegador import driver
_ENDPOINT = "https://www.calendario.com.br/"

class EstadoValido(Enum):
    RS = "rs"
    SC = "sc"

def get_datas_feriados_municipais(cidade:str,estado:str) -> List[str]:
    pass

def get_feriados_por_url(url:str) -> List[str]:
    pass

def get_cidades(estado:EstadoValido) -> List[str]:
    pass

def get_urls_cidades(estado:EstadoValido) -> List[str]:
    url = f"{_ENDPOINT}-feriados-estado-{estado}.php?ano={datetime.now().year}"
    driver.get(url)
    elements = WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.XPATH, "///div[@id='div_outras_cidades']/table/tbody/tr/td/a")))
    # return map(,)
