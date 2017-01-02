from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
    for i in range(0, n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
