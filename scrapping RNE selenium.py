from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

url='http://inal.sifega.anmat.gov.ar/consultadeRegistro/'
opts = Options()
opts.add_argument ("user-agent=Mozilla/5.0") ## ver detalle de esto
driver = webdriver.Chrome('./chromedriver', options=opts)
driver.get(url)

actividad = 1
seleccion = driver.find_element(By.XPATH,'//select[@name="tipo"]')
seleccion.send_keys(actividad)

boton = driver.find_element(By.XPATH,'//button/type="submit"')
boton.click()
