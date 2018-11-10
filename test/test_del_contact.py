
def test_delete_first_contact(app):
    # удаление первого контакта из списка на стартовой странице
    app.contact.delete_first_contact()


def test_delete_contact_from_edit_form(app):
    # удаление контакта из формы редактирования
    app.contact.delete_first_contact_from_edit_form()



