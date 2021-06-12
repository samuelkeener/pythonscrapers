from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import requests
from plyer import notification
from datetime import datetime
from win10toast import ToastNotifier
push = ToastNotifier()

refresh_time=600

bestbuy_link='https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149'
bestbuyTest_link = 'https://www.bestbuy.com/site/marvels-spider-man-miles-morales-standard-launch-edition-playstation-5/6430146.p?skuId=6430146'
gameStop_link='https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5/11108140.html'
gameStopTest_link = 'https://www.gamestop.com/video-games/playstation-5/games/products/marvels-spider-man-miles-morales/11108199.html?rrec=true'
target_link='https://www.target.com/p/playstation-5-console/-/A-81114595'
targetTest_link = 'https://www.target.com/p/dualsense-wireless-controller-for-playstation-5-white-black/-/A-81114477'
newegg_link='https://www.newegg.com/p/N82E16868110298'

class Stockr:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument(" — incognito")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--headless") 
        self.driver = webdriver.Chrome(executable_path='D:/python_programs/chromedriver_win32/chromedriver.exe')
        self.timeout=30
    
    def BestBuy(self, link):
        self.driver.get(link)
        time.sleep(1)
        btn=WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.CLASS_NAME,'add-to-cart-button'))).text
        print(btn)
        avail=btn=='Add to Cart'
        if avail:
            status='In Stock'
        else:
            status = 'Out of Stock'
        time.sleep(2)
        return status

    
    def gameStop(self, link):
        self.driver.get(link)
        time.sleep(20)
        btn=WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.CLASS_NAME,'add-to-cart-buttons'))).text
        try:
            if 'ADD TO CART' in btn:
                status='In Stock'	
            elif 'NOT AVAILABLE' in btn:
                status = 'Out of Stock'	
            else:
                status = 'Something is wrong with your code'
        except:
            print('ERROR...quiting')

        time.sleep(2)
        return status

    
    def target(self, link):
        self.driver.get(link)
        time.sleep(20)
        try:
            btn=WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.XPATH,'//*[@id="viewport"]/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div[1]/div[2]/button')))
            if btn.is_enabled():
                status='In Stock'
        except:
            status = 'Out of Stock'
        time.sleep(2)
        return status

    def newegg(self,link):
        self.driver.get(link)
        try:
            btn=WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ProductBuy"]/div/div[2]')))
            if btn.is_enabled():
                status='In Stock'
        except:
            status = 'Out of Stock'
        return status


def main():
    S=Stockr()

    if (S.target(targetTest_link)=='In Stock'):
        push.show_toast(title="Target works")
    else:
        print('Target doesnt work')
    if (S.BestBuy(bestbuyTest_link)=='In Stock'):
        push.show_toast(title="Bestbuy works")
    else:
        print('BB Doesnt work')
    if (S.gameStop(gameStopTest_link)=='In Stock'):
        push.show_toast(title="Gamestop works")
    else:
        print('Gamestop doesnt work')
    

    while True:
        print('Current Run Time: ',datetime.now())

        if (S.BestBuy(bestbuy_link)=='In Stock'):
            push.show_toast(title="Stock at bestbuy")
        else:
            print('No BestBuy')
        if (S.gameStop(gameStop_link)=='In Stock'):
            push.show_toast(title="Stock at Gamestop")
        else:
            print('No Gamestop')
        if (S.target(target_link)=='In Stock'):
            push.show_toast(title="Stock at Target")
        else:
            print('No Target')
#		if (S.newegg(newegg_link)=='In Stock'):
#			push.show_toast(newegg_link, title="Stock at Newegg")
#		else:
#			print('No Newegg\n\n')                                                                     
        time.sleep(refresh_time)

if __name__ == "__main__":
	main()