from random import randrange
import re


def test_contact_on_home_page(app):
    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.id == contact_from_edit_page.id
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert clear(contact_from_home_page.address) == clear(contact_from_edit_page.address)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_contact_on_home_page_db(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    for contact in contacts_from_home_page:
        index = contacts_from_db.index(contact)
        assert contact.id == contacts_from_db[index].id
        assert contact.lastname == contacts_from_db[index].lastname
        assert contact.firstname == contacts_from_db[index].firstname
        assert contact.address == contacts_from_db[index].address
        assert contact.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[index])
        assert contact.all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[index])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
