from fixture.db import DbFixture
from fixture.orm import ORMFixture

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
db_orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

print('\n******DB ORMFixture:******\n')
try:
    l = db_orm.get_group_list()
    for item in l:
        print(item)
    print(len(l))
    l = db_orm.get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    # orm connection is closed automatically
    pass # db_orm.destroy()

print('\n******DB DbFixture:******\n')
try:
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()