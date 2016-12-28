from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None,
                 title=None, company=None, address=None, homephone=None, mobilephone=None, workphone=None, fax=None,
                 email=None, email2=None, email3=None, homepage=None, group="[none]", address2=None, phone2=None,
                 notes=None, id=None, all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.group = group
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        x = self.firstname
        y = other.firstname
        b = (x == y)
        xl = self.lastname
        l = len(xl)
        yl = other.lastname
        yy = len(yl)
        c = (xl == yl)
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstname.strip() == other.firstname and self.lastname == other.lastname.strip()

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
