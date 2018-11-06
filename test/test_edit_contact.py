from model.contact_properties import Contact


def test_edit_first_contact(app):
    # редактирование контакта - переход по кнопке в таблице контактов
    app.session.login(username="admin", password="secret")
    contact = Contact(firstname="Ekaterina", middlename="Aleksandrovna", lastname="Pentjuhina",
                      nickname="kate_penti", title="ttl", company="company", address="Kolomna",
                      mobile="8-333-333-33-33", email="katkarach@gmail.com", homepage="hmpg.net",
                      address2="address", phone2="home-phone", notes="notes", bday="14", bmonth="October",
                      byear="1991", aday="1", amonth="January", ayear="2010")
    app.contact.edit_first_contact(contact)
    app.session.logout()


def test_edit_first_contact_from_details(app):
    # редактирование контакта - переход к редактированию из формы просмотра деталей контакта
    app.session.login(username="admin", password="secret")
    contact = Contact(firstname="Ekaterina", middlename="Aleksandrovna", lastname="Pentjuhina",
                      nickname="kate_penti", title="ttl", company="company", address="Kolomna",
                      mobile="8-222-222-22-22", email="katkarach@gmail.com", homepage="hmpg.net",
                      address2="address", phone2="612-13-14", notes="notes", bday="14", bmonth="October",
                      byear="1991", aday="1", amonth="January", ayear="2010")
    app.contact.edit_first_contact_from_details(contact)
    app.session.logout()


def test_contact_details(app):
    # просмотр деталей контакта
    app.session.login(username="admin", password="secret")
    app.contact.view_details_of_first_contact()
    app.session.logout()