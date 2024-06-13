from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from navegador import driver
from navegador.calendario import _ENDPOINT as ENDPOINT





def get_cidades(driver: webdriver, url_estado:str) -> List[str]:
    pass


cidades = ["agudo","montenegro","canoas","lages"]
estado = "rs"
ano = "2024"
for cidade in cidades:
    url = f"{ENDPOINT}feriados-{cidade}-{estado}.php?ano={ano}"
    print(f"{url=}")
    driver.get(url)
    frame = driver.find_element(By.ID, "calendar_frame")
    driver.switch_to.frame(frame)
    elements = WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.XPATH, "//td[contains(@class,'feriado_municipal')]/div")))

    with open("feriados_2024.html", "a", encoding="utf-8") as file:
        for element in elements:
            id = element.get_attribute("id")
            date = id[4:]
            print(f"{cidade} {date=}")
            file.write(f"{cidade};{date}\n")
    
driver.quit()

