from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")

# Install ChromeDriver using ChromeDriverManager and set it up with options
chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
edge_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# Open demoqa.com
chrome_driver.get("https://demoqa.com")
edge_driver.get("https://demoqa.com")


#clicks element page

WebDriverWait(chrome_driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[1]/div' ))).click()
WebDriverWait(edge_driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[1]/div' ))).click()
#clicks radio btn page to begin TC-02
WebDriverWait(chrome_driver, 20).until(EC.element_to_be_clickable((By.ID, 'item-2'))).click()
WebDriverWait(edge_driver, 20).until(EC.element_to_be_clickable((By.ID, 'item-2'))).click()

time.sleep(2)

WebDriverWait(chrome_driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[2]/label'))).click()
WebDriverWait(edge_driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[2]/label'))).click()
time.sleep(1)

WebDriverWait(chrome_driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/label' ))).click()
WebDriverWait(edge_driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/label' ))).click()
time.sleep (1)


print("TC-02 Passed")


chrome_driver.quit()



