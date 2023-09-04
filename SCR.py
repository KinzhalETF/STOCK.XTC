import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image

# URL of the website to capture
url = "https://example.com"

# Set up Chrome WebDriver
service = Service("/path/to/chromedriver")  # Replace with the path to your chromedriver executable
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no GUI)
options.add_argument("--disable-gpu")  # Disable GPU acceleration

driver = webdriver.Chrome(service=service, options=options)

try:
    # Navigate to the website
    driver.get(url)

    # Give the page some time to load (you can adjust this)
    time.sleep(5)

    # Capture a screenshot
    screenshot = driver.get_screenshot_as_png()

    # Save the screenshot to a file
    screenshot_filename = "website_screenshot.png"
    with open(screenshot_filename, "wb") as file:
        file.write(screenshot)

    print(f"Screenshot saved as {screenshot_filename}")

finally:
    # Close the browser
    driver.quit()
