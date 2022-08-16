__maintainer__ = ['santosh.sharma']

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_driver import BaseDriver


class SelectExtensionPage(BaseDriver):

    ameyo_logo = "//img[@title='Ameyo']"
    cust_exp_platform_elem = "//h6[normalize-space()='Customer Experience Platform']"
    ent_connect_elem = "//h5[contains(text(),'That Helps Enterprises Connect, Serve and Support ')]"
    footer_text_elem = "//span[contains(text(),'Contact center software')]"
    select_ext_elem = "//h6[normalize-space()='Select Extension']"
    ext_placeholder = "//label[.='Extension']"
    enter_ext_field = "//input[@id='size-small-outlined']"
    ext_dropdown = "//button[@title='Open']"
    phone_number_field = "//input[@name='phoneNumber']"
    continue_btn = "//button[@value='legacy']"
    logout_btn = "//span[normalize-space()='Logout']"
    select_extension = "size-small-outlined"
    ext_list = "li"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_ext(self, extension):
        select_extension = self.find_elem(By.ID, self.select_extension)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(select_extension))
        select_extension.click()
        ext_list = self.find_elems(By.TAG_NAME, self.ext_list)
        for i in ext_list:
            if extension in i.text:
                i.click()
                break

    def set_phn_number(self, phn_number):
        phone_number = self.driver.find_element(By.XPATH, self.phone_number_field)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(phone_number))
        phone_number.click()
        phone_number.send_keys(phn_number)
        phone_number.send_keys(Keys.ENTER)

    def continue_login(self):
        continue_btn = self.driver.find_element(By.XPATH, self.continue_btn)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(continue_btn))
        continue_btn.click()

