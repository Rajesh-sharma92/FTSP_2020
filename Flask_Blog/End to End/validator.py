import re

def credit_card(card_no):
    reg = r'[456]+(\d{15}|\d{3}-(\d{4}-){2}\d{4})'
    chk = re.match(reg,card_no)
    rep = re.search(r'(\d)\1{3,}',card_no.replace('-',''))
    if chk and not rep:
        return "Valid"
    else:
        return "Invalid"
