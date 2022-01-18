from pandas.core.arrays.categorical import contains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
import os
import io
import re
from pathlib import Path
start_time = time.time()



class MyScraper:
    def wait(self, mess='', sec=5):
        print(mess)
        for i in range(1, sec+1, 1):
            print(f'{i} ', end='', flush=True)
            time.sleep(1)
    def test(self):
        print('---testing---')


class ScraperLog:
    def __init__(self, log_path):
        self.log_path = log_path
        if not os.path.exists(log_path):
            with open(log_path, "w") as f:
                f.write('')    
        self.time_now = time.strftime("%a, %d %b %Y %H:%M:%S")
        self.current_file = str(Path(__file__).absolute())
    def line_prepender(self, filename, line):
        with io.open(filename, 'r+', encoding='utf-8') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(line + content)
    def write(self, line):
        self.line_prepender(log_path, line)    
        
        
        
if __name__ == '__main__':
    driver_path = "D:\ChromeDriver\chromedriver_ver96.exe"
    driver = webdriver.Chrome(driver_path)
    scraper = MyScraper()
    
    
    log_path = r'D:\Python\django\ARA\SpiderSelenium\log.txt'
    log = ScraperLog(log_path)
    
    
    homepage = f'https://www.amazon.com/Starbucks-Coffee-Frappuccino-13-7oz-Bottles/product-reviews/B08T7X9S9Z/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&pageNumber=1&filterByStar=five_star&sortBy=recent'
    driver.get(homepage)
    
    
    scraper.wait(sec=3)

        
    review_count_css_selector = '#filter-info-section > div.a-row.a-spacing-base.a-size-base > span'
    review_count_str = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, review_count_css_selector))).text
    review_count = re.findall(r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?(?!\d)', review_count_str)[1]
    print(f'--- review_count = {review_count}')
    
    
    ratings_strlist = []
    review_titles_strlist = []
    review_bodies_strlist = []
    # int(review_count)
    for i in range(1, int(review_count), 1):
        templist = []
        most_recent_five_star_reviews_page = f'https://www.amazon.com/Starbucks-Coffee-Frappuccino-13-7oz-Bottles/product-reviews/B08T7X9S9Z/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&pageNumber={i}&filterByStar=five_star&sortBy=recent'
        driver.get(most_recent_five_star_reviews_page)
        print('--- PAGE = ' + driver.current_url)
        scraper.wait(sec=2)
        
        
        review_titles = driver.find_elements_by_css_selector("*[data-hook='review-title']")
        for x in review_titles:
            templist.append(x.text)
        del templist[0:2]
        review_titles_strlist = review_titles_strlist + templist
        print(review_titles_strlist)
        
                
        review_bodies = driver.find_elements_by_css_selector("*[data-hook='review-body']")
        for x in review_bodies:
            if 'five_star' in driver.current_url:
                ratings_strlist.append(5)
            review_bodies_strlist.append(x.text)
        print(review_bodies_strlist)
        log.write(f'page {i}' + ' ' + driver.current_url + ' ' + log.current_file + ' ' + log.time_now + '\n')
        
    
    
    df = pd.DataFrame({'rating':ratings_strlist, 'title':review_titles_strlist, 'review':review_bodies_strlist})
    df.to_csv(r'D:\Python\django\ARA\SpiderSelenium\canned_coffee.csv', columns=None, index=False, header=True, encoding='utf-8-sig', sep=',', decimal='.') 
    driver.quit()
    print("--- %s seconds ---" % (time.time() - start_time))