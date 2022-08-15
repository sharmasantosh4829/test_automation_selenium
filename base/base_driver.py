__maintainer__ = ['santosh.sharma']

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:

    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        page_len = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHieght);"
        )

    def find_elem(self, locator=By.XPATH, elem=None):
        elem = self.driver.find_element(locator, elem)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of(elem))
        return elem

    def find_elems(self, locator=By.XPATH, elem=None):
        elems = self.driver.find_elements(locator, elem)
        # wait = WebDriverWait(self.driver, 20)
        # wait.until(EC.visibility_of_all_elements_located(elems))
        return elems

    def get_elem_text(self, elem):
        elem = self.find_elem(elem=elem)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of(elem))
        return elem.text

    def is_elem_displayed(self, elem):
        elem = self.find_elem(elem=elem)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of(elem))
        return elem.is_displayed()

    def is_elem_visible(self, elem):
        elem = self.find_elem(elem=elem)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of(elem))
        return elem.is_visible()

    def is_elem_enabled(self, elem):
        elem = self.find_elem(elem=elem)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of(elem))
        return elem.is_enabled()

    def take_screenshot(self, ss_location):
        self.driver.get_screenshot_as_file(ss_location)

    def take_elem_screeshot(self, elem, ss_location):
        elem.screenshot(ss_location)

    def wait_for_presence_of_all_elems(self, locator):
        wait = WebDriverWait(self.driver, 20)
        list_of_elements = wait.until(EC.presence_of_all_elements_located(locator))
        return list_of_elements
