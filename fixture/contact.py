from selenium.webdriver.support.ui import Select
from model.contact_properties import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_page_add_new(self):
        wd = self.app.wd
        # open page for create new contact
        wd.find_element_by_link_text("add new").click()

    def fill_contact_details(self, contact):
        wd = self.app.wd
        # fill name of contact
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        # fill contact details
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)
        self.change_field_value("homepage", contact.homepage)
        # fill b-day
        if contact.bday is not None:
            wd.find_element_by_name("bday").click()
            Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
            wd.find_element_by_xpath("//option[@value='14']").click()
        if contact.bmonth is not None:
            wd.find_element_by_name("bmonth").click()
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
            wd.find_element_by_xpath("//option[@value='October']").click()
        self.change_field_value("byear", contact.byear)
        # fill anniversary
        if contact.aday is not None:
            wd.find_element_by_name("aday").click()
            Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
            wd.find_element_by_xpath("(//option[@value='1'])[2]").click()
        if contact.amonth is not None:
            wd.find_element_by_name("amonth").click()
            Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
            wd.find_element_by_xpath("(//option[@value='January'])[2]").click()
        self.change_field_value("ayear", contact.ayear)
        # fill secondary details
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def add_new(self, contact):
        wd = self.app.wd
        self.open_page_add_new()
        self.fill_contact_details(contact)
        self.submit()
        self.return_to_homepage()

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
        wd.find_element_by_id("logo").click()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # update contact details
        self.fill_contact_details(contact)
        # submit
        wd.find_element_by_name("update").click()
        self.return_to_homepage()

    def view_details_of_first_contact(self):
        wd = self.app.wd
        # open firm of first contact's details
        wd.find_element_by_xpath("//img[@alt='Details']").click()

    def edit_first_contact_from_details(self, contact):
        wd = self.app.wd
        self.view_details_of_first_contact()
        # modify
        wd.find_element_by_name("modifiy").click()
        # update contact details
        self.fill_contact_details(contact)
        # submit
        wd.find_element_by_name("update").click()
        self.return_to_homepage()

    def delete_first_contact_from_edit_form(self):
        wd = self.app.wd
        # open edit form of first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # submit deletion
        wd.find_element_by_xpath("(//input[@name='update'])[3]").click()
        self.return_to_homepage()

    def return_to_homepage(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_to_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        contacts = []
        for element in wd.find_elements_by_css_selector("tr[name=entry]"):
            firstname = element.find_element_by_css_selector("td:nth-child(3)").text
            lastname = element.find_element_by_css_selector("td:nth-child(2)").text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return contacts







