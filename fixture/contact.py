class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        # open contact modification form
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        # fill contact form
        self.fill_contact_form(new_contact_data, modify=True)
        # submit modification
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact, modify=False):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.firstname)
        self.change_field_value("nickname", contact.firstname)
        self.change_field_value("title", contact.firstname)
        self.change_field_value("company", contact.firstname)
        self.change_field_value("address", contact.firstname)
        self.change_field_value("home", contact.firstname)
        self.change_field_value("mobile", contact.firstname)
        self.change_field_value("work", contact.firstname)
        self.change_field_value("fax", contact.firstname)
        self.change_field_value("email", contact.firstname)
        self.change_field_value("email2", contact.firstname)
        self.change_field_value("email3", contact.firstname)
        self.change_field_value("homepage", contact.firstname)
        self.change_field_value("address2", contact.firstname)
        self.change_field_value("phone2", contact.firstname)
        self.change_field_value("notes", contact.firstname)
        if not modify:
            wd.find_element_by_xpath("//select[@name='new_group']/option[text()='" + contact.group + "']").click()

