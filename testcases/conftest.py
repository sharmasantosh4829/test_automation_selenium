__maintainer__ = ['santosh.sharma']

import os
import pytest
from utils.logger import Logger
from utils.utils import Utils
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as CHROME_OPTIONS
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FIREFOX_OPTIONS
from webdriver_manager.core.utils import ChromeType
from utils.read_properties import ReadConfig

filename = (__file__.split(os.path.sep)[-1].split(".")[0])
logfile = Utils.get_log_file()
logger = Logger.logger(logfile, logger_name=__name__)


@pytest.fixture(scope="class")
def setup(request, browser):
    if browser == "chrome":
        logger.info("initiating chrome driver")
        options = CHROME_OPTIONS()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install()),
                                  options=options)
    elif browser == "firefox":
        logger.info("initiating firfox driver")
        options = FIREFOX_OPTIONS()
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    base_url = ReadConfig.get_app_url()
    driver.get(base_url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")
