# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_first_group(app):
    app.session.login( username="admin", password="secret")
    app.group.modify_first_group(Group(name="group_upd", header="header_upd", footer="footer_upd"))
    app.session.logout()
