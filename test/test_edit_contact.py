from model.contact import Contact

def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(firstname="Ivan1", middlename="Ivanovich1", lastname="Ivanov1", nickname="Ivashka1", photopath ="C:\\lava1.jpg", title="test_title1", company="test_company_name1", address="Ekaterinburg, Sovetskaja str, 100", homephone="+7{495}12345000", mobilephone="891612345000", workphone="891677788000", faxphone="891655544000", email1="newemail1@maill.ru", email2="newemail2@maill.ru", email3="newemail3@maill.ru", homepage="www.newhomepage.ru", dates_bday="5", dates_bmonth="January",  dates_byear="2000",  dates_aday="11",  dates_amonth="December",  dates_ayear="2001", secondary_address="Novgorod, Street Test", secondary_home="33", secondary_notes="this is new notes"))
    app.session.logout()