from model.contact import Contact
import random
import string


constant = [
    Contact(firstname="name1", lastname="lastname1", middlename="middlename1"),
    Contact(firstname="name2", lastname="lastname2", middlename="middlename2"),
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    symbols = "123456789"
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

