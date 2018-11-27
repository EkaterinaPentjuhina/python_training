# -*- coding: utf-8 -*-
from model.contact_properties import Contact
import pytest
import random
import string


def random_string(maxlen):
    symbols = string.ascii_letters
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digit(maxlen):
    digits = string.digits
    return "".join([random.choice(digits) for i in range(random.randint(5, maxlen))])


def random_mix_string(maxlen, postfix):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + postfix


testdata = [
    Contact(firstname=random_string(10), lastname=random_string(15), middlename=random_string(15),
            nickname=random_string(7), title=random_string(15), company=random_string(15),
            mobilephone=random_digit(11), email=random_mix_string(10, "@mail.ru"), homepage=random_mix_string(10, ".net"),
            address=random_string(20))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




