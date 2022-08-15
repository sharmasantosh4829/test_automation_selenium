__maintainer__ = ['santosh.sharma']

import os
import configparser


path = os.getcwd()
par_dir = os.path.abspath(os.path.join(path, os.pardir))
config_dir = os.path.join(par_dir, "config")
config_file = os.path.join(config_dir, "config.ini")

config = configparser.RawConfigParser()
config.read(config_file)


class ReadConfig:

    @staticmethod
    def get_app_url():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def get_title():
        title = config.get('common info', 'title')
        return title

    @staticmethod
    def get_base_window_handle():
        base_window_handle = config.get('common info', 'base_window_handle')
        return base_window_handle

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('common info', 'invalid_username')
        return invalid_username

    @staticmethod
    def get_invalid_password():
        invalid_password = config.get('common info', 'invalid_password')
        return invalid_password

    @staticmethod
    def select_voice_campaign():
        voice_campaign = config.get('select voice campaign', 'voice_campaign')
        return voice_campaign

    @staticmethod
    def select_extension():
        extension = config.get('select extension', 'ext')
        return extension

    @staticmethod
    def enter_phone_number():
        phone_number = config.get('select extension', 'phone_number')
        return phone_number

    @staticmethod
    def get_logs_dir():
        logs_dir = config.get('logger info', 'log_dir')
        return logs_dir

    @staticmethod
    def get_log_file_ext():
        log_file_ext = config.get('logger info', 'log_file_ext')
        return log_file_ext

    @staticmethod
    def get_screenshot_dir():
        screenshots_dir = config.get('screenshot info', 'screenshot_dir')
        return screenshots_dir

    @staticmethod
    def get_screenshot_file_ext():
        screenshot_file_ext = config.get('screenshot info', 'screenshot_file_ext')
        return screenshot_file_ext

    @staticmethod
    def get_config_dir():
        config_dir = config.get('config info', 'config_dir')
        return config_dir

    @staticmethod
    def get_config_file_ext():
        config_file_ext = config.get('config info', 'config_file_ext')
        return config_file_ext

    @staticmethod
    def get_testdata_dir():
        testdata_dir = config.get('testdata info', 'testdata_dir')
        return testdata_dir

    @staticmethod
    def get_testdata_file_ext():
        testdata_file_ext = config.get('testdata info', 'testdata_file_ext')
        return testdata_file_ext

