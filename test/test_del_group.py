from model.group import Group
import random


def test_delete_some_group_by_id(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups


def test_delete_all_groups(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    app.group.delete_all_groups()
    all_groups = db.get_group_list()
    assert len(all_groups) == 0


def test_delete_some_group_by_index(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    from random import randrange
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups

