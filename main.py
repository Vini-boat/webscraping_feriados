from navegador.calendario import get_cidades_e_url
from navegador.calendario import get_feriados_por_url





# def get_cidades(driver: webdriver, url_estado:str) -> List[str]:
#     pass


# cidades = ["agudo","montenegro","canoas","lages"]
# estado = "rs"
# ano = "2024"
# for cidade in cidades:
#     url = f"{ENDPOINT}feriados-{cidade}-{estado}.php"
#     print(f"{url=}")
#     driver.get(url)
#     frame = driver.find_element(By.ID, "calendar_frame")
#     driver.switch_to.frame(frame)
#     elements = WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.XPATH, "//td[contains(@class,'feriado_municipal')]/div")))

#     with open("feriados_2024.html", "a", encoding="utf-8") as file:
#         file.write(f"\n{cidade}")
#         for element in elements:
#             id = element.get_attribute("id")
#             date = id[4:]
#             print(f"{cidade} {date=}")
#             file.write(f";{date}")


if __name__ == "__main__":
    for estado in ["rs","sc"]:
        cidades = get_cidades_e_url(estado)
        for cidade in cidades:
            feriados = get_feriados_por_url(cidade.url)
            print(cidade, f"{feriados=}")
            with open("feriados_2024.html", "a", encoding="utf-8") as file:
                file.write(f"{cidade.nome};{feriados}\n")