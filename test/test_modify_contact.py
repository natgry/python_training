# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="natalia", middlename="alexandrovna", lastname="gryaznova"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="natalia updated", middlename="", lastname="gryaznova updated")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="natalia", middlename="alexandrovna", lastname="gryaznova", email="-"))
    app.contact.modify_first_contact(Contact(email="x@mail.ru"))


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="natalia", middlename="alexandrovna", lastname="gryaznova", email="-"))
    app.contact.modify_first_contact(Contact(firstname="natalia_upd", middlename="",
                                             lastname="gryaznova_upd", nickname="natgry_upd",
                                             title="sfe_upd", company="emc_upd",
                                             address="spb_upd", home="updated", mobile="updated", work="updated",
                                             fax="updated", email="", email2="x@mail.ru", email3="",
                                             homepage="", group="", address2="", phone2="", notes=""))


