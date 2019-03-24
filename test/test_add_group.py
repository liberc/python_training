# -*- coding: utf-8 -*-
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import NoAlertPresentException
#import unittest, time, re
import pytest
from fixture.application import Application
from model.group import Group

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="test_name", header="test_header", footer="test_footer"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

# def is_element_present(self, how, what):
#     try: self.wd.find_element(by=how, value=what)
#     except NoSuchElementException as e: return False
#     return True
#
# def is_alert_present(self):
#     try: self.wd.switch_to_alert()
#     except NoAlertPresentException as e: return False
#     return True
#
# if __name__ == "__main__":
#     unittest.main()
