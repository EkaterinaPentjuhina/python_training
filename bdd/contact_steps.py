from pytest_bdd import given, when, then
from model.contact_properties import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <firstname>, <lastname>, <middlename>, <nickname>, <title>, <company>, <homephone>, <mobilephone>, <workphone>, <phone2>, <email>, <homepage>, <address>')
def new_contact(firstname, lastname, middlename, nickname, title, company, homephone, mobilephone, workphone, phone2,
                email, homepage, address):
    return Contact(firstname=firstname, lastname=lastname, middlename=middlename, nickname=nickname, title=title,
                   company=company, homephone=homephone, mobilephone=mobilephone, workphone=workphone, phone2=phone2,
                   email=email, homepage=homepage, address=address)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.add_new(new_contact)


@then('the new contact list is equal to the old list with added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(firstname="firstname1", lastname="lastname1", middlename="middlename1",
                                    nickname="nickname1", title="title1", company="company1", homephone="11-11-11",
                                    mobilephone="11-11-11", workphone="1111-11", phone2="11-11-11", email="1@mail.ru",
                                    homepage="homepage.net", address="address1"))
    return db.get_contact_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old contact list without the deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts) + 1
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)


@given("new contact's data")
def update_contact():
    return Contact(firstname="Katerina", middlename="Aleksandrovna", lastname="Pentjuhina", nickname="kate_penti",
                   title="ttl", company="company", address="Kolomna", mobilephone="8-111-111-11-11",
                   email="katkarach@gmail.com", homepage="hmpg.net", address2="address", phone2="home-phone",
                   notes="notes")


@when("I modify the contact's properties")
def modify_contact(app, random_contact, update_contact):
    app.contact.edit_contact_by_id(random_contact.id, update_contact)


@then("the new contact list is equal to the old contact list with the modified contact")
def verify_contact_modified(db, non_empty_contact_list, random_contact, update_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    index = old_contacts.index(random_contact)
    old_contacts[index] = update_contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)





