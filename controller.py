from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Apna Colab notebook link daalo
COLAB_URL = "https://colab.research.google.com/drive/17y18dEcsjIfCUgrXS7zvb3tcApfaAYSn#scrollTo=39FyC3mRyf36"

print("🚀 Starting Selenium Colab trigger...")

options = webdriver.ChromeOptions()
# ⚠️ Headless mode hata diya (ab browser dikhai dega)
# options.add_argument("--headless")

options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
print("✅ Chrome WebDriver started")

driver.get(COLAB_URL)
print("🔗 Opened Colab notebook:", COLAB_URL)

# Notebook load hone ka wait
time.sleep(15)

# Trigger Run All (Ctrl+F9)
body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.CONTROL, Keys.F9)
print("✅ Sent Run All (Ctrl+F9) command")

# Thoda rukho taaki tum browser me dekh sako kya ho raha hai
time.sleep(30)

driver.quit()
print("🛑 Browser closed successfully")
