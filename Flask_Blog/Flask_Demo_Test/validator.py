import re

def mobile_no(mob_no):
    reg = r'[456]+(\d{15}|\d{3}-(\d{4}-){2}\d{4})'
    chk = re.match(reg,mob_no)
    rep = re.search(r'(\d)\1{3,}',mob_no.replace('-',''))
    if chk and not rep:
        return "Valid"
    else:
        return "Invalid"
