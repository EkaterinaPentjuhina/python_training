from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_page_add_new(self):
        wd = self.app.wd
        # open page for create new contact
        wd.find_element_by_link_text("add new").click()

    def fill_contact_details(self, contact):
        wd = self.app.wd
        # fill name of new contact
        # fill firstname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        # fill middlename
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        # fill lastname
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # fill nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # fill contact details
        # fill title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        # fill company's name
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        # fill address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        # fill mobile
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        # fill e-mail
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # fill homepage
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # fill b-day
        # day
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_xpath("//option[@value='14']").click()
        # month
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_xpath("//option[@value='October']").click()
        # year
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        # fill anniversary
        # day
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        wd.find_element_by_xpath("(//option[@value='1'])[2]").click()
        # month
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_xpath("(//option[@value='January'])[2]").click()
        # year
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        # fill secondary details
        # fill address
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        # fill home phone
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        # fill notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def add_new(self, contact):
        wd = self.app.wd
        self.open_page_add_new()
        self.fill_contact_details(contact)
        self.submit()
        # return to homepage
        wd.find_element_by_link_text("home").click()

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        # return to homepage
        wd.find_element_by_link_text("home").click()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # update contact details
        self.fill_contact_details(contact)
        # submit
        wd.find_element_by_name("update").click()
        # return to homepage
        wd.find_element_by_link_text("home").click()

    def view_details_of_first_contact(self):
        wd = self.app.wd
        # open firm of first contact's details
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        # return to homepage
        wd.find_element_by_link_text("home").click()

    def edit_first_contact_from_details(self, contact):
        wd = self.app.wd
        # open firm of first contact's details
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        # modify
        wd.find_element_by_name("modifiy").click()
        # update contact details
        self.fill_contact_details(contact)
        # submit
        wd.find_element_by_name("update").click()
        # return to homepage
        wd.find_element_by_link_text("home").click()

    def delete_first_contact_from_edit_firm(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # submit deletion
        wd.find_element_by_xpath("(//input[@name='update'])[3]").click()
        # return to homepage
        wd.find_element_by_link_text("home").click()




