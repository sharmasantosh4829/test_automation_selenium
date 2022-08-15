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
from utils.excel_utils import Excl


@pytest.mark.usefixtures("setup")
class TestLoginDdt:
    title = ReadConfig.get_title()
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
    def test_03_verify_login_page_elems(self, request):
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

    @pytest.mark.skip("WIP")
    def test_04_verify_login_page_elems_text(self, request):
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
    def test_05_agent_login(self, request):
        self.logger.info(f"********** Starting {request.node.name} **********")
        testdata_file = Utils.get_testdata_file()
        self.rows = Excl.get_row_count(testdata_file, "Sheet1")
        self.logger.debug(f"row count: {self.rows}")

        list_status = []
        for row in range(2, self.rows+1):
            self.username = Excl.read_data(testdata_file, "Sheet1", row, 1)
            self.password = Excl.read_data(testdata_file, "Sheet1", row, 2)
            self.expected = Excl.read_data(testdata_file, "Sheet1", row, 3)
            self.login_page_obj.enter_user_id(self.username)
            self.login_page_obj.enter_password(self.password)
            self.login_page_obj.login()
            time.sleep(5)
            title = self.login_page_obj.get_title()
            if title == self.title:
                if self.expected == "Pass":
                    self.logger.info(f"***Passed***")
                    self.select_campaigns_page_obj.logout()
                    time.sleep(5)
                    list_status.append("Pass")
                elif self.expected == "Fail":
                    self.logger.info(f"***Passed***")
                    list_status.append("Pass")
            elif title != self.title:
                if self.expected == "Pass":
                    self.logger.info(f"***Failed***")
                    self.select_campaigns_page_obj.logout()
                    time.sleep(5)
                    list_status.append("Fail")
                elif self.expected == "Fail":
                    self.logger.info(f"***Passed***")
                    list_status.append("Pass")
        if "Fail" not in list_status:
            self.logger.info(f"********** {request.node.name} passed **********")
            assert True
        else:
            self.logger.error(f"********** {request.node.name} failed **********")
            assert False
