from model.group import Group
import random

# def test_modify_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test group"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(name="group1", header="group1_header", footer="group1_footer"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test group"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(name="Group111", header="Header111", footer="Footer111")
    app.group.modify_group_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    index = old_groups.index(group)
    old_groups[index] = new_group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test group"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

