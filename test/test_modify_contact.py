from model.contact_properties import Contact
from random import randrange


def test_edit_first_contact(app):
    # редактирование контакта - переход по кнопке в таблице контактов
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="Ekaterina", middlename="Aleksandrovna", lastname="Pentjuhina",
                                    nickname="kate_penti", title="ttl", company="company", address="Kolomna",
                                    mobilephone="8-111-111-11-11", email="katkarach@gmail.com", homepage="hmpg.net",
                                    address2="address", phone2="home-phone", notes="notes", bday="14", bmonth="October",
                                    byear="1991", aday="1", amonth="January", ayear="2010"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Katerina", middlename="Aleksandrovna", lastname="Pentjuhina",
                      nickname="kate_penti", title="ttl", company="company", address="Kolomna",
                      mobilephone="8-111-111-11-11", email="katkarach@gmail.com", homepage="hmpg.net",
                      address2="address", phone2="home-phone", notes="notes", bday="14", bmonth="October",
                      byear="1991", aday="1", amonth="January", ayear="2006")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


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
