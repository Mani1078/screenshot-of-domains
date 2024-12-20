from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# کمک گرفته شده از chatgpt
# مسیر ChromeDriver
driver_path = "D:\\chromedriver\\chromedriver.exe"

# خواندن دامنه‌ها از فایل
with open("alive.txt", 'r') as file:
    domains = [line.strip() for line in file.readlines()]  # حذف فضاهای اضافی

# تنظیمات WebDriver
options = webdriver.ChromeOptions()
options.headless = True  # اجرای بدون نمایش مرورگر


driver = webdriver.Chrome(service=Service(driver_path), options=options)

# ایجاد پوشه برای ذخیره اسکرین‌شات‌ها
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

for domain in domains:
    # اضافه کردن پیشوند http:// در صورت نبود
    if not domain.startswith("http://") and not domain.startswith("https://"):
        domain = "http://" + domain

    try:
        driver.get(domain)

        # صبر کردن برای بارگذاری کامل صفحه
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # تولید نام فایل اسکرین‌شات
        file_name = domain.replace("http://", "").replace("https://", "").replace("/", "_") + ".png"
        screenshot_path = os.path.join("screenshots", file_name)

        # گرفتن اسکرین‌شات
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved for {domain} at {screenshot_path}")

    except Exception as e:
        print(f"Failed to capture screenshot for {domain}: {e}")

driver.quit()
