from model.contact import Contact
import random


def test_delete_some_contact_by_id(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="natalia", lastname="gryaznova", homephone="123-456",
                                   mobilephone="123-456", workphone="123-456", phone2="123-456"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts


def test_delete_some_contact_by_index(app):
    from random import randrange
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="natalia", lastname="gryaznova", homephone="123-456",
                                   mobilephone="123-456", workphone="123-456", phone2="123-456"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts


def test_delete_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="natalia", lastname="gryaznova", homephone="123-456",
                                   mobilephone="123-456", workphone="123-456", phone2="123-456"))
    app.contact.delete_all_contacts()
    all_contacts = app.contact.get_contact_list()
    assert len(all_contacts) == 0