def test_open_google(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    print("\n[Test] Google page title is correct.")

def test_open_saucedemo(driver):
    driver.get("https://www.saucedemo.com/")
    assert "Swag Labs" in driver.title
    print("\n[Test] SauceDemo page title is correct.")
