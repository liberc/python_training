# -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
#import unittest, time, re
import pytest
from fixture.application import Application
from model.contact import Contact
from model.contact import ContactDates
from model.contact import ContactSecondary

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    #контейнер
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.fill_contact_main(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Ivashka", photopath = "C:\\lava.jpg", title="test_title", company="test_company_name", address="Moscow, Sovetskaja str, 100", homephone="+7{495}12345678", mobilephone="891612345678", workphone="891677788899", faxphone="891655544111", email1="testemail1@maill.ru", email2="testemail2@maill.ru", email3="testemail3@maill.ru", homepage="www.homepage.ru"))
    app.fill_contact_dates(ContactDates(bday="1", bmonth="March", byear="1999", aday="8", amonth="July", ayear="2005"))
    app.fill_contact_secondary(ContactSecondary(address="Moscow, Street Test", home="21", notes="this is test notes"))
    app.session.logout()



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
# def close_alert_and_get_its_text(self):
#     try:
#         alert = self.wd.switch_to_alert()
#         alert_text = alert.text
#         if self.accept_next_alert:
#             alert.accept()
#         else:
#             alert.dismiss()
#         return alert_text
#     finally: self.accept_next_alert = True

# if __name__ == "__main__":
#     unittest.main()
