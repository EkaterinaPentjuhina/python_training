# -*- coding: utf-8 -*-
from model.contact_properties import Contact


def test_add_new(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ekaterina", middlename="Aleksandrovna", lastname="Pentjuhina",
                      nickname="kate_penti", title="ttl", company="company", address="Kolomna",
                      mobile="8-111-111-11-11", email="katkarach@gmail.com", homepage="hmpg.net",
                      address2="address", phone2="home-phone", notes="notes", bday="14", bmonth="October",
                      byear="1991", aday="1", amonth="January", ayear="2010")
    app.contact.add_new(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




