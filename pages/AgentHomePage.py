__maintainer__ = ['santosh.sharma']

from base.base_driver import BaseDriver


class AgentHomePage(BaseDriver):

    ameyo_hidden_logo = "//img[@class='hidden logo-icon']"
    agent_name = "//p[@automationid='agentName']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

