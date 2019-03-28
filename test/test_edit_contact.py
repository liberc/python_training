from model.contact import Contact
from model.contact import ContactDates
from model.contact import ContactSecondary

def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(firstname="Ivan1", middlename="Ivanovich1", lastname="Ivanov1", nickname="Ivashka1", photopath ="C:\\lava1.jpg", title="test_title1", company="test_company_name1", address="Ekaterinburg, Sovetskaja str, 100", homephone="+7{495}12345000", mobilephone="891612345000", workphone="891677788000", faxphone="891655544000", email1="newemail1@maill.ru", email2="newemail2@maill.ru", email3="newemail3@maill.ru", homepage="www.newhomepage.ru"),ContactDates(bday="5", bmonth="January", byear="2000", aday="11", amonth="December", ayear="2001"),ContactSecondary(address="Novgorod, Street Test", home="33", notes="this is new notes"))
    app.session.logout()