
def test_delete_first_contact(app):
    # удаление первого контакта из списка на стартовой странице
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()


def test_delete_contact_from_edit_firm(app):
    # удаление контакта из формы редактирования
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact_from_edit_firm()
    app.session.logout()


