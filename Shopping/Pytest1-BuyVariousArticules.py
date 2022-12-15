#importamos el webdriver de selenium (Se debe instalar el interprete selenium previamente)
import logging
import os
from importlib.resources import path
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time
load_dotenv()  # take environment variables from .env.

try:

    #Seteamos donde se encuentra nuestro driver predeterminado con el que trabajara webdriver
    #PATH = "C:\Program Files (x86)\chromedriver.exe"(DEPRECADO)
    #driver = webdriver.Chrome(PATH)(DEPRECADO)

    # ----- Webdriver configuration -----
    if (os.environ["IS_JENKINS"] == "True"):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # -----------------------------------

    #Seteamos la URL a la que se correra la prueba
    driver.get(os.environ["HOST"])

    #Los time.sleep() agregados es para que vayan viendo el fluejo de ingreso de usuario 
    #y contraseña ya que sino las acciones pasaran en milisegundos y no podran oportunidad 
    #de ver el flujo de forma humana sin embargo esto se elimina de cara a pruebas reales por performance de las mismas

    #Testeamos la presencia de los elementos actuales que se  presentan en la pagina web
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]")))
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]")))
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[1]")))
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[2]")))
   
   
    #Hacemos login en la pagina con las credenciales que se muestran en login page en el footer de la misma
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input"))).send_keys("standard_user")
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[2]/input"))).send_keys("secret_sauce")
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/form/input"))).click()
    
    #Empezamos agregar productos al carro de compras verifiando a sus vez las propiedades de dicho articulo como nombre, description y precio
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#item_4_img_link > img"))).click()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/div[1]")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/div[2]")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/div[3]")))
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/button"))).click()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/button"))).click()
    time.sleep(2)


    #Agregamos un segundo articulo
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#item_0_img_link > img"))).click()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/div[1]")))
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/div[2]")))
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/div[3]")))
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/button"))).click()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/button"))).click()
    time.sleep(2)

    #Agregamos un tercer articulo
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#item_1_img_link > img"))).click()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/div[1]")))
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/div[2]")))
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/div[3]")))
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/button"))).click()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/button"))).click()
    time.sleep(2)

    #Vemos los articulos que se agregaron al carrito para proceder con la compra
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a"))).click()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/span")))
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]")))
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div[3]")))
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div[4]")))
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div[5]")))
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/button[1]")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/button[2]"))).click()
    time.sleep(2)

    #Avanzamos con la compra y completamos el checkout process en la checkout page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/span")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input"))).send_keys("Martin Test")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/input"))).send_keys("Lee Test")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/input"))).send_keys("1m23m2")
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[2]/input"))).click()
    time.sleep(2)

    #Revisamos el resumen de nuestra compra o el overview page (En este caso deje todos los elementos como clickeables con click para que fuera bajando conforme los datos mostrado en el webDriver)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/span")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div[1]"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div[2]"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div[3]"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div[4]"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div[5]"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div[6]"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div[7]"))).click()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div[8]/button[2]"))).click()
    time.sleep(2)
    
    #Verificamos el Status final de la compra o thank you page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/span")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/h2"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout_complete_container > img"))).click()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/button"))).click()
    time.sleep(2)

    #Hacemos Logout una vez ingresamos a la home view despues del login
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/button"))).click()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/nav/a[3]"))).click()
    time.sleep(2)
   
    driver.close
    logging.info("PyTest - BuyVariousArticules - Finalizo satisfactoriamente")

except: 
    logging.error("PyTest - BuyVariousArticules - Fallo")