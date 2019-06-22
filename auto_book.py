from selenium import webdriver
from time import gmtime, strftime
import pickle
import time
import urllib.request
import urllib
from http.cookiejar import CookieJar
import multiprocessing
from multiprocessing import Pool

# driver = selenium.webdriver.Firefox()
# driver.get("http://www.google.com")
# cookies = pickle.load(open("cookies.pkl", "rb"))
# for cookie in cookies:
#     driver.add_cookie(cookie)

def auto_book(account):
    name_link_mapping = [["cookies_fucong.pkl", "p1=10010568"],
                         ["cookies_liujianbo.pkl", "p1=N1705187E"]]

    driver = webdriver.Chrome() #options=options
    driver.get("https://intu.ntu.edu.sg/_layouts/iNTU/Main.aspx?Page=Home")
    cookies = pickle.load(open(name_link_mapping[account][0], "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://wis.ntu.edu.sg/pls/webexe88/srce_smain_s.srce$sel31_o?{}&p2=&p_info=3BB26".format(name_link_mapping[account][1]))

    while 1:
        print(strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        if strftime("%Y-%m-%d %H:%M:%S", time.localtime()) == '2019-06-22 16:26:00':
            driver.find_element_by_xpath("//input[@value='3BB2BB0628-Jun-20192']").click() #3BB2BB[02][23-Jun-2019][1] [court#][date][time slot#]
            driver.find_element_by_xpath("//input[@value='Confirm']").click() #3BB2BB[02][23-Jun-2019][1] [court#][date][time slot#]
            break
        else:
            print("waiting...")
    return True


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=auto_book, args=(0,))
    p2 = multiprocessing.Process(target=auto_book, args=(1,))
    with Pool(8) as p:
        p.map(auto_book, [0,1])
