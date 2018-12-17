from model.group import Group
from model.contact_properties import Contact


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(app, db):
    ui_contact_list = app.contact.get_contact_list()
    db_contact_list = db.get_contact_list()
    assert sorted(ui_contact_list, key=Contact.id_or_max) == sorted(db_contact_list, key=Contact.id_or_max)


def test_contacts_in_group_db_ui(app, orm):
    group_id = 229
    ui_list = app.contact.get_contacts_in_group(group_id)
    orm_list = orm.get_contacts_in_group(group_id)
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(orm_list, key=Contact.id_or_max)
