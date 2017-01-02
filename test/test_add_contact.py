# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, data_contacts):
    contact = data_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# @pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
# def test_add_contact(app, contact):
#     old_contacts = app.contact.get_contact_list()
#     app.contact.create(contact)
#     assert len(old_contacts) + 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_contact_with_spaces(app):
#     app.contact.delete_all_contacts()
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="firstname_C  name", lastname="lastn  ame_GpHne  4P4vZQ")
#     app.contact.create(contact)
#     assert len(old_contacts) + 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     new_lastname_len = len(new_contacts[0].lastname)
#     new_firstname_len = len(new_contacts[0].firstname)
#     old_contacts.append(contact)
#     old_lastname_len = len(old_contacts[0].lastname)
#     old_firstname_len = len(old_contacts[0].firstname)
#     assert new_lastname_len == old_lastname_len
#     assert new_firstname_len == old_firstname_len
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


