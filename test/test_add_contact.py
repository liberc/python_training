from model.contact import Contact
from model.contact import ContactDates
from model.contact import ContactSecondary

#контейнер
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.init_creation()
    app.contact.fill_main(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Ivashka", photopath ="C:\\lava.jpg", title="test_title", company="test_company_name", address="Moscow, Sovetskaja str, 100", homephone="+7{495}12345678", mobilephone="891612345678", workphone="891677788899", faxphone="891655544111", email1="testemail1@maill.ru", email2="testemail2@maill.ru", email3="testemail3@maill.ru", homepage="www.homepage.ru"))
    app.contact.fill_dates(ContactDates(bday="1", bmonth="March", byear="1999", aday="8", amonth="July", ayear="2005"))
    app.contact.fill_secondary(ContactSecondary(address="Moscow, Street Test", home="21", notes="this is test notes"))
    app.contact.submit_contact_form()
    app.session.logout()

