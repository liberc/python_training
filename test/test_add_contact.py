from model.contact import Contact

#контейнер
def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.init_creation()
    contact = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Ivashka", photopath ="C:\\lava.jpg", title="test_title", company="test_company_name", address="Moscow, Sovetskaja str, 100", homephone="+7{495}12345678", mobilephone="891612345678", workphone="891677788899", faxphone="891655544111", email1="testemail1@maill.ru", email2="testemail2@maill.ru", email3="testemail3@maill.ru", homepage="www.homepage.ru", dates_bday="1", dates_bmonth="March", dates_byear="1999", dates_aday="8", dates_amonth="July", dates_ayear="2005", secondary_address="Moscow, Street Test", secondary_home="21", secondary_notes="this is test notes")
    app.contact.fill_main(contact)
    app.contact.submit_contact_form()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

