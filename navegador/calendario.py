from dataclasses import dataclass
from enum import Enum
from typing import List
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException

from navegador import driver
_ENDPOINT = "https://www.calendario.com.br/"

class EstadoValido(Enum):
    RS = "rs"
    SC = "sc"

def get_datas_feriados_municipais(cidade:str,estado:str) -> List[str]:
    pass

def get_feriados_por_url(url:str) -> List[str]:
    driver.get(url)
    frame = driver.find_element(By.ID, "calendar_frame")     
    driver.switch_to.frame(frame)
    try:
        elements = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH, "//td[contains(@class,'feriado_municipal')]/div")))
    except TimeoutException:
        return []
    return [element.get_attribute("id")[4:] for element in elements]

def _get_elementos_cidades(estado:EstadoValido) -> List[WebElement]:
    url = f"{_ENDPOINT}feriados-estado-{estado}.php"
    driver.get(url)
    return WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@id='div_outras_cidades']/table/tbody/tr/td/a")))

def get_cidades(estado:EstadoValido) -> List[str]:
    return [element.text for element in _get_elementos_cidades(estado)]

def get_urls_cidades(estado:EstadoValido) -> List[str]:
    return [element.get_attribute("href") for element in _get_elementos_cidades(estado)]

@dataclass
class Cidade:
    nome: str
    url: str

def get_cidades_e_url(estado:EstadoValido) -> List[Cidade]:
    return [Cidade(element.text, element.get_attribute("href")) for element in _get_elementos_cidades(estado)]