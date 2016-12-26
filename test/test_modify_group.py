# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="New group")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    old_groups[0] = group
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
