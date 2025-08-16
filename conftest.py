from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Attach test outcome to the node so fixtures can see pass/fail
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

def _make_driver(headless: bool = True):
    options = Options()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

def pytest_addoption(parser):
    parser.addoption("--headed", action="store_true", help="Run with visible browser")

@pytest.fixture
def driver(request):
    headless = not request.config.getoption("--headed")
    driver = _make_driver(headless=headless)
    yield driver
    # If test failed, save a screenshot before quitting
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        shots = Path("artifacts") / "screenshots"
        shots.mkdir(parents=True, exist_ok=True)
        file = shots / f"{request.node.name}.png"
        driver.save_screenshot(str(file))
        print(f"\n[screenshot] saved to {file}")
    driver.quit()
