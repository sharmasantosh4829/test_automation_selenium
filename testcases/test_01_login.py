__maintainer__ = ['santosh.sharma']

import os
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.LoginPage import LoginPage
from pages.SelectCampaignsPage import SelectCampaignsPage
from pages.SelectExtensionPage import SelectExtensionPage
from pages.AgentHomePage import AgentHomePage
from utils.read_properties import ReadConfig
from utils.logger import Logger
from utils.utils import Utils


@pytest.mark.usefixtures("setup")
class TestLogin:
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    invalid_username = ReadConfig.get_invalid_username()
    invalid_password = ReadConfig.get_invalid_password()
    title = ReadConfig.get_title()
    voice_campaign = ReadConfig.select_voice_campaign()
    extension = ReadConfig.select_extension()
    phone_number = ReadConfig.enter_phone_number()
    filename = (__file__.split(os.path.sep)[-1].split(".")[0])
    logfile = Utils.get_log_file(filename=filename)
    logger = Logger.logger(logfile, logger_name=__name__)

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login_page_obj = LoginPage(self.driver)
        self.select_campaigns_page_obj = SelectCampaignsPage(self.driver)
        self.select_ext_page_obj = SelectExtensionPage(self.driver)
        self.agent_logged_in_page_obj = AgentHomePage(self.driver)

    # @pytest.mark.skip("WIP")
    def test_01_verify_title(self, request):
        self.logger.info(f"********** Starting {request.node.name} **********")
        title = self.login_page_obj.get_title()
        if title == self.title:
            assert True
        else:
            self.logger.error(f"********** {request.node.name} failed **********")
            self.logger.error("Reason: Wrong page title")
            self.logger.error(f"expected title: {title}, actual title: {self.title}")
            self.login_page_obj.take_screenshot(Utils.get_screenshot_file(request.node.name))
            self.logger.error("please refer screenshot!!!")
            assert False
        self.logger.info(f"********** {request.node.name} passed **********")

    # @pytest.mark.skip("WIP")
    def test_02_verify_login_page_elems(self, request):
        self.logger.info(f"********** Starting {request.node.name} **********")
        self.logger.info("********** Verifying elements on Login Page **********")
        for elem in self.login_page_obj.elems_list:
            self.logger.info(elem)
            if elem not in [self.login_page_obj.login_btn, self.login_page_obj.wrong_credentials_elem]:
                if self.login_page_obj.is_elem_displayed(elem=elem):
                    self.logger.debug(f"{elem} is displayed")
                    assert True
                else:
                    self.logger.error(f"********** {request.node.name} failed **********")
                    self.logger.error(f"{elem} is not displayed")
                    elem = self.login_page_obj.find_elem(elem)
                    elem_ss = elem + request.node.name
                    self.login_page_obj.take_elem_screeshot(elem, Utils.get_screenshot_file(elem_ss))
                    self.login_page_obj.take_screenshot(Utils.get_screenshot_file(request.node.name))
                    self.logger.error(f"Please refer screenshots!!!")
                    assert False
            elif elem in [self.login_page_obj.login_btn]:
                if not self.login_page_obj.is_elem_enabled(elem):
                    self.logger.debug(f"{elem} not is enabled")
                    assert True
                else:
                    self.logger.error(f"********** {request.node.name} failed **********")
                    self.logger.error(f"Reason: {elem} is enabled")
                    elem = self.login_page_obj.find_elem(elem)
                    elem_ss = elem + request.node.name
                    self.login_page_obj.take_elem_screeshot(elem, Utils.get_screenshot_file(elem_ss))
                    self.login_page_obj.take_screenshot(Utils.get_screenshot_file(request.node.name))
                    self.logger.error(f"Please refer screenshots!!!")
                    assert False
        self.logger.info(f"********** {request.node.name} passed **********")

    # @pytest.mark.skip("WIP")
    def test_03_verify_login_page_elems_text(self, request):
        self.logger.info(f"********** Starting {request.node.name} **********")
        self.logger.info("********** Verifying elements text on Login Page **********")
        for elem in self.login_page_obj.elems_list:
            if elem not in [self.login_page_obj.wrong_credentials_elem]:
                elem_index = self.login_page_obj.elems_list.index(elem)
                self.logger.debug(f"elem index: {elem_index}")
                elem_text = self.login_page_obj.get_elem_text(elem)
                self.logger.debug(f"elem text: {elem_text}")
                if elem in self.login_page_obj.elems_text_dict.keys() and \
                        elem_text == self.login_page_obj.elems_text_dict[elem]:
                    self.logger.debug(f"{self.login_page_obj.elems_list[elem_index]} text is matching")
                    assert True
                elif elem not in self.login_page_obj.elems_text_dict.keys():
                    self.logger.debug(f"{elem} text not available")
                    assert True
                else:
                    self.logger.error(f"********** {request.node.name} failed **********")
                    self.logger.error(f"Reason: {elem} text is not matching")
                    self.logger.error(f"expected: {self.login_page_obj.elems_text_dict[elem]}, actual: {elem_text}")
                    self.login_page_obj.take_elem_screeshot(elem, Utils.get_screenshot_file(request.node.name))
                    self.login_page_obj.take_screenshot(Utils.get_screenshot_file(request.node.name))
                    self.logger.error(f"Please refer screenshots!!!")
                    assert False
        self.logger.info(f"********** {request.node.name} passed **********")

    # @pytest.mark.skip("WIP")
    def test_04_agent_login(self, request):
        self.logger.info(f"********** Starting {request.node.name} **********")
        eye_icon_visibility_on = self.login_page_obj.find_elem(elem=self.login_page_obj.eye_icon_visibility_on)
        login_btn = self.login_page_obj.find_elem(elem=self.login_page_obj.login_btn)

        self.logger.info("********** Agent login **********")
        elems_list = [eye_icon_visibility_on, login_btn]
        for elem in self.login_page_obj.elems_list:
            if elem in [eye_icon_visibility_on, login_btn]:
                elem_index = elems_list.index(elem)
                if elem.is_displayed():
                    self.logger.debug(f"{elems_list[elem_index]} is displayed")
                    assert True
                else:
                    self.logger.error(f"********** {request.node.name} failed **********")
                    self.logger.error(f"{elems_list[elem_index]} is not displayed")
                    self.login_page_obj.take_elem_screeshot(elem, Utils.get_screenshot_file(request.node.name))
                    self.login_page_obj.take_screenshot(Utils.get_screenshot_file(request.node.name))
                    self.logger.error(f"Please refer screenshots!!!")
                    assert False
        self.login_page_obj.enter_user_id(self.invalid_username)
        self.login_page_obj.enter_password(self.invalid_password)
        password_hidden_elem = self.login_page_obj.find_elem(elem=self.login_page_obj.password_hidden_elem)
        if password_hidden_elem.is_displayed():
            self.logger.debug(f"{password_hidden_elem} is displayed")
            assert True
        else:
            self.logger.error(f"********** {request.node.name} failed **********")
            self.logger.error(f"password is not hidden")
            self.login_page_obj.take_elem_screeshot(password_hidden_elem, Utils.get_screenshot_file(request.node.name))
            self.login_page_obj.take_screenshot(Utils.get_screenshot_file(request.node.name))
            self.logger.error(f"Please refer screenshots!!!")
            assert False
        eye_icon_visibility_on.click()
        password_visible_elem = self.login_page_obj.find_elem(elem=self.login_page_obj.password_visible_elem)
        if password_visible_elem.is_displayed():
            self.logger.debug(f"{password_visible_elem} is displayed")
            assert True
        else:
            self.logger.error(f"********** {request.node.name} failed **********")
            self.logger.error(f"password is not visible")
            self.login_page_obj.take_elem_screeshot(password_visible_elem, Utils.get_screenshot_file(request.node.name))
            self.login_page_obj.take_screenshot(Utils.get_screenshot_file(request.node.name))
            self.logger.error(f"Please refer screenshots!!!")
            assert False
        eye_icon_visibility_on.click()
        self.login_page_obj.login()
        time.sleep(5)
        wrong_credentials_elem = self.login_page_obj.find_elem(elem=self.login_page_obj.wrong_credentials_elem)
        if wrong_credentials_elem.is_displayed() and \
                wrong_credentials_elem.text == \
                self.login_page_obj.elems_text_dict[self.login_page_obj.wrong_credentials_elem]:
            self.logger.debug(f"Login unsuccessful")
            self.logger.debug(f"{wrong_credentials_elem.text} is displayed")
            assert True
        else:
            self.logger.error(f"********** {request.node.name} failed **********")
            self.logger.error(f"wrong_credentials_elem is not visible")
            self.login_page_obj.take_elem_screeshot(wrong_credentials_elem, Utils.get_screenshot_file(request.node.name))
            self.login_page_obj.take_screenshot(Utils.get_screenshot_file(request.node.name))
            self.logger.error(f"Please refer screenshots!!!")
            assert False
        captcha_img = self.login_page_obj.find_elem(elem=self.login_page_obj.captcha_img)
        captcha_placeholder = self.login_page_obj.find_elem(elem=self.login_page_obj.captcha_placeholder)
        captcha_elems = [captcha_img, captcha_placeholder]
        for elem in captcha_elems:
            elem_index = captcha_elems.index(elem)
            if elem.is_displayed():
                self.logger.debug(f"{captcha_elems[elem_index]} is displayed")
                assert True
            else:
                self.logger.error(f"********** {request.node.name} failed **********")
                self.logger.error(f"{captcha_elems[elem_index]} is not displayed")
                self.login_page_obj.take_elem_screeshot(elem, Utils.get_screenshot_file(request.node.name))
                self.login_page_obj.take_screenshot(Utils.get_screenshot_file(request.node.name))
                self.logger.error(f"Please refer screenshots!!!")
                assert False
        self.driver.refresh()
        time.sleep(5)
        self.login_page_obj.enter_user_id(self.username)
        self.login_page_obj.enter_password(self.password)
        self.login_page_obj.login()
        time.sleep(5)
        select_campaigns_elem = self.select_campaigns_page_obj. \
            find_elem(elem=self.select_campaigns_page_obj.select_campaigns_elem)
        if select_campaigns_elem.is_displayed():
            self.logger.debug(f"Login Successful")
            assert True
        else:
            self.logger.error(f"********** {request.node.name} failed **********")
            self.logger.error(f"Agent Login Failed!!!")
            self.login_page_obj.take_elem_screeshot(select_campaigns_elem, Utils.get_screenshot_file(request.node.name))
            self.login_page_obj.take_screenshot(Utils.get_screenshot_file(request.node.name))
            self.logger.error(f"Please refer screenshot!!!")
            assert False
        voice_camp_input_field = self.select_campaigns_page_obj. \
            find_elem(elem=self.select_campaigns_page_obj.voice_camp_input_field)
        if voice_camp_input_field.is_displayed():
            self.logger.debug(f"Login Successful")
            assert True
        else:
            self.logger.error(f"********** {request.node.name} failed **********")
            self.logger.error(f"Agent Login Failed!!!")
            self.driver.get_screenshot_as_file(Utils.get_screenshot_file(request.node.name))
            self.logger.error(f"Please refer screenshot!!!")
            assert False
        time.sleep(3)
        self.select_campaigns_page_obj.select_voice_campaign(self.voice_campaign)
        actionchains = ActionChains(self.driver)
        actionchains.move_to_element(voice_camp_input_field).move_by_offset(0, 26).click().perform()
        time.sleep(5)
        self.select_campaigns_page_obj.continue_login()
        time.sleep(3)
        select_ext_elem = self.select_ext_page_obj.find_elem(By.XPATH, self.select_ext_page_obj.select_ext_elem)
        if select_ext_elem.is_displayed():
            self.logger.debug(f"Login Successful")
            assert True
        else:
            self.logger.error(f"********** {request.node.name} failed **********")
            self.logger.error(f"Agent Login Failed!!!")
            self.select_ext_page_obj.take_screenshot(Utils.get_screenshot_file(request.node.name))
            self.logger.error(f"Please refer screenshot!!!")
            assert False
        self.select_ext_page_obj.select_ext(self.extension)
        self.select_ext_page_obj.set_phn_number(self.phone_number)
        self.select_ext_page_obj.continue_login()
        time.sleep(10)
        ameyo_hidden_logo = self.agent_logged_in_page_obj.find_elem(
            elem=self.agent_logged_in_page_obj.ameyo_hidden_logo)
        actionchains.move_to_element(ameyo_hidden_logo).perform()
        agent_name = self.agent_logged_in_page_obj.find_elem(elem=self.agent_logged_in_page_obj.agent_name)
        if agent_name.is_displayed():
            self.logger.debug(f"Login Successful")
            assert True
        else:
            self.logger.error(f"********** {request.node.name} failed **********")
            self.logger.error(f"Agent Login Failed!!!")
            self.agent_logged_in_page_obj.take_screenshot(Utils.get_screenshot_file(request.node.name))
            self.logger.error(f"Please refer screenshot!!!")
            assert False
        self.logger.info(f"********** {request.node.name} passed **********")
