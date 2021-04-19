import json 
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

def main():
    profile = webdriver.FirefoxProfile()
    profile.set_preference('dom.webdriver.enabled', False)
    profile.set_preference('useAutomationExtension', False)
    profile.update_preferences()

    base_url = 'https://www.kijiji.ca'

    #with webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile) as driver:
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile)
    driver.get(f'{base_url}/t-login.html')
    
    try:
        WebDriverWait(driver, 10).until(lambda d: d.find_element(By.ID, 'emailOrNickname'))
    except TimeoutException:
        print('Page took too long to load')
        
    driver.find_element(By.ID, 'emailOrNickname').send_keys('jasonmcheong@gmail.com')
    driver.find_element(By.ID, 'password').send_keys('Joker2575!!!')

    time.sleep(1)
    actions = ActionChains(driver)
    actions.send_keys(Keys.RETURN)
    actions.perform()

    # Post new ad
    json_file = open('posts.json')
    data = json.load(json_file)
    json_file.close()
    
    driver.get(f'{base_url}/p-admarkt-post-ad.html?categoryId={category_id}&adTitle=Apple+Magic+Keyboard')
    driver.find_element(By.ID, 'AdTitleForm').send_keys('some json title')
    driver.find_element(By.XPATH, '//*[@id="CategorySuggestion"]/div[1]/ul/li/button').send_keys(Keys.RETURN)

    
    driver.find_element(By.ID, 'pstad-descrptn').send_keys('some json description')


    # Manage active listings
    driver.get(f'{base_url}/m-my-ads/active/1')


    #driver.find_element(By.XPATH, "//button[@type='submit']").send_keys(Keys.RETURN)

    #driver.close()

if __name__ == '__main__':
    main()
