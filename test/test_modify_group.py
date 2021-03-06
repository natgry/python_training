# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_group_by_id_with_db_check(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(name="New group", header="new header", footer="new footer")
    new_group.id = group.id
    app.group.modify_group_by_id(group.id, new_group)
    old_groups = [new_group if x.id == group.id else x for x in old_groups]
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_some_group_name(app):
    from random import randrange
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    old_groups[index] = group
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="header"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New header"))
    assert len(old_groups) == app.group.count()


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", footer="footer"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(footer="New footer"))
    assert len(old_groups) == app.group.count()


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="", header="header_upd", footer="footer_upd"))
    assert len(old_groups) == app.group.count()
