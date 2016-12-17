# -*- coding: utf-8 -*-
import pytest

from contact import Contact
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="natalia", middlename="alex",
                               lastname="gryaznova", nickname="natgry",
                               title="sfe", company="emc",
                               address="spb", home="-", mobile="-", work="-", fax="-",
                               email="natgry@yandex.ru", email2="-", email3="-",
                               homepage="-", group="[none]", address2="-", phone2="-", notes="-"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="",
                               lastname="", nickname="",
                               title="", company="",
                               address="", home="", mobile="", work="", fax="",
                               email="", email2="", email3="",
                               homepage="", group="[none]", address2="", phone2="", notes=""))
    app.session.logout()

