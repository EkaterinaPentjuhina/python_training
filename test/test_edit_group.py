from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="group1", header="group1_header", footer="group1_footer"))
    app.session.logout()