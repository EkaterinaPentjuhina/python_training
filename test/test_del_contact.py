from model.contact_properties import Contact


def test_delete_first_contact(app):
    # удаление первого контакта из списка на стартовой странице
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="Ekaterina", middlename="Aleksandrovna", lastname="Pentjuhina",
                                    nickname="kate_penti", title="ttl", company="company", address="Kolomna",
                                    mobile="8-111-111-11-11", email="katkarach@gmail.com", homepage="hmpg.net",
                                    address2="address", phone2="home-phone", notes="notes", bday="14", bmonth="October",
                                    byear="1991", aday="1", amonth="January", ayear="2010"))
    app.contact.delete_first_contact()


def test_delete_contact_from_edit_form(app):
    # удаление контакта из формы редактирования
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="Ekaterina", middlename="Aleksandrovna", lastname="Pentjuhina",
                                    nickname="kate_penti", title="ttl", company="company", address="Kolomna",
                                    mobile="8-111-111-11-11", email="katkarach@gmail.com", homepage="hmpg.net",
                                    address2="address", phone2="home-phone", notes="notes", bday="14", bmonth="October",
                                    byear="1991", aday="1", amonth="January", ayear="2010"))
    app.contact.delete_first_contact_from_edit_form()



