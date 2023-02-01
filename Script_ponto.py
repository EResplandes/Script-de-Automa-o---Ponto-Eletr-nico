# Importando Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from datetime import date
import datetime
import time
import pyautogui as pya

# Lista de dias Segunda = 0, Terça = 1, Quarta = 2, Quinta = 3, Sexta = 4, Sabado = 5 e Domingo = 6
DIAS = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-Feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]

# Pegando dia da semana de acordo com a data atual
dia_semana = date.today().weekday()

# Script de Automação
if (dia_semana != 4):

    # Definindo pause 
    pya.PAUSE = 2

    # Usando o navegador ome
    navegador = webdriver.Chrome()

    # Passo 1 -> Abrir sistema de relatório (#url desejada)
    navegador.get("#url desejada")

    #Passo 2 -> Logar no sistema de relatório 
    navegador.find_element('xpath', '//*[@id="lblLogin"]').send_keys("#usuario sistema")
    navegador.find_element('xpath', '//*[@id="lblPass"]').send_keys("#senha sistema")
    navegador.find_element('xpath', '//*[@id="dvREP"]/div/div[3]/a').send_keys(Keys.ENTER)

    # Passo 3 -> Navegar até onde gera relatório
    time.sleep(10)
    pya.click(x=448, y=497)

    navegador.find_element('xpath','//*[@id="menuItem2"]').click()

    # Passo 3 -> Gerar o relatório com a data atual
    navegador.find_element('xpath', '//*[@id="lblDataF"]').click()
    time.sleep(2)
    pya.hotkey("ctrl", 'a')
    pya.hotkey("ctrl", 'c')
    navegador.find_element('xpath', '//*[@id="lblDataI"]').click()
    pya.hotkey("ctrl", 'a')
    pya.hotkey("ctrl", 'v')
    pya.press("Backspace")
    pya.press("Backspace")
    pya.press("Backspace")
    pya.press("Backspace")
    pya.press("Backspace")
    pya.write("0300")
    navegador.find_element('xpath', '//*[@id="communication"]/table/tbody/tr[5]/td/a').click()
    time.sleep(10)

    # Passo 4 -> Abrir sistema de ponto (#url desejada)
    navegador.get("#url desejada")

    # Passo 5 -> Logar no sistema de ponto
    navegador.find_element('xpath', '/html/body/form/input[2]').send_keys("#usuario do sistema")
    navegador.find_element('xpath', '/html/body/form/input[3]').send_keys("#senha do sistema")
    navegador.find_element('xpath', '/html/body/form/button').send_keys(Keys.ENTER)

    # Passo 6 -> Clicar em Gerar relatório
    navegador.find_element('xpath','//*[@id="sidebarMenu"]/div/ul[2]/li[1]/a').click()
    time.sleep(2)

    # Passo 7 -> Selecionar arquivo
    pya.click(x=510, y=597)
    pya.click(x=332, y=56)
    pya.write("Downloads")
    pya.press("enter")
    pya.click(x=300, y=184)
    pya.hotkey("enter")
    time.sleep(2)

    #Passo 8 -> Clicar em "Carregar relatório"
    navegador.find_element('xpath', '/html/body/div/div/main/div[2]/div/form/input[2]').send_keys(Keys.ENTER)

    #Passo 9 -> Finalizando relatório do dia anterior
    pya.click(x=793, y=303)
else:
     # Definindo pause 
    pya.PAUSE = 2

    # Usando o navegador ome
    navegador = webdriver.Chrome()

    # Passo 1 -> Abrir sistema de relatório (#url desejada)
    navegador.get("#url desejada")

    #Passo 2 -> Logar no sistema de relatório 
    navegador.find_element('xpath', '//*[@id="lblLogin"]').send_keys("#usuario do sistema")
    navegador.find_element('xpath', '//*[@id="lblPass"]').send_keys("#senha do sistema")
    navegador.find_element('xpath', '//*[@id="dvREP"]/div/div[3]/a').send_keys(Keys.ENTER)

    # Passo 3 -> Navegar até onde gera relatório
    time.sleep(10)
    pya.click(x=448, y=497)

    navegador.find_element('xpath','//*[@id="menuItem2"]').click()

    # Passo 3 -> Gerar o relatório com a data atual
    navegador.find_element('xpath', '//*[@id="lblDataF"]').click()
    time.sleep(2)
    pya.hotkey("ctrl", 'a')
    pya.hotkey("ctrl", 'c')
    navegador.find_element('xpath', '//*[@id="lblDataI"]').click()
    pya.hotkey("ctrl", 'a')
    pya.hotkey("ctrl", 'v')
    pya.press("Backspace")
    pya.press("Backspace")
    pya.press("Backspace")
    pya.press("Backspace")
    pya.press("Backspace")
    pya.write("0300")
    navegador.find_element('xpath', '//*[@id="communication"]/table/tbody/tr[5]/td/a').click()
    time.sleep(10)

    # Passo 4 -> Abrir sistema de ponto (#url desejada)
    navegador.get("#url desejada")

    # Passo 5 -> Logar no sistema de ponto
    navegador.find_element('xpath', '/html/body/form/input[2]').send_keys("#usuario do sistema")
    navegador.find_element('xpath', '/html/body/form/input[3]').send_keys("#senha do sistema")
    navegador.find_element('xpath', '/html/body/form/button').send_keys(Keys.ENTER)

    # Passo 6 -> Clicar em Gerar relatório
    navegador.find_element('xpath','//*[@id="sidebarMenu"]/div/ul[2]/li[1]/a').click()
    time.sleep(2)

    # Passo 7 -> Selecionar arquivo
    pya.click(x=510, y=597)
    pya.click(x=332, y=56)
    pya.write("Downloads")
    pya.press("enter")
    pya.click(x=300, y=184)
    pya.hotkey("enter")
    time.sleep(2)

    #Passo 8 -> Alterar inicio do expediente
    pya.click(x=582, y=750)
    pya.write("8")
    pya.hotkey("enter")

    # Passo 9 -> Clicar em "Carregar relatório"
    navegador.find_element('xpath', '/html/body/div/div/main/div[2]/div/form/input[2]').send_keys(Keys.ENTER)

    # Passo 10 -> Finalizar relatório
    pya.click(x=793, y=303)
    
