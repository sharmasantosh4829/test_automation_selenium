__maintainer__ = ['santosh.sharma']

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.logger import Logger

from base.base_driver import BaseDriver


class LoginPage(BaseDriver):

    countries_flag_list = ['EN', 'TR', 'DE', 'AR', 'FR', 'JA', 'TH']
    ameyo_logo = "//img[@title='Ameyo']"
    cust_exp_platform_elem = "//h6[normalize-space()='Customer Experience Platform']"
    ent_connect_elem = "//h5[contains(text(),'That Helps Enterprises Connect, Serve and Support ')]"
    footer_text_elem = "//span[contains(text(),'Contact center software')]"
    country_dropdown = "//*[name()='path' and contains(@d,'M7.41 8.59')]"
    lang_in_dropdown = "//p[contains(@class, 'MuiTypography-root mx-4')]"
    country_flag_drop_down = "//img[@alt='EN']"
    wlcm_to_ameyo_elem = "//h5[contains(text(),'Welcome to Ameyo')]"
    eye_icon_visibility_off = "//span[contains(text(),'visibility_off')]"
    eye_icon_visibility_on = "//span[contains(text(),'visibility')]"
    user_id_placeholder = "//label[.='User ID *']"
    password_placeholder = "//label[.='Password *']"
    user_id_field = "//input[@name='userId']"
    password_field = "//input[@name='password']"
    wrong_credentials_elem = "//p[.='User ID or Password is either incorrect or left blank']"
    Acc_blocked_elem = "//p[.='Account blocked temporarily']"
    password_hidden_elem = "//input[@name='password' and @type='password']"
    password_visible_elem = "//input[@name='password' and @type='text']"
    login_btn = "//button[@value='legacy']"
    or_login_with_text = "//h6[normalize-space()='or login with']"
    google_sso_btn = "(//button[@type='button'])[.='Google SSO']"
    saml_btn = "(//button[@type='button'])[.='SAML']"
    captcha_img = "//img[@alt='CAPTCHA']"
    captcha_placeholder = "//label[.='CAPTCHA *']"
    elems_list = [ameyo_logo, cust_exp_platform_elem, ent_connect_elem, footer_text_elem, country_dropdown,
                  lang_in_dropdown, country_flag_drop_down, wlcm_to_ameyo_elem, eye_icon_visibility_off,
                  user_id_placeholder, password_placeholder, user_id_field, password_field, wrong_credentials_elem,
                  login_btn, or_login_with_text, google_sso_btn, saml_btn]
    elems_text_dict = {cust_exp_platform_elem: "Customer Experience Platform",
                       ent_connect_elem: "That Helps Enterprises Connect, Serve and Support their Customers",
                       footer_text_elem: "2021 © Ameyo. Contact center software",
                       wlcm_to_ameyo_elem: "Welcome to Ameyo",
                       user_id_placeholder: "User ID *",
                       password_placeholder: "Password *",
                       wrong_credentials_elem: "User ID or Password is either incorrect or left blank",
                       login_btn: "LOG IN",
                       or_login_with_text: "or login with",
                       google_sso_btn: "Google SSO",
                       saml_btn: "SAML"}

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_title(self):
        title = self.driver.title
        return title

    def enter_user_id(self, user_id):
        user_id_field = self.find_elem(By.XPATH, self.user_id_field)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(user_id_field))
        user_id_field.clear()
        user_id_field.send_keys(user_id)

    def enter_password(self, password):
        password_field = self.find_elem(By.XPATH, self.password_field)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(password_field))
        password_field.clear()
        password_field.send_keys(password)

    def login(self):
        login_btn = self.find_elem(By.XPATH, self.login_btn)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(login_btn))
        login_btn.click()
