from selenium.webdriver.common.by import By
import time


class PaginaLetras:
    url = 'https://www.letras.mus.br/'
    musica = 'Chove Chuva Jorge Ben Jor '

    def __init__(self, navegador):
        self.navegador = navegador

    def carregarUrl(self):
        self.navegador.get(self.url)
        time.sleep(10)

    def inserirLetra(self):
        self.navegador.find_element(By.XPATH, '//*[@id="main_suggest"]').send_keys(self.musica)
        time.sleep(2)
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/form/div/ul/li[2]/a').click()

    def pegarLetra(self):
        letraMusica = self.navegador.find_elements(By.XPATH, '//*[@id="js-lyric-content"]/article/div[2]/div[2]')

        print("\n")
        for estrofes in letraMusica:
            print(estrofes.text)

