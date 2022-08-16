__maintainer__ = ['santosh.sharma']

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_driver import BaseDriver


class SelectCampaignsPage(BaseDriver):

    ameyo_logo = "//img[@title='Ameyo']"
    cust_exp_platform_elem = "//h6[normalize-space()='Customer Experience Platform']"
    ent_connect_elem = "//h5[contains(text(),'That Helps Enterprises Connect, Serve and Support ')]"
    footer_text_elem = "//span[contains(text(),'Contact center software')]"
    select_campaigns_elem = "//h6[normalize-space()='Select campaigns to get started']"
    no_int_camp_avail_placeholder = "//label[.='No Interaction Campaign Available']"
    no_chat_camp_avail_placeholder = "//label[.='No Chat Campaign Available']"
    blended_elem = "//span[.='Blended']"
    voice_camp_placeholder = "//label[.='Voice Campaign']"
    voice_camp_dropdown = "//button[@class='MuiButtonBase-root MuiIconButton-root MuiAutocomplete-popupIndicator']"
    voice_camp_input_field = "//input[contains(@id, 'mui') and not(@disabled)]"
    continue_btn = "//span[normalize-space()='continue']"
    logout_btn = "//span[normalize-space()='Logout']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_voice_campaign(self, voice_campaign):
        voice_camp_dd = self.find_elem(By.XPATH, self.voice_camp_dropdown)
        voice_camp_inp_field = self.find_elem(By.XPATH, self.voice_camp_input_field)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of(voice_camp_dd))
        voice_camp_dd.click()
        voice_camp_inp_field.send_keys(voice_campaign)

    def continue_login(self):
        continue_btn = self.find_elem(By.XPATH, self.continue_btn)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(continue_btn))
        continue_btn.click()

    def logout(self):
        logout_btn = self.find_elem(By.XPATH, self.logout_btn)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(logout_btn))
        logout_btn.click()
