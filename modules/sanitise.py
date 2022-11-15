import re


def char_check(val, ret):
    x = re.search('^[a-zA-Z0-9]*$', val)
    if x:
        return ret
    else:
        return "Requested endpoint contains invalid characters", 400


def check_abc123(val):
    for i in val:
        x = re.search('^[a-zA-Z0-9]*$', i)
        if x:
            pass
        else:
            return False
    return True


def check_digits(val):
    for i in val:
        x = re.search('^[0-9]*$', i)
        if x:
            pass
        else:
            return False
    return True


def check_email(val):
    for i in val:
        x = re.search('^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})*$', i)
        if x:
            pass
        else:
            return False
    return True


def check_abc123_spaces(val):
    for i in val:
        x = re.search('^[a-zA-Z0-9 ]*$', i)
        if x:
            pass
        else:
            return False
    return True