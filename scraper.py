from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_live_gold_price():
    # Set up headless Chrome (no GUI)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Launch driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    for i in range(10):
      try:
          url = "https://spot.augmont.com/liverates"
          driver.get(url)
          time.sleep(5)  # wait

          # Find price element
          price_element = driver.find_element(By.CSS_SELECTOR, "div#gold-price")
          gold_price = price_element.text.strip()
          #gmum100gm995
          gmum_price_element_low = driver.find_elements(By.CSS_SELECTOR, "span#gmum100gm995-sell")
          low_price = gmum_price_element_low[0].text.strip()
          gmum_price_element_high = driver.find_elements(By.CSS_SELECTOR, "span#gmum100gm995-buy")
          high_price = gmum_price_element_high[0].text.strip()

          print(f"Live Gold Price (USD/oz): {gold_price}")
          print(f"Live Sell Price GMUM100GM995: {low_price}")
          print(f"Live Buy Price GMUM100GM995: {high_price}")


      except Exception as e:
          print("Error while fetching gold price:", e)
    driver.quit()


if __name__ == "__main__":
    get_live_gold_price()
