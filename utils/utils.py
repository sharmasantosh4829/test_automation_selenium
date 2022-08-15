__maintainer__ = ['santosh.sharma']

import os
from utils.read_properties import ReadConfig


class Utils:

    @staticmethod
    def get_log_file(filename="automation"):
        logs_dir = ReadConfig.get_logs_dir()
        log_file_ext = ReadConfig.get_log_file_ext()
        path = os.getcwd()
        par_dir = os.path.abspath(os.path.join(path, os.pardir))
        log_dir = os.path.join(par_dir, logs_dir)
        filename = filename + log_file_ext
        logfile = os.path.join(log_dir, filename)
        return logfile

    @staticmethod
    def get_screenshot_file(filename):
        screenshots_dir = ReadConfig.get_screenshot_dir()
        screenshots_file_ext = ReadConfig.get_screenshot_file_ext()
        path = os.getcwd()
        par_dir = os.path.abspath(os.path.join(path, os.pardir))
        screenshots_dir = os.path.join(par_dir, screenshots_dir)
        filename = filename + screenshots_file_ext
        screenshot_file = os.path.join(screenshots_dir, filename)
        return screenshot_file

    @staticmethod
    def get_config_file(filename="config"):
        config_dir = ReadConfig.get_logs_dir()
        config_file_ext = ReadConfig.get_log_file_ext()
        path = os.getcwd()
        par_dir = os.path.abspath(os.path.join(path, os.pardir))
        config_dir = os.path.join(par_dir, config_dir)
        filename = filename + config_file_ext
        config_file = os.path.join(config_dir, filename)
        return config_file

    @staticmethod
    def get_testdata_file(filename="test_data.xlsx"):
        testdata_dir = ReadConfig.get_testdata_dir()
        path = os.getcwd()
        par_dir = os.path.abspath(os.path.join(path, os.pardir))
        testdata_dir = os.path.join(par_dir, testdata_dir)
        testdata_file = os.path.join(testdata_dir, filename)
        return testdata_file


