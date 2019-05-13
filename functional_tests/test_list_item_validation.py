import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

from .base import FunctionalTest


class InvalidValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_item(self):
        self.fail('write me!')
