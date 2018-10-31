class ContactName:

    def __init__(self, firstname, middlename, lastname, nickname):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname


class ContactDate:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


class ContactDetails:

    def __init__(self, title, company, address, mobile, email, homepage):
        self.title = title
        self.company = company
        self.address = address
        self.mobile = mobile
        self.email = email
        self.homepage = homepage


class ContactSecondary:

    def __init__(self, address2, phone2, notes):
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes



