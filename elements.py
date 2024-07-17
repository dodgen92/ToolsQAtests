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

# Install EdgeDriver using EdgeChromiumDriverManager and set it up with options
edge_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# Open demoqa.com on both Chrome and Edge
chrome_driver.get("https://demoqa.com")
edge_driver.get("https://demoqa.com")

# Click element on Chrome and Edge
WebDriverWait(chrome_driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[1]/div'))).click()
WebDriverWait(edge_driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[1]/div'))).click()

# Click text field input on Chrome and Edge
WebDriverWait(chrome_driver, 20).until(EC.element_to_be_clickable((By.ID, 'item-0'))).click()
WebDriverWait(edge_driver, 20).until(EC.element_to_be_clickable((By.ID, 'item-0'))).click()

# Fill in form fields for TC-01 on Chrome
WebDriverWait(chrome_driver, 20).until(EC.element_to_be_clickable((By.ID, 'userName'))).send_keys("John Doe")
WebDriverWait(chrome_driver, 20).until(EC.element_to_be_clickable((By.ID, 'userEmail'))).send_keys("Testemail@test.com")
WebDriverWait(chrome_driver, 20).until(EC.element_to_be_clickable((By.ID, 'currentAddress'))).send_keys("101 Bleaker Street")
WebDriverWait(chrome_driver, 20).until(EC.element_to_be_clickable((By.ID, 'permanentAddress'))).send_keys("New York")

# Submit the form on Chrome
submit_button_chrome = WebDriverWait(chrome_driver, 20).until(EC.element_to_be_clickable((By.ID, 'submit')))
chrome_driver.execute_script("arguments[0].scrollIntoView();", submit_button_chrome)
submit_button_chrome.click()

# Fill in form fields for TC-01 on Edge
WebDriverWait(edge_driver, 20).until(EC.element_to_be_clickable((By.ID, 'userName'))).send_keys("John Doe")
WebDriverWait(edge_driver, 20).until(EC.element_to_be_clickable((By.ID, 'userEmail'))).send_keys("Testemail@test.com")
WebDriverWait(edge_driver, 20).until(EC.element_to_be_clickable((By.ID, 'currentAddress'))).send_keys("101 Bleaker Street")
WebDriverWait(edge_driver, 20).until(EC.element_to_be_clickable((By.ID, 'permanentAddress'))).send_keys("New York")

# Submit the form on Edge
submit_button_edge = WebDriverWait(edge_driver, 20).until(EC.element_to_be_clickable((By.ID, 'submit')))
edge_driver.execute_script("arguments[0].scrollIntoView();", submit_button_edge)
submit_button_edge.click()

print("TC-01 Passed")

# Wait and close the browsers
time.sleep(5)
chrome_driver.quit()
edge_driver.quit()