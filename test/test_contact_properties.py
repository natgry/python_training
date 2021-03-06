from model.contact import Contact
import re
from random import randrange


def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="natalia", lastname="gryaznova", homephone="123-456",
                                   mobilephone="123-456", workphone="123-456", phone2="123-456"))
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_emails_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="natalia", lastname="gryaznova", homephone="123-456",
                                   mobilephone="123-456", workphone="123-456", phone2="123-456"))
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_name_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="natalia", lastname="gryaznova", homephone="123-456",
                                   mobilephone="123-456", workphone="123-456", phone2="123-456"))
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname


def test_address_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="natalia", lastname="gryaznova", homephone="123-456",
                                   mobilephone="123-456", workphone="123-456", phone2="123-456"))
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.address == contact_from_edit_page.address


def test_contact_properties_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="natalia", lastname="gryaznova", homephone="002",
                                   email="x@yandex.ru", address="spb", phone2="123-456"))
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address


def test_phones_on_view_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="natalia", lastname="gryaznova", homephone="123-456",
                                   mobilephone="123-456", workphone="123-456", phone2="123-456"))
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_view_page = app.contact.get_contact_info_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(str):
    return re.sub("[() -]", "", str)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                [contact.homephone, contact.mobilephone, contact.workphone, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                         filter(lambda x: x is not None,
                                [contact.email, contact.email2, contact.email3])))


def test_contact_properties_on_home_page_db_check(app, db):
    if len(db.get_contact_list()) < 2:
        app.contact.create(Contact(firstname="natalia", lastname="gryaznova", homephone="123-455",
                                   mobilephone="123-456", workphone="123-111", phone2="123-459", address='spb',
                                   email="x@yandex.ru", email2="xx@yandex.ru", email3="xxx@yandex.ru"))
        app.contact.create(Contact(firstname="ivan", lastname="gryaznov", homephone="123-456",
                                   mobilephone="123-457", workphone="123-457", phone2="123-458", address='spb',
                                   email="y@yandex.ru", email2="yy@yandex.ru", email3="yyy@yandex.ru"))
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()

    for contact in contacts_from_home_page:
        contact_db_data = list(filter(lambda x: x.id == contact.id, contacts_from_db))[0]
        assert contact.all_phones_from_home_page == merge_phones_like_on_home_page(contact_db_data)
        assert contact.all_emails_from_home_page == merge_emails_like_on_home_page(contact_db_data)
        assert contact.firstname == contact_db_data.firstname
        assert contact.lastname == contact_db_data.lastname
        assert contact.address == contact_db_data.address