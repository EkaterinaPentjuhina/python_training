# -*- coding: utf-8 -*-
from model.contact_properties import Contact
import allure


def test_add_new(app, db, json_contacts, check_ui):
    contact = json_contacts
    with allure.step('Given a group list'):
        old_contacts = db.get_contact_list()
    with allure.step('When I add a contact %s to the list' % contact):
        app.contact.add_new(contact)
    with allure.step('Then the new contact list is equal to the old list with added contact'):
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)




