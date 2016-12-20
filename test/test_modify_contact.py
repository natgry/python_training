# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(firstname="natalia_upd", middlename="",
                                             lastname="gryaznova_upd", nickname="natgry_upd",
                                             title="sfe_upd", company="emc_upd",
                                             address="spb_upd", home="updated", mobile="updated", work="updated",
                                             fax="updated", email="", email2="x@mail.ru", email3="",
                                             homepage="", group="", address2="", phone2="", notes=""))


def test_modify_contact_name(app):
    app.contact.modify_first_contact(Contact(firstname="natalia updated", middlename="", lastname="gryaznova updated",))


def test_modify_contact_email(app):
    app.contact.modify_first_contact(Contact(email="x@mail.ru"))
