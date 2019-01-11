from model.contact_properties import Contact
import random
import allure


def test_delete_contact(app, db, check_ui):
    with allure.step('Given a non-empty contact list'):
        if len(db.get_contact_list()) == 0:
            app.contact.add_new(Contact(firstname="Ekaterina", middlename="Aleksandrovna", lastname="Pentjuhina",
                                        nickname="kate_penti", title="ttl", company="company", address="Kolomna",
                                        mobilephone="8-111-111-11-11", email="katkarach@gmail.com", homepage="hmpg.net",
                                        address2="address", phone2="home-phone", notes="notes", bday="14", bmonth="October",
                                        byear="1991", aday="1", amonth="January", ayear="2010"))
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        contact = random.choice(old_contacts)
    with allure.step('When I delete the contact from the list'):
        app.contact.delete_contact_by_id(contact.id)
    with allure.step('Then the new contact list is equal to the old contact list without the deleted contact'):
        new_contacts = db.get_contact_list()
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def test_delete_contact_from_edit_form(app, db, check_ui):
    with allure.step('Given a non-empty contact list'):
        if len(db.get_contact_list()) == 0:
            app.contact.add_new(Contact(firstname="Ekaterina", middlename="Aleksandrovna", lastname="Pentjuhina",
                                        nickname="kate_penti", title="ttl", company="company", address="Kolomna",
                                        mobilephone="8-111-111-11-11", email="katkarach@gmail.com", homepage="hmpg.net",
                                        address2="address", phone2="home-phone", notes="notes", bday="14", bmonth="October",
                                        byear="1991", aday="1", amonth="January", ayear="2010"))
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        contact = random.choice(old_contacts)
    with allure.step('When I delete the contact from the list'):
        app.contact.delete_contact_by_id_from_edit_form(contact.id)
    with allure.step('Then the new contact list is equal to the old contact list without the deleted contact'):
        new_contacts = db.get_contact_list()
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



