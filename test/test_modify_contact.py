from model.contact_properties import Contact
import random


def test_edit_contact(app, db, check_ui):
    # редактирование контакта - переход по кнопке в таблице контактов
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(firstname="Ekaterina", middlename="Aleksandrovna", lastname="Pentjuhina",
                                    nickname="kate_penti", title="ttl", company="company", address="Kolomna",
                                    mobilephone="8-111-111-11-11", email="katkarach@gmail.com", homepage="hmpg.net",
                                    address2="address", phone2="home-phone", notes="notes", bday="14", bmonth="October",
                                    byear="1991", aday="1", amonth="January", ayear="2010"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    update_contact = Contact(firstname="Katerina", middlename="Aleksandrovna", lastname="Pentjuhina",
                      nickname="kate_penti", title="ttl", company="company", address="Kolomna",
                      mobilephone="8-111-111-11-11", email="katkarach@gmail.com", homepage="hmpg.net",
                      address2="address", phone2="home-phone", notes="notes")
    app.contact.edit_contact_by_id(contact.id, update_contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    index = old_contacts.index(contact)
    old_contacts[index] = update_contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


# def test_edit_contact_firstname(app):
#     if app.contact.count() == 0:
#         app.contact.add_new(Contact(firstname="Ekaterina", middlename="Aleksandrovna", lastname="Pentjuhina",
#                                     nickname="kate_penti", title="ttl", company="company", address="Kolomna",
#                                     mobile="8-111-111-11-11", email="katkarach@gmail.com", homepage="hmpg.net",
#                                     address2="address", phone2="home-phone", notes="notes", bday="14", bmonth="October",
#                                     byear="1991", aday="1", amonth="January", ayear="2010"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.edit_first_contact(Contact(firstname="Kate"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)


# def test_edit_contact_mobile(app):
#     if app.contact.count() == 0:
#         app.contact.add_new(Contact(firstname="Ekaterina", middlename="Aleksandrovna", lastname="Pentjuhina",
#                                     nickname="kate_penti", title="ttl", company="company", address="Kolomna",
#                                     mobile="8-111-111-11-11", email="katkarach@gmail.com", homepage="hmpg.net",
#                                     address2="address", phone2="home-phone", notes="notes", bday="14", bmonth="October",
#                                     byear="1991", aday="1", amonth="January", ayear="2010"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.edit_first_contact(Contact(mobile="8-222-222-22-22"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)


# def test_edit_first_contact_from_details(app):
#     # редактирование контакта - переход к редактированию из формы просмотра деталей контакта
#     if app.contact.count() == 0:
#         app.contact.add_new(Contact(firstname="Ekaterina", middlename="Aleksandrovna", lastname="Pentjuhina",
#                                     nickname="kate_penti", title="ttl", company="company", address="Kolomna",
#                                     mobile="8-111-111-11-11", email="katkarach@gmail.com", homepage="hmpg.net",
#                                     address2="address", phone2="home-phone", notes="notes", bday="14", bmonth="October",
#                                     byear="1991", aday="1", amonth="January", ayear="2010"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.edit_first_contact_from_details(Contact(address="Saint-Petersburg"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)


# def test_contact_details(app):
#     # просмотр деталей контакта
#     app.contact.view_details_of_first_contact()
