from sys import maxsize

class Contact:

    def __init__(self, firstname = None, middlename = None, lastname = None, nickname = None, photopath = None, title = None, company = None, address = None, homephone = None, mobilephone = None, workphone = None, faxphone = None, email1 = None, email2 = None, email3 = None, homepage = None, dates_bday = None, dates_bmonth = None, dates_byear = None, dates_aday = None, dates_amonth = None, dates_ayear = None, secondary_address = None, secondary_home = None, secondary_notes = None, id = None):
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
        self.dates_bday = dates_bday
        self.dates_bmonth = dates_bmonth
        self.dates_byear = dates_byear
        self.dates_aday = dates_aday
        self.dates_amonth = dates_amonth
        self.dates_ayear = dates_ayear
        self.secondary_address = secondary_address
        self.secondary_home = secondary_home
        self.secondary_notes = secondary_notes
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id == other.id or other.id is None or self.id is None) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize