from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 🔑 Replace with your Colab notebook ID
COLAB_URL = "https://colab.research.google.com/drive/17y18dEcsjIfCUgrXS7zvb3tcApfaAYSn#scrollTo=39FyC3mRyf36"
# Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# Agar tumhe browser khula dekhna hai to headless mat lagao
# options.add_argument("--headless")  

driver = webdriver.Chrome(options=options)
driver.get(COLAB_URL)
time.sleep(15)  # wait for notebook to load

# Screenshot le lo (debugging ke liye)
driver.save_screenshot("colab_screen.png")

# Trigger "Run All" (Ctrl+F9)
body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.CONTROL, Keys.F9)

print("✅ Colab notebook triggered")

# Kuch der rukne ke liye (notebook start hone ka time)
time.sleep(10)

# Final screenshot
driver.save_screenshot("colab_screen_after.png")

driver.quit()
