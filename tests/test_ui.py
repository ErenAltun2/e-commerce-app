from selenium import webdriver
from selenium.webdriver.common.by import By  # By sınıfını ekledik
from selenium.webdriver.chrome.options import Options
import time

def test_add_to_cart():
    options = Options()
    options.headless = True  # Tarayıcıyı başlatmadan işlemi gizlice yapar
    driver = webdriver.Chrome(options=options)
    driver.get('http://10.30.3.43:5000')  # Uygulamanızın URL'si
    
    # find_element_by_xpath yerine find_element ve By kullanıyoruz
    driver.find_element(By.XPATH, '//a[contains(@href, "/add/1")]').click()  # Ürün sepete ekleniyor
    
    time.sleep(1)  # Sayfanın yüklenmesini beklemek için
    
    # Sepete eklendi mesajını kontrol et
    assert "sepete eklendi" in driver.page_source  
    
    driver.quit()
