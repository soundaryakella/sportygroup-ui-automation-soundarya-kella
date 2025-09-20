import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def chrome_options():
    opts = Options()
    mobile_emulation = {"deviceName": "Pixel 2"}  # Mobile emulator
    opts.add_experimental_option("mobileEmulation", mobile_emulation)
    return opts

@pytest.fixture
def driver(chrome_options):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(8)
    yield driver
    driver.quit()
