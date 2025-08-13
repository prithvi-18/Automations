import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    print("\n[Setup] Opening browser in headless mode...")

    options = Options()
    options.add_argument("--headless")                  # Run without GUI
    options.add_argument("--disable-gpu")               # Stability for CI
    options.add_argument("--window-size=1920,1080")     # Full HD viewport
    options.add_argument("--no-sandbox")                # CI Linux fix
    options.add_argument("--disable-dev-shm-usage")     # Prevent memory issues

    # ✅ Correct way to initialize Chrome with WebDriverManager in Selenium 4
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver  # this hands control to the test
    print("\n[Teardown] Closing browser...")
    driver.quit()