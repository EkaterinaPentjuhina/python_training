from model.contact_properties import Contact


def test_edit_first_contact(app):
    # редактирование контакта - переход по кнопке в таблице контактов
    contact = Contact(firstname="Kate", middlename="Aleksandrovna", lastname="Pentjuhina",
                      nickname="kate_penti", title="ttl", company="company", address="Kolomna",
                      mobile="8-111-111-11-11", email="katkarach@gmail.com", homepage="hmpg.net",
                      address2="address", phone2="home-phone", notes="notes", bday="14", bmonth="October",
                      byear="1991", aday="1", amonth="January", ayear="2006")
    app.contact.edit_first_contact(contact)


def test_edit_first_contact_from_details(app):
    # редактирование контакта - переход к редактированию из формы просмотра деталей контакта
    contact = Contact(firstname="Katerina", middlename="Aleksandrovna", lastname="Pentjuhina",
                      nickname="kate_penti", title="ttl", company="company", address="Kolomna",
                      mobile="8-111-111-11-11", email="katkarach@gmail.com", homepage="hmpg.net",
                      address2="address", phone2="home-phone", notes="notes", bday="14", bmonth="October",
                      byear="1991", aday="1", amonth="January", ayear="2007")
    app.contact.edit_first_contact_from_details(contact)


# def test_contact_details(app):
#     # просмотр деталей контакта
#     app.contact.view_details_of_first_contact()
