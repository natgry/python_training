from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_all_contacts(self):
        wd = self.app.wd
        self.app.open_home_page()
        nmb_contacts = self.count()
        if nmb_contacts != 0:
            for ndx in range(0, nmb_contacts):
                self.select_contact_by_index(ndx)
            # submit deletion
            wd.find_element_by_xpath("//input[@value='Delete']").click()
            wd.switch_to_alert().accept()
            self.contact_cache = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # open contact modification form
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        # fill contact form
        self.fill_contact_form(new_contact_data, modify=True)
        # submit modification
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # open contact modification form
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()
        # fill contact form
        self.fill_contact_form(new_contact_data, modify=True)
        # submit modification
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def add_contact_to_group_by_id(self, id, group):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # select group
        wd.find_element_by_xpath("//select[@name='to_group']/option[text()='%s']" % group.name).click()
        # submit adding
        wd.find_element_by_xpath("//input[@value='Add to']").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact, modify=False):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)
        if not modify:
            wd.find_element_by_xpath("//select[@name='new_group']/option[text()='%s']" % contact.group).click()


    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            table = wd.find_elements_by_xpath("//table[@class='sortcompletecallback-applyZebra']//tr[@name='entry']")
            for element in table:
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cells = element.find_elements_by_xpath("td")
                lastname = cells[1].text
                firstname = cells[2].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # open contact modification form
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # open contact view form
        wd.find_elements_by_xpath("//img[@title='Details']")[index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        address2 = wd.find_element_by_name("address2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, phone2=phone2,
                       email=email, email2=email2, email3=email3,
                       address=address, address2=address2)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text)
        mobilephone = re.search("M: (.*)", text)
        workphone = re.search("W: (.*)", text)
        phone2 = re.search("P: (.*)", text)
        homephone = '' if homephone is None else homephone.group(1)
        mobilephone = '' if mobilephone is None else mobilephone.group(1)
        workphone = '' if workphone is None else workphone.group(1)
        phone2 = '' if phone2 is None else phone2.group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, phone2=phone2)