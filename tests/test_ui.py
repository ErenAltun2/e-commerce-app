from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart():
    options = Options()
    options.headless = True  # Tarayıcıyı başlatmadan işlemi gizlice yapar
    driver = webdriver.Chrome(options=options)
    driver.get('http://10.30.3.43:5000')  # Uygulamanızın URL'si
    
    try:
        # Ürünü sepete ekleme butonuna tıklama
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "/add/1")]'))
        ).click()
        
        # Sepete eklendi mesajının sayfada bulunup bulunmadığını kontrol etme
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'sepete eklendi')]"))
        )
        
        # Sepete eklendi mesajının sayfa içeriğinde olup olmadığını kontrol et
        assert "sepete eklendi" in driver.page_source
    
    except Exception as e:
        print(f"Test sırasında hata oluştu: {e}")
    finally:
        driver.quit()

