class Contact:

    def __init__(self, firstname, middlename, lastname, nickname, photopath, title, company, address, homephone, mobilephone, workphone, faxphone, email1, email2, email3, homepage):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photopath = photopath
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.faxphone = faxphone
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage


class ContactDates:

    def __init__(self, bday, bmonth, byear, aday, amonth, ayear):
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear

class ContactSecondary:

    def __init__(self, address, home, notes):
        self.address = address
        self.home = home
        self.notes = notes