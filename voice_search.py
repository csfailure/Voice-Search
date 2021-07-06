from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import speech_recognition as sr
import sys
import os

def youtube():
    
    PATH = "C:\\Users\\YOUR\\CHROMEDRIVER\\PATH\\chromedriver.exe"
    
    
    string = texttt.split(' ', 1)[1]


    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # OR options.add_argument("--disable-gpu")


    driver = webdriver.Chrome(PATH, options=options)
    driver.get("https://www.youtube.com")
    
    consent = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/span')
    consent.click()
    
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="search"]'))
        )
        element.click()
        element.send_keys(string)
        time.sleep(2)
        element.send_keys(Keys.ENTER)
    finally:
        print("Opening video")  
        
    try:
        video = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '(//a[@id="video-title"])[position()>0]'))
        )
        video.click()
        url = driver.current_url
        driver.close()
        driver1 = webdriver.Chrome(PATH)
        driver1.get(url)
    
        consent1 = driver1.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/span')
        consent1.click()
        
    finally:
        print("Watching {}".format(string))

def soundcloud():
    
    PATH = "C:\\Users\\35569\\Documents\\webdrivers\\chromedriver.exe"
    
    
    string = texttt.split(' ', 1)[1]


    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # OR options.add_argument("--disable-gpu")


    driver = webdriver.Chrome(PATH,options=options)
    driver.get("https://www.soundcloud.com")
    
    cookies = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
    )
    cookies.click()
    
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div/div[2]/div/div[1]/span/span/form/input'))
        )
        element.click()
        time.sleep(1)
        element.send_keys(string)
        time.sleep(1)
        element.send_keys(Keys.ENTER)
    finally:
        print("Opening Song")  
        
    try:
        sound = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div/div[2]/div/div[1]/span/span/form'))
        )
        sound.click()
        url = driver.current_url
        driver.close()
        driver1 = webdriver.Chrome(PATH)
        driver1.get(url)
        
        cookies1 = WebDriverWait(driver1, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
        )
        cookies1.click()
        time.sleep(0.5)
        playsound = driver1.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/div/div/div/ul/li[1]/div/div/div/div[2]/div[1]/div/div/div[1]/a')
        playsound.click()
    finally:
        print("Listening to {}".format(string))

def google():
    
    PATH = "C:\\Users\\35569\\Documents\\webdrivers\\chromedriver.exe"
    
    
    string = texttt.split(' ', 1)[1]


    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # OR options.add_argument("--disable-gpu")


    driver = webdriver.Chrome(PATH)
    driver.get("https://www.google.com")
    accept = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="L2AGLb"]'))
            )
    accept.click()
    
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'))
        )
        element.click()
        #time.sleep(0.5)
        element.send_keys(string)
        time.sleep(1)
        element.send_keys(Keys.ENTER)
    finally:
        print("Searching on Google for {}".format(string)) 
        
    
        
def main():

    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Say Something...")
        audio = r.listen(source)
        
        global texttt
        texttt = r.recognize_google(audio)
        print('Opening : {}'.format(texttt))
        first_word = texttt.split()[0]
        if first_word == "YouTube":
            youtube()
        elif first_word == "SoundCloud":
            soundcloud()
        elif first_word == "Google":
            google()
        else:
            print("You have to mention either Google, Youtube or SoundCloud first to activate")
        
        print("Do you want to search something else? [y][n]")
        yesorno = input()
        
        if yesorno == 'y':
            main()
        else:
            print("Bye")
            sys.exit()
if __name__ == "__main__":
    main()
        

