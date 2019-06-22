from selenium import webdriver
from time import gmtime, strftime
import pickle
import time
import urllib.request
import urllib
from http.cookiejar import CookieJar
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Chang Lei\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(options=options) #options=options
driver.get("https://intu.ntu.edu.sg/_layouts/iNTU/Main.aspx?Page=Home")
driver.get("https://wis.ntu.edu.sg/pls/webexe88/srce_smain_s.srce$sel31_o?p1=N1705187E&p2=&p_info=3BB26")
pickle.dump(driver.get_cookies(), open("cookies_liujianbo.pkl","wb"))
