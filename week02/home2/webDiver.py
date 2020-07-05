from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    def login():
        browser.get('https://shimo.im/login?from=home')
        browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('13680991857')
        browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('o34993652')
        
        time.sleep(1)  
        browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
    # browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
    # btm1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
    # btm1.click()

    # browser.find_element_by_xpath('//*[@id="username"]').send_keys('13680991857')
    # browser.find_element_by_id('password').send_keys('o34993652)
    # time.sleep(1)
    # browser.find_element_by_xpath('//a[contains(@class,"btn-account")]').click()
        cookies = browser.get_cookies() # 获取cookies
        print(cookies)
        time.sleep(3)
except Exception as e:
    print(e)
login()
# finally:    
#     browser.close()
    