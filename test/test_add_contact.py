# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="natalia", middlename="alex",
                               lastname="gryaznova", nickname="natgry",
                               title="sfe", company="emc",
                               address="spb", home="-", mobile="-", work="-", fax="-",
                               email="natgry@yandex.ru", email2="-", email3="-",
                               homepage="-", group="[none]", address2="-", phone2="-", notes="-"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="",
                               lastname="", nickname="",
                               title="", company="",
                               address="", home="", mobile="", work="", fax="",
                               email="", email2="", email3="",
                               homepage="", group="[none]", address2="", phone2="", notes=""))


