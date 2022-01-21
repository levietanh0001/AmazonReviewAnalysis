from logging import logProcesses
from select import select
from pandas.core.arrays.categorical import contains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time
import os
import io
import re
from pathlib import Path




class MyTimer():
    def start_timer(self):
        self.start_time = time.time()
    def end_timer(self):
        print("--- %s seconds ---" % (time.time() - self.start_time))
        
        

class MyScraper:
    def driver(self):
        # self.driver = webdriver.Chrome(driver_path)
        s=Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)
        
        
        
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        return self.driver
    def wait(self, mess='', sec=5):
        print(mess)
        for i in range(1, sec+1, 1):
            print(f'{i} ', end='', flush=True)
            time.sleep(1)
    def set_csv_path(self, csv_path):
        self.csv_path = csv_path
    def set_log_path(self, log_path):
        self.log_path = log_path
        if not os.path.exists(log_path):
            with open(log_path, "w") as f:
                f.write('')    
        self.time_now = time.strftime("%a, %d %b %Y %H:%M:%S")
        self.current_file = str(Path(__file__).absolute())
    def set_homepage(self, homepage):
        self.homepage = homepage
    def set_item_count_per_page(self, item_count_per_page):
        self.item_count_per_page = item_count_per_page
    def log(self, line):
        with io.open(self.log_path, 'r+', encoding='utf-8') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(line + content)
    def find_element(self, driver, flag, selector, ret='object'):
        if ret=='object':
            if flag=='css_selector':
                return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
            elif flag=='xpath':
                return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, selector)))
            elif flag=='class_name':
                return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, selector)))
            elif flag=='id':
                return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, selector)))
            elif flag=='link_text':
                return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, selector)))
            elif flag=='tag_name':
                return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, selector)))
            elif flag=='name':
                return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, selector)))
            # return WebDriverWait(driver, 10).until(EC.presence_of_element_located(flag, selector))
        elif ret=="text":
            if flag=='css_selector':
                return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector))).text
            elif flag=='xpath':
                return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, selector))).text
            elif flag=='class_name':
                return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, selector))).text
            elif flag=='id':
                return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, selector))).text
            elif flag=='link_text':
                return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, selector))).text
            elif flag=='tag_name':
                return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, selector))).text
            elif flag=='name':
                return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, selector))).text
    def find_elements(self, driver, flag, selector, ret='object'):
        if ret=='object':
            if flag=='css_selector':
                return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
            elif flag=='xpath':
                return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, selector)))
            elif flag=='class_name':
                return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, selector)))
            elif flag=='id':
                return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, selector)))
            elif flag=='link_text':
                return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.LINK_TEXT, selector)))
            elif flag=='tag_name':
                return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, selector)))
            elif flag=='name':
                return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.NAME, selector)))
            # return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(flag, selector))
        elif ret=="text":
            if flag=='css_selector':
                return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))).text
            elif flag=='xpath':
                return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, selector))).text
            elif flag=='class_name':
                return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, selector))).text
            elif flag=='id':
                return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, selector))).text
            elif flag=='link_text':
                return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.LINK_TEXT, selector))).text
            elif flag=='tag_name':
                return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, selector))).text
            elif flag=='name':
                return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.NAME, selector))).text
    def to_csv(self, data):
        df = pd.DataFrame(data)
        df.to_csv(self.csv_path, columns=None, index=False, header=True, encoding='utf-8-sig', sep=',', decimal='.')
    
        
        
        
        
if __name__ == '__main__':
    t = MyTimer()
    t.start_timer()
    
    
    # driver_path = r"D:/ChromeDriver/chromedriver_ver96.exe"
    log_path = r'./log.txt'
    csv_path = r'./canned_coffee.csv'
    homepage = f'https://www.amazon.com/Starbucks-Coffee-Frappuccino-13-7oz-Bottles/product-reviews/B08T7X9S9Z/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&pageNumber=1&filterByStar=five_star&sortBy=recent'
    s = MyScraper()
    s.set_log_path(log_path)
    s.set_csv_path(csv_path)
    s.set_homepage(homepage)
    s.set_item_count_per_page(10)
    driver = s.driver()
    
    
    
    driver.get(s.homepage)
    s.wait(sec=3)

    
    review_count_css_selector = "#filter-info-section > div.a-row.a-spacing-base.a-size-base"
    review_count_str = WebDriverWait(driver, 10).until(EC.presence_of_element_located( (By.CSS_SELECTOR, review_count_css_selector) )).text
    
    # review_count_str = s.find_element(driver=driver, flag='css_selector', selector=review_count_css_selector, ret='text')
    review_count = re.findall(r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?(?!\d)', review_count_str)[1]
    print(f'--- review_count = {review_count}')
    
    
    ratings_strlist = []
    review_titles_strlist = []
    review_bodies_strlist = []
    # int(review_count)
    to_be_scraped = int(int(review_count)/int(s.item_count_per_page))
    for i in range(1, to_be_scraped, 1):
        print('\n=== 3 ===')
        templist = []
        most_recent_five_star_reviews_page = f'https://www.amazon.com/Starbucks-Coffee-Frappuccino-13-7oz-Bottles/product-reviews/B08T7X9S9Z/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&pageNumber={i}&filterByStar=five_star&sortBy=recent'
        driver.get(most_recent_five_star_reviews_page)
        print('--- PAGE = ' + driver.current_url)
        s.wait(sec=2)
        
        
        review_titles = driver.find_elements_by_css_selector("*[data-hook='review-title']")
        review_titles_selector = "*[data-hook='review-title']"
        # review_titles = s.find_elements(driver, flag='css_selector', selector=review_titles_selector, ret='object')
        for x in review_titles:
            templist.append(x.text)
        del templist[0:2]
        review_titles_strlist = review_titles_strlist + templist
        print(review_titles_strlist)
        
        review_bodies_selector = "*[data-hook='review-body']"  
        # review_bodies = s.find_elements(driver, flag='css_selector', selector=review_bodies_selector, ret='object')
        review_bodies = driver.find_elements_by_css_selector("*[data-hook='review-body']")
        for x in review_bodies:
            if 'five_star' in driver.current_url:
                ratings_strlist.append(5)
            review_bodies_strlist.append(x.text)
        print(review_bodies_strlist)
        s.log(f'page {i}' + ' ' + driver.current_url + ' ' + s.current_file + ' ' + s.time_now + '\n')
        
    
    
    scraped_dict = {'rating':ratings_strlist, 'title':review_titles_strlist, 'review':review_bodies_strlist}
    s.to_csv(data=scraped_dict)
    # df = pd.DataFrame(scraped_dict)
    # df.to_csv(r'D:\Python\django\ARA\SpiderSelenium\canned_coffee.csv', columns=None, index=False, header=True, encoding='utf-8-sig', sep=',', decimal='.') 
    driver.quit()
    t.end_timer()