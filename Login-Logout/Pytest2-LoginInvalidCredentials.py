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
    driver.maximize_window()



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
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input"))).send_keys("standard_user1")
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[2]/input"))).send_keys("secret_sauce1")
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/form/input"))).click()

    #Verificamos mensaje de error de credenciales
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3")))
    time.sleep(2)
    
   
    driver.close
    logging.info("PyTest - Login Invalid Credentials - Finalizo satisfactoriamente")

except: 
    logging.error("PyTest - Login Invalid Credentials - Fallo")