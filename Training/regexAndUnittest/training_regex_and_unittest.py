import re

def is_phone(number):
    return bool(re.match('^(06 |\+33 6 )([0-9]{2} ){3}[0-9]{2}$', number))\
    or bool(re.match('^(06|\+33 6)([0-9]{2}){4}$', number))

def is_mail(mail):
    return bool(re.match('^[a-zA-Z0-9.\-_]+@[a-zA-Z]+[.][a-zA-Z]+$', mail))
