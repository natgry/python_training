from model.contact import Contact
import re


def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="natalia", lastname="gryaznova", homephone="123-456",
                                   mobilephone="123-456", workphone="123-456", phone2="123-456"))
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_view_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="natalia", lastname="gryaznova", homephone="123-456",
                                   mobilephone="123-456", workphone="123-456", phone2="123-456"))
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
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