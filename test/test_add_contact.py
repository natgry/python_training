# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="natalia", middlename="alex",
                      lastname="gryaznova", nickname="natgry",
                      title="sfe", company="emc",
                      address="spb", home="-", mobile="-", work="-", fax="-",
                      email="natgry@yandex.ru", email2="-", email3="-",
                      homepage="-", group="[none]", address2="-", phone2="-", notes="-")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="",
                      lastname="", nickname="",
                      title="", company="",
                      address="", home="", mobile="", work="", fax="",
                      email="", email2="", email3="",
                      homepage="", group="[none]", address2="", phone2="", notes="")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


