from selenium import webdriver
from app.segundoExercicio.letraMusica import PaginaLetras
import time


def test_buscar_letra():
    service = webdriver.ChromeService()
    navegador = webdriver.Chrome(service=service)
    pagina = PaginaLetras(navegador)
    pagina.carregarUrl()
    pagina.inserirLetra()
    pagina.pegarLetra()