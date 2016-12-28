# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_modify_some_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="natalia", middlename="alexandrovna", lastname="gryaznova",
                                   homephone="123-456", mobilephone="123-456", workphone="123-456", phone2="123-456"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="natalia updated", middlename="", lastname="gryaznova updated")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="natalia", lastname="gryaznova", email="-",
                                   homephone="123-456", mobilephone="123-456", workphone="123-456", phone2="123-456"))
    app.contact.modify_first_contact(Contact(email="x@mail.ru"))


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="natalia", middlename="alexandrovna", lastname="gryaznova",
                                   homephone="123-456", mobilephone="", workphone="", phone2=""))
    app.contact.modify_first_contact(Contact(firstname="natalia_upd", middlename="",
                                             lastname="gryaznova_upd", nickname="natgry_upd",
                                             title="sfe_upd", company="emc_upd",
                                             address="spb_upd", homephone="updated", mobilephone="updated", workphone="updated",
                                             fax="updated", email="", email2="x@mail.ru", email3="",
                                             homepage="", group="", address2="", phone2="123-456", notes=""))


