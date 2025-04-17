from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_add_to_cart():
    options = Options()
    options.headless = True  # Tarayıcıyı başlatmadan işlemi gizlice yapar
    driver = webdriver.Chrome(options=options)
    driver.get('http://10.30.3.43:5000')  # Uygulamanızın URL'si
    driver.find_element_by_xpath('//a[contains(@href, "/add/1")]').click()  # Ürün sepete ekleniyor
    time.sleep(1)  # Sayfanın yüklenmesini beklemek için
    assert "sepete eklendi" in driver.page_source  # Sepete eklendi mesajını kontrol et
    driver.quit()
