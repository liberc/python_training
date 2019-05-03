from model.contact import Contact

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.init_creation()
        app.contact.fill_main(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Ivashka",
                                      photopath="C:\\lava.jpg", title="test_title", company="test_company_name",
                                      address="Moscow, Sovetskaja str, 100", homephone="+7{495}12345678",
                                      mobilephone="891612345678", workphone="891677788899", faxphone="891655544111",
                                      email1="testemail1@maill.ru", email2="testemail2@maill.ru",
                                      email3="testemail3@maill.ru", homepage="www.homepage.ru", dates_bday="1",
                                      dates_bmonth="March", dates_byear="1999", dates_aday="8", dates_amonth="July",
                                      dates_ayear="2005", secondary_address="Moscow, Street Test", secondary_home="21",
                                      secondary_notes="this is test notes"))
        app.contact.submit_contact_form()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan5", middlename="Ivanovich5", lastname="Ivanov5", nickname="Ivashka1", photopath ="C:\\lava1.jpg", title="test_title1", company="test_company_name1", address="Ekaterinburg, Sovetskaja str, 100", homephone="+7{495}12345000", mobilephone="891612345000", workphone="891677788000", faxphone="891655544000", email1="newemail1@maill.ru", email2="newemail2@maill.ru", email3="newemail3@maill.ru", homepage="www.newhomepage.ru", dates_bday="5", dates_bmonth="January",  dates_byear="2000",  dates_aday="11",  dates_amonth="December",  dates_ayear="2001", secondary_address="Novgorod, Street Test", secondary_home="33", secondary_notes="this is new notes")
    contact.id = old_contacts[0].id
    app.contact.edit_first(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)