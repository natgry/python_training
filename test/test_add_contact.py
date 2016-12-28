# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "-" + \
           "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(maxlen):
    letters = string.ascii_letters
    return "".join([random.choice(letters) for i in range(random.randrange(maxlen))]) + "@" + \
           "".join([random.choice(letters) for i in range(random.randrange(maxlen))]) + ".ru"


testdata = [Contact(firstname="", lastname="", middlename="")] + [
    Contact(firstname=random_string("firstname_", 10), middlename=random_string("middlename_", 20), lastname=random_string("lastname_", 20),
            homephone=random_phone(5), mobilephone=random_phone(5), workphone=random_phone(5), phone2=random_phone(5),
            address=random_string("address", 20), email=random_email(8), email2=random_email(8), email3=random_email(8))
    for i in range(0, 5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


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


