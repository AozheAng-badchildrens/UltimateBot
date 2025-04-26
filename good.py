import re
def domain_check(domain):
    if re.match('^[A-Za-z][A-Za-z0-9-]*[.][A-Za-z][A-Za-z][A-Za-z]?$', domain) is None:
        return False
    return True