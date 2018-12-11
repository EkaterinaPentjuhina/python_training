from selenium.webdriver.support.ui import Select
from model.contact_properties import Contact
import re


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
        self.change_field_value("mobile", contact.mobilephone)
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
        self.contact_cache = None

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_id("logo").click()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        # select first contact
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_id("logo").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        # select first contact
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # update contact details
        self.fill_contact_details(contact)
        # submit
        wd.find_element_by_name("update").click()
        self.return_to_homepage()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_xpath('//a[contains(@href, "edit.php?id=%s")]' % id).click()
        # update contact details
        self.fill_contact_details(contact)
        # submit
        wd.find_element_by_name("update").click()
        self.return_to_homepage()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def view_details_of_first_contact(self):
        wd = self.app.wd
        self.open_contact_view_by_index(0)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

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
        self.contact_cache = None

    def delete_contact_by_index_from_edit_form(self, index):
        wd = self.app.wd
        # open edit form of first contact
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # submit deletion
        wd.find_element_by_xpath("(//input[@name='update'])[3]").click()
        self.return_to_homepage()
        self.contact_cache = None

    def delete_contact_by_id_from_edit_form(self, id):
        wd = self.app.wd
        # open edit form of first contact
        wd.find_element_by_xpath('//a[contains(@href, "edit.php?id=%s")]' % id).click()
        # submit deletion
        wd.find_element_by_xpath("(//input[@name='update'])[3]").click()
        self.return_to_homepage()
        self.contact_cache = None

    def delete_first_contact_from_edit_form(self):
        self.delete_contact_by_index_from_edit_form(0)

    def return_to_homepage(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_to_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                firstname = element.find_element_by_css_selector("td:nth-child(3)").text
                lastname = element.find_element_by_css_selector("td:nth-child(2)").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                address = element.find_element_by_css_selector("td:nth-child(4)").text
                all_phones = element.find_element_by_css_selector("td:nth-child(6)").text
                all_emails = element.find_element_by_css_selector("td:nth-child(5)").text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone, phone2=secondaryphone, email=email, email2=email2,
                       email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone, phone2=secondaryphone)











