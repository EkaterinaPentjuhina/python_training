from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test group"))
    app.group.modify_first_group(Group(name="group1", header="group1_header", footer="group1_footer"))


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test group"))
    app.group.modify_first_group(Group(name="New group"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test group"))
    app.group.modify_first_group(Group(header="New header"))

