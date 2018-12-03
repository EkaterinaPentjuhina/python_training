from model.contact_properties import Contact
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

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(maxlen):
    symbols = string.ascii_letters
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digit(maxlen):
    digits = string.digits
    return "".join([random.choice(digits) for i in range(random.randint(5, maxlen))])


def random_mix_string(maxlen, postfix):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + postfix


testdata = [
    Contact(firstname=random_string(10), lastname=random_string(15), middlename=random_string(15),
            nickname=random_string(7), title=random_string(15), company=random_string(15),
            homephone=random_digit(11), mobilephone=random_digit(11), workphone=random_digit(11), phone2=random_digit(11),
            email=random_mix_string(10, "@mail.ru"), homepage=random_mix_string(10, ".net"),
            address=random_string(20))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

