from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pyautogui
import time


options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)


driver.get("https://humanbenchmark.com/tests/typing ")


try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "letters"))
    )

   
    time.sleep(3) 
    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")

    container = soup.find("div", class_="letters")
    if not container:
        print("Typing container not found!")
        exit()

    words = container.find_all("span")
    text = ''.join([word.text for word in words])

    if not text:
        print("No text found to type.")
        exit()

    print("Typing:", text)
    

    time.sleep(0.5)

    
    pyautogui.typewrite(text, interval=0)

    time.sleep(5)  

except Exception as e:
    print("An error occurred:")