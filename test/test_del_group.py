from model.group import Group
from random import randrange


def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups


def test_delete_all_groups(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_all_groups()
    all_groups = app.group.get_group_list()
    assert len(all_groups) == 0
