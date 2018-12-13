from model.contact_properties import Contact
import random


def test_add_contact_to_group(app, db):
    # if len(db.get_contact_list()) == 0:
    #     app.contact.add_new(Contact(firstname="Ekaterina", middlename="Aleksandrovna", lastname="Pentjuhina",
    #                                 nickname="kate_penti", title="ttl", company="company", address="Kolomna",
    #                                 mobilephone="8-111-111-11-11", email="katkarach@gmail.com", homepage="hmpg.net",
    #                                 address2="address", phone2="home-phone", notes="notes", bday="14", bmonth="October",
    #                                 byear="1991", aday="1", amonth="January", ayear="2010"))
    # all_contacts = db.get_contact_list()
    # contact = random.choice(all_contacts)
    group_name = "name2"
    contact_id = 237
    app.contact.add_contact_to_group(contact_id, group_name)


