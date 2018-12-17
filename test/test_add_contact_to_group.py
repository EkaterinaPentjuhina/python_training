from model.contact_properties import Contact
import random
from model.group import Group


def test_add_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.add_new(Contact(firstname="Ekaterina", middlename="Aleksandrovna", lastname="Pentjuhina",
                                    nickname="kate_penti", title="ttl", company="company", address="Kolomna",
                                    mobilephone="8-111-111-11-11", email="katkarach@gmail.com", homepage="hmpg.net",
                                    address2="address", phone2="home-phone", notes="notes", bday="14", bmonth="October",
                                    byear="1991", aday="1", amonth="January", ayear="2010"))
    all_contacts = orm.get_contact_list()
    contact = random.choice(all_contacts)
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test group"))
    all_groups = orm.get_group_list()
    group = random.choice(all_groups)
    if contact in orm.get_contacts_in_group(group):
        # удалить контакт из группы
        app.contact.delete_contact_from_group(group.id, contact.id)
    # добавить контакт к группе
    app.contact.add_contact_to_group(contact.id, group.id)
    contacts_in_group = orm.get_contacts_in_group(group)
    contacts_in_group_ui = app.contact.get_contacts_in_group(group.id)
    assert sorted(contacts_in_group_ui, key=Contact.id_or_max) == sorted(contacts_in_group, key=Contact.id_or_max)




